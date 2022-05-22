#!/usr/bin/env python3

import os
import json
import subprocess
import tkinter as tk

from modules import polling_client as PC
from modules import android_device as AD

def load_settings():
    if os.environ.get('HORAI_SETTINGS') is None:
        return None

    try:
        settings_file = os.environ['HORAI_SETTINGS']
        with open(settings_file, 'r') as file:
            data = file.read()
        if data == None or data == "":
            return {}
        return json.loads(data)
    except:
        return {}

def save_settings(data):
    data_str = json.dumps(data, indent = 4)
    try:
        settings_file = os.environ['HORAI_SETTINGS']
        with open(settings_file, 'w') as file:
            file.seek(0)
            file.write(data_str)
            file.truncate()
    except Exception as e:
        print("!! Error writing to file !!")
        print(e)

def is_adb_installed():
    try:
        subprocess.call(['adb', '--version'], stdout=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def start():
    root = tk.Tk()
    width = root.winfo_screenwidth() / 8 # create screen width
    height = root.winfo_screenheight() # get screen height
    root.geometry("%dx%d" % (width, height))

    root.title('Device Tray')
    icon = tk.PhotoImage(file = 'images/app_icon.png')
    root.iconphoto(False, icon)

    client = PC.PollingClient(root, load_settings, save_settings)
    root.mainloop()

if __name__ == "__main__":
    settings = load_settings()
    if settings == None:
        print("Unable to load settings. Ensure you have an environment variable named `HORAI_SETTINGS` and that the value is a file reference")
    elif not is_adb_installed():
        print("Unable to find adb. Ensure you have the Android Debug Bridge installed")
    else:
        # pixel5 = AD.AndroidDevice("13021FDD4005XC")
        # archos = AD.AndroidDevice("FS204602820")
        #
        # print("Pixel 5")
        # pixel5.fetch_window_dump()
        # print("Archos")
        # archos.fetch_window_dump()

        start()
