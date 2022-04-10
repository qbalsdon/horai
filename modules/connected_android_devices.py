#!/usr/bin/env python3
import subprocess

def get_device_list():
    return subprocess.run(["adb","devices"], capture_output=True).stdout.decode().strip().split('\n', 1)[-1]

if __name__ == "__main__":
    print(get_device_list())
