# horai
An Android Device GUI written in Python

The aim of this project is to allow Android Developers and testers greater control of their Android devices. It's written in Python 3 so that it can be cross platform.

## Requirements
  - [Android Debug Bridge (ADB)][1]
  - Python 3 (required)
  - tkinter (required)
  - A writable text file referenced in an environment variable called `horai.settings`

## Optional dependencies
  - GenyMotion's [scrcpy][0] (optional, but assumed)

## Development process
All settings are optional. The development should happen in such a manner that assumes the setting is not present or could be in a different format. Always try be backwards compatible.

## Features

  - Dynamic sub menus that are loaded at run time. This means you can have specific menu items for your app
  - Constant `adb devices` refresh with the tray. Allowing users to see what devices are connected
  - Quick recording option using scrcpy
  - Faster device navigation and manipulation

#### TODO
  - When opened, check for
    - :white_check_mark: settings
    - :white_check_mark: adb
      - if none present, dialog and exit
      - if present, read into a variable
  - :white_check_mark: After settings load
    - show a screen tray with devices
    - devices that are not listed as "device" must have a signal that there is a problem
    - allow device selection to be toggled by numbers 1 - 0 (10)
    - ~when a device is saved -~ check where the UI automator dumps output and save that with it
  - Menu system
    - Have a base menu
      - Save device settings
      - Load device settings
      - Edit recording directory
      - COMMAND+S will start scrcpy on all selected devices
    - Load menus from a folder
      - Android menu: Current Activity name, Open settings, System report, Layout inspector, Quick navigate
      - Layout inspector
        - Improved search
        - Simple render
    - Load menus from a folder that is ignored in git
      - Have an example menu file
      - Must have package name, friendly name

#### BUGS

## About
This is a labour of love regarding automation. The goal is to let developers access what they need to quicker and do less command line management. I wrote the original scripts in bash, then re-did them in Python, and now I want to create an easy interface, requiring a new re-write.

All images are subject to copyright on [FreePik][2] and are used with my paid subscription.


  [0]: https://github.com/Genymobile/scrcpy
  [1]: https://developer.android.com/studio/command-line/adb
  [2]: https://www.freepik.com
