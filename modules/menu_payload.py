#!/usr/bin/env python3

class MenuPayload:
    """
    This class is the payload that gets passed to every menu - including lambdas. This should make managing the
    different dependencies easier for developers.
    """
    def __init__(self, get_selected_devices, file_select_lambda, user_input_lambda, show_table_lambda, show_xml_lambda, exit_lambda):
        self.get_selected_devices = get_selected_devices
        self.file_select = file_select_lambda
        self.user_input = user_input_lambda
        self.show_table = show_table_lambda
        self.show_xml = show_xml_lambda
        self.exit = exit_lambda

    def run_on_all(self, fn):
        devices = self.get_selected_devices()
        for device in devices:
            fn(device)
