#!/usr/bin/env python3

import tkinter as tk
from tkinter import Menu

from os import listdir
from os.path import isfile, join

from menu.file import FileMenu

def create_cascade(parent, list_name, action_list, key_binding):
    menu_item = Menu(
        parent,
        tearoff=0
    )
    for key in action_list:
        if type(action_list[key]) is dict:
            menu_item.add_separator()
            menu_item.add_cascade(
                label=key,
                menu=create_cascade(menu_item, key, action_list[key], key_binding)
            )
        elif type(action_list[key]) is list:
            menu_item.add_command(
                label=key,
                command=action_list[key][0],
                accelerator=action_list[key][1]
            )
            key_binding[action_list[key][1]] = action_list[key][0]
        else:
            menu_item.add_command(
                label=key,
                command=action_list[key]
            )
    return menu_item

def create_menu(root_window, payload):
    # create the menu
    menubar = Menu(root_window)
    key_binding = {}
    root_window.config(menu=menubar)

    # load the built in menus
    built_in_menus = [
        FileMenu(payload)
    ]

    # load the custom menus
    custom_menus = [

    ]

    # Combine all the menus
    all_menus = built_in_menus + custom_menus
    # populate the menu bar
    for menuItem in all_menus:
        menubar.add_cascade(
            label=menuItem.title,
            menu=create_cascade(menubar, menuItem.title, menuItem.action_map, key_binding),
            underline=0
        )

    return menubar, key_binding
