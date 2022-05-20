#!/usr/bin/env python3
import os
from subprocess import Popen, run, PIPE, STDOUT

class AndroidDevice:
    """
    Represents an android device. Can fetch UI as XML and run basic commands that interact with the Android Debug Bridge (adb)
    """
    def __init__(self, serial_number, alias="", scrcpy_flags=""):
        self.serial_number = serial_number
        self.alias = alias
        self.scrcpy_flags = scrcpy_flags

    # Run command
    def _run_command(self, command_params):
        return run(command_params, capture_output=True).stdout.decode().strip()

    def _run_command_async(self, command_params):
        command_params_no_blanks = [param for param in command_params if param]
        Popen(command_params_no_blanks, shell=False, stdout=PIPE, stderr=STDOUT)

    # Scrcpy "Screen Copy"
    def scrcpy(self):
        name = self.serial_number
        if self.alias != "":
            name = self.alias
        self._run_command_async(["scrcpy", "-s", self.serial_number, "--window-title", name, self.scrcpy_flags])

    def scrcpy_record(self, location):
        datestr = date.today().strftime("%d_%B_%Y")
        device_name = self.serial_number
        if self.alias != "":
            device_name = self.alias
        name = f"{location}/{device}-{device_name.replace(' ','_')}-{datestr}.mp4"
        # name = f"/Users/quba/Downloads/recording.mp4"
        title = f"RECORDING {device_name}"
        self._run_command_async(["scrcpy", "-s", self.serial_number, "--record", name, "--window-title", title])

    # Window dump
    def _remove_window_dump(self, fileReference):
        self.adb_command(["shell", "rm", fileReference], output=False)

    def fetch_window_dump(self):
        try:
            output = self.adb_command(["exec-out", "uiautomator", "dump"])
            file_to_read = output.replace("UI hierchary dumped to: ","")
            print(f" --> FILE DUMPED TO {file_to_read}")
            self.adb_command(["pull", file_to_read], output=False)
            xml_file = os.path.basename(file_to_read)
            print(f" --> reading {xml_file}")
            with open(xml_file) as file:
                data = file.read()
            os.remove(xml_file)
            self._remove_window_dump(file_to_read)
            return data
        except FileNotFoundError as e:
            return None

    # adb commands
    def _add_adb(self, parameters):
        params = parameters

        #check for adb
        if params[0] != "adb":
            params = ["adb"] + params

        # check for device flag
        if params[1] != "-s":
            params = [params[0]] + ["-s", str(self.serial_number)] + params[1:]
        return params

    def adb_command(self, parameters, output=True):
        command_params=self._add_adb(parameters)
        value = self._run_command(command_params)
        if output:
            return value
        else:
            return ""

    def adb_get_value(self, level, variable_name):
        command_params=self._add_adb(["shell", "settings", "get", level, variable_name])
        return self._run_command(command_params)

    def adb_set_value(self, level, variable_name, value):
        command_params=self._add_adb(["shell", "settings", "put", level, variable_name, value])
        self._run_command(command_params)

    def press_button(self, keycode):
        self.adb_command(["shell", "input", "keyevent", keycode])

    def type_text(self, text):
        self.adb_command(["shell", "input", "text", text.replace(" ", "\ ")])
