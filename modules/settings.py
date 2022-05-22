#!/usr/bin/env python3

import tkinter as tk
from tkinter import Frame, Label, Entry, StringVar, Button, filedialog, BOTH, YES, LEFT, RIGHT, END

SAVE_LOCATION_KEY = "save_location"

class SettingsEditor:
    def __init__(self, menu_payload):
        self.menu_payload = menu_payload
        self.settings = self.menu_payload.load_settings()
        self.__create_window()

    def __create_window(self):
        self.window = tk.Toplevel()
        self.window.title("Settings")

        self.__create_save_location_section()
        self.__create_save_cancel_section()

    # Main button events
    def __save_settings(self):
        self.menu_payload.save_settings(self.settings)
        self.__close_settings()

    def __close_settings(self):
        self.window.destroy()

    # Building UI sections
    def __create_save_location_section(self):
        self.save_location_frame = Frame(self.window)
        self.save_location_label = Label(self.save_location_frame, text="Save location")
        self.save_location_label.pack(side=LEFT)

        save_location = ""
        if SAVE_LOCATION_KEY in self.settings:
            save_location = self.settings[SAVE_LOCATION_KEY]

        self.save_location_variable = StringVar(self.save_location_frame, value=save_location)
        self.save_location_input = Entry(self.save_location_frame, bd=1, textvariable=self.save_location_variable)
        self.save_location_input.pack(side=LEFT, fill=BOTH, expand=YES)

        self.save_location_choose = Button(self.save_location_frame, text="...", command=self.__find_folder)
        self.save_location_choose.pack(side=RIGHT)
        self.save_location_frame.pack(fill=BOTH, expand=YES)

    def __create_save_cancel_section(self):
        self.save_cancel_section_frame = Frame(self.window)

        self.save_button = Button(self.save_cancel_section_frame, text="Save", command=self.__save_settings)
        self.save_button.pack(side=LEFT)

        self.cancel_button = Button(self.save_cancel_section_frame, text="Cancel", command=self.__close_settings)
        self.cancel_button.pack(side=RIGHT)

        self.save_cancel_section_frame.pack(fill=BOTH, expand=YES)

    # Button events
    def __find_folder(self):
        path = ''
        if SAVE_LOCATION_KEY in self.settings:
            save_location = self.settings[SAVE_LOCATION_KEY]
            path = filedialog.askdirectory(title="Select default save directory", initialdir=save_location)
        else:
            path = filedialog.askdirectory(title="Select default save directory")

        if path != '':
            self.save_location_input.delete(0, END)
            self.save_location_input.insert(0, path)
            self.save_location_variable.value = path
            self.settings[SAVE_LOCATION_KEY] = path
