#!/usr/bin/env python3

from modules import android_device as AD

class MenuPayload:
    """
    This class is the payload that gets passed to every menu - including lambdas. This should make managing the
    different dependencies easier for developers.
    """
    def __init__(self,
                 window_root,
                 get_selected_devices,
                 load_settings,
                 save_settings,
                 exit_lambda):
        self.get_selected_devices = get_selected_devices
        self.window_root = window_root,
        self.load_settings = load_settings
        self.save_settings = save_settings
        self.exit = exit_lambda

    def run_on_all(self, fn):
        device_serials = self.get_selected_devices()
        for device_serial in device_serials:
            fn(device_serial)

    def get_all_selected_devices(self):
        device_serials = self.get_selected_devices()
        settings = self.load_settings()

        device_list = []
        for serial in device_serials:
            alias = ""
            srccpy_params = ""
            if settings != None:
                # TODO: get device alias and scrcpy params from settings if they exist
                pass
            device_list.append(AD.AndroidDevice(serial, alias, srccpy_params))

        return device_list
