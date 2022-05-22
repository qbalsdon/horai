#!/usr/bin/env python3

from subprocess import run
from sys import platform

from helpers.open_web_site import open_web_page

from modules.settings import SAVE_LOCATION_KEY

"""
Creates the menu options under the 'Scrcpy' heading
"""
class ScrcpyMenu:
    def __init__(self, menu_payload):
        self.title = "Scrcpy"
        self.order = 1
        self.menu_payload = menu_payload

        self.action_map = {
            "About": lambda: open_web_page("https://github.com/Genymobile/scrcpy"),
            "scrcpy": [lambda: self.run_scrcpy(), "Command-s"],
            "record": lambda: self.record_scrcpy(),
            "Close Windows":  lambda: self.close_windows()
        }

    def run_scrcpy(self):
        for device in self.menu_payload.get_all_selected_devices():
            device.scrcpy()

    def record_scrcpy(self):
        settings = self.menu_payload.load_settings()
        if SAVE_LOCATION_KEY not in settings or settings[SAVE_LOCATION_KEY] == None:
            print("!! NO SAVE LOCATION SET !!")
            return
        for device in self.menu_payload.get_all_selected_devices():
            device.scrcpy_record(settings[SAVE_LOCATION_KEY])

    def close_windows(self):
        # TODO: test windows version
        if platform == "win32":
            run(["Taskkill", "/IM", "scrcpy", "/f"], capture_output=False)
            return
        run(["pkill","scrcpy"], capture_output=False)
