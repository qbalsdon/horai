#!/usr/bin/env python3

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
            "Close" : lambda: self.menu_payload.exit()
        }
