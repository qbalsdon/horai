#!/usr/bin/env python3
import os

class AndroidDevice:
    """
    Represents an android device. Can fetch UI as XML and run basic commands that interact with the Android Debug Bridge (adb)
    """
    def __init__(self, serial_number, alias, scrcpy_flags, ui_dump_location):
        self.serial_number = serial_number
        self.alias = alias
        self.scrcpy_flags = scrcpy_flags
        self.ui_dump_location = ui_dump_location

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
        if output:
            return subprocess.run(command_params, capture_output=True).stdout.decode().strip()
        else:
            subprocess.run(command_params, capture_output=True)
        return ""

    def _remove_window_dump(self, fileReference):
        self.adb_command(["shell", "rm", fileReference], output=False)

    def fetch_window_dump(self):
        xml_file="window_dump.xml"
        file_to_read = f"{self.ui_dump_location}{xml_file}"
        try:
            self._remove_window_dump(file_to_read)
            self.adb_command(["exec-out", "uiautomator", "dump"], output=False)
            self.adb_command(["pull", file_to_read], output=False)
            with open(xml_file) as file:
                data = file.read()
            os.remove(xml_file)
            self._remove_window_dump(file_to_read)
            return data
        except FileNotFoundError as e:
            return None

    def adb_get_value(self, level, variable_name, output=True):
        command_params=self._add_adb(["shell", "settings", "get", level, variable_name])
        value = subprocess.run(command_params, capture_output=True).stdout.decode().strip()
        return value

    def adb_set_value(self, level, variable_name, value, device=None, output=True):
        command_params=self._add_adb(["shell", "settings", "put", level, variable_name, value])
        subprocess.run(command_params, capture_output=True)

    def press_button(keycode):
        self.adb_command(["shell", "input", "keyevent", keycode])

    def type_text(text):
        self.adb_command(["shell", "input", "text", text.replace(" ", "\ ")])
