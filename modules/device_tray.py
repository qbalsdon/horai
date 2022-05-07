#!/usr/bin/env python3
import queue

import tkinter as tk
import time

from tkinter import ttk
from tkinter import Menu
from tkinter import simpledialog
from tkinter import filedialog as fd

from modules import connected_android_devices, menu_builder, menu_payload
from modules.xml_viewer import XML_Viewer

class DeviceTray:

    def clear_frame(self, container):
        for widget in container.winfo_children():
           widget.destroy()
        container.pack_forget()

    def device_name_formatted(self, device_serial):
        name = None #get_device_name(device_serial)
        if name == None:
            name = device_serial
        else:
            name = f"{name} ({device_serial[0:5]}...)"
        return name

    def create_binding(self, listener, binding_name, fn):
        binding = f"<{binding_name}>"
        if len(binding_name) == 1:
            binding = f"{binding_name}"
        # print(f"Key bind: [{binding}]")
        listener.bind_all(binding, lambda event: fn())

    def toggle_device(self, device_serial, str_var):
        if str_var.get() == device_serial:
            str_var.set("")
        else:
            str_var.set(device_serial)

    def populate_devices_frame(self, container):
        self.clear_frame(container)
        previous_selection = []
        for var in self.user_devices:
            if len(var.get()) > 0:
                previous_selection.append(var.get())

        self.user_devices = []
        devices_list = connected_android_devices.get_device_list()
        if devices_list.splitlines()[0] != 'List of devices attached':
            current_row = 0
            for line in devices_list.splitlines():
                data = line.split("\t")
                selected_device = tk.StringVar()
                name = self.device_name_formatted(data[0])

                device_check = ttk.Checkbutton(
                    container,
                    text=name,
                    onvalue=data[0],
                    offvalue="",
                    compound='left',
                    variable=selected_device)
                if data[0] in previous_selection:
                    selected_device.set(data[0])
                self.user_devices.append(selected_device)

                device_check.pack(fill=tk.X, side=tk.TOP, padx=(10, 10), pady=(5, 5))
                current_row = current_row + 1
                self.create_binding(
                    device_check,
                    f"{current_row}",
                    lambda device_serial=data[0], variable=selected_device: self.toggle_device(device_serial, variable)
                )

    def create_device_frame(self, container):
        devices_frame = ttk.Frame(container)
        devices_frame.grid(row=1, column=0, columnspan=1, sticky='NW', pady=(5, 5))
        self.populate_devices_frame(devices_frame)
        return devices_frame

    def selected_device_list(self):
        mapped = list(map((lambda var: var.get()), self.user_devices))
        return list(filter(lambda value: len(value) > 0, mapped))

    def find_file(self):
        filename = fd.askopenfilename()
        return filename

    def get_user_input(self, prompt):
        return simpledialog.askstring(title="Input", prompt=prompt)

    def create_window_table(self, root, title, data, show_names=False):
        window = tk.Toplevel(root)
        window.title(title)
        row = 0
        for key in data.keys():
            label = ttk.Label(window, text=key, borderwidth=2, relief="solid")
            label.grid(row=row, column=0, sticky='WE')
            next_col = 1
            if show_names:
                name = get_device_name(key)
                if name == key:
                    name = "..."
                label = ttk.Label(window, text=name, borderwidth=2, relief="solid")
                label.grid(row=row, column=next_col, sticky='WE')
                next_col = next_col + 1
            text = ttk.Label(window, text=data[key], borderwidth=2, relief="solid")
            text.grid(row=row, column=next_col, sticky='WE')
            row = row + 1

    def show_table(self, root, device_data):
        if isinstance(list(device_data.items())[0][1], str):
            self.create_window_table(root, "Summary", device_data, True)
        else:
            for data in device_data:
                self.create_window_table(root, self.device_name_formatted(data), device_data[data])

    def create_xml_window(self, root, title, xml):
        window = tk.Toplevel(root)
        window.title(title)
        XML_Viewer(window, xml, heading_text=title).pack(fill='both', expand=True)

    def show_xml(self, root, device_data):
        for device in device_data:
            self.create_xml_window(root, self.device_name_formatted(device), device_data[device])

    def __init__(self, root, queue, endCommand):
        self.queue = queue
        self.user_devices = []
        # Set up the GUI
        root.title('Device Tray')
        icon = tk.PhotoImage(file = 'images/app_icon.png')
        root.iconphoto(False, icon)

        # action_mapper = ActionMapper(
        #     self.selected_device_list,
        #     self.find_file,
        #     self.get_user_input,
        #     lambda data: self.show_table(root, data),
        #     lambda data: self.show_xml(root, data),
        #     lambda: root.destroy())

        payload = menu_payload.MenuPayload(
            self.selected_device_list,
            self.find_file,
            self.get_user_input,
            lambda data: self.show_table(root, data),
            lambda data: self.show_xml(root, data),
            lambda: root.destroy()
        )
        menu, key_bindings = menu_builder.create_menu(root, payload)

        self.devices_frame = self.create_device_frame(root)
        self.devices_frame.grid(row=0, column=0, sticky='NWS')
        # for binding in key_bindings:
        #     if "-" in binding:
        #         arr=binding.split("-")
        #         modifier = arr[0]
        #         key = arr[1]
        #         if len(key) == 1:
        #             key = key.lower()
        #         binding_name=f"{modifier}-{key}"
        #     else:
        #         binding_name=f"{binding.lower()}"
        #     self.create_binding(root, binding_name, key_bindings[binding])

    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                self.populate_devices_frame(self.devices_frame)
                # Check contents of message and do whatever is needed. As a
                # simple test, print it (in real life, you would
                # suitably update the GUI's display in a richer fashion).
            except queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass
