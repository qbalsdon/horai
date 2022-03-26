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

#### TODO
  - When opened, check for
    - settings
    - adb
      - if none present, dialog and exit
      - if present, read into a variable
  - After settings load
    - show a screen tray with devices
    - devices that are not listed as "device" must have a signal that there is a problem
    - allow device selection to be toggled by numbers 1 - 0
    - COMMAND+S will start scrcpy on all selected devices
    - when a device is saved - check where the UI automator dumps output and save that with it

#### BUGS

#### DONE


## About
This is a labour of love regarding automation. The goal is to let developers access what they need to quicker and do less command line management. I wrote the original scripts in bash, then re-did them in Python, and now I want to create an easy interface, requiring a new re-write.


  [0]: https://github.com/Genymobile/scrcpy
  [1]: https://developer.android.com/studio/command-line/adb