#!/usr/bin/env python3

import os

class FileMenu:
    def __init__(self, menu_payload):
        self.title = "File"
        self.order = 0
        self.menu_payload = menu_payload

        self.action_map = {
            "About" : lambda: print("TODO: Show about screen"),
            "scrcpy": [lambda: self.execute_command(device_scrcpy), "Command-s"],
            "record": lambda: self.execute_command(device_record),
            "Exit scrcpy": lambda: run_command(["pkill","scrcpy"]),
            "Close" : lambda: self.menu_payload.exit()
        }

    def execute_command(self, command):
        print (f"execute_command invoked: {command}")
        # run_on_all_selected_devices(command, self.selected_devices_lambda())
