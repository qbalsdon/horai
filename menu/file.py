#!/usr/bin/env python3

import os

"""
Creates the menu options under the 'File' heading
"""
class FileMenu:
    def __init__(self, menu_payload):
        self.title = "File"
        self.order = 0
        self.menu_payload = menu_payload

        self.action_map = {
            "About" : lambda: print("TODO: Show about screen"),
            "Settings" : lambda: print("TODO: Show settings screen"),
            "scrcpy": [lambda: self.run_scrcpy(), "Command-s"],
            "record": lambda: self.record_scrcpy(),
            "Close" : lambda: self.menu_payload.exit()
        }

    def run_scrcpy(self):
        for device in self.menu_payload.get_all_selected_devices():
            device.scrcpy()

    def record_scrcpy(self):
        settings = self.menu_payload.load_settings()
        if "SAVE_FILE_LOCATION" not in settings or settings["SAVE_FILE_LOCATION"] == None:
            print("!! NO SAVE LOCATION SET !!")
            return
        for device in self.menu_payload.get_all_selected_devices():
            device.scrcpy_record()
