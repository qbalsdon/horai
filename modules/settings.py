#!/usr/bin/env python3

import tkinter as tk

class SettingsEditor:
    def __init__(self, root):
        self.root = root
        window = tk.Toplevel(root)
        window.title("Settings")
        window.geometry("%dx%d" % (300, 300))
