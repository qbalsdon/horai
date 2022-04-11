#!/usr/bin/env python3

import os
import subprocess
import tkinter as tk

from modules import polling_client as PC

def load_settings():
    try:
        settings_file = os.environ['HORAI_SETTINGS']
        with open(settings_file, 'r') as file:
            data = file.read()
        if data == None or data == "":
            return {}
        return json.loads(data)
    except:
        return {}

# TODO
def save_settings(data):
    pass

def is_adb_installed():
    try:
        subprocess.call(['adb', '--version'], stdout=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def start():
    root = tk.Tk()
    width = root.winfo_width() #get root width size
    height = root.winfo_screenheight() #get screen height size
    root.geometry("%dx%d" % (width, height))

    client = PC.PollingClient(root, load_settings)
    root.mainloop()

if __name__ == "__main__":
    settings = load_settings()
    if settings == None:
        print("Unable to load settings. Ensure you have an environment variable named `HORAI_SETTINGS` and that the value is a file reference")
    elif not is_adb_installed():
        print("Unable to find adb. Ensure you have the Android Debug Bridge installed")
    else:
        start()
