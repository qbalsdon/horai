#!/usr/bin/env python3

import tkinter as tk

class SettingsEditor:
    def __init__(self, menu_payload):
        self.menu_payload = menu_payload
        __create_window()

    def __create_window():
        window = tk.Toplevel()
        window.title("Settings")
        window.geometry("%dx%d" % (300, 300))
