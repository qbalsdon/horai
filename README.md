# horai
An Android Device GUI written in Python

The aim of this project is to allow Android Developers and testers greater control of their Android devices. It's written in Python 3 so that it can be cross platform.

## Requirements
  - [Android Debug Bridge (ADB)][1]
  - Python 3 (required) - Developed with `Python 3.9.12`
  - tkinter (required)
  - A writable text file referenced in an environment variable called `HORAI_SETTINGS`

## Optional dependencies

### On your computer
  - GenyMotion's [scrcpy][0] (optional, but assumed) - Developed with `scrcpy 1.24`

### On your Android device
  - [Accessibility scanner][4]
  - [Accessibility Broadcast Dev][3]

## How to set up

Ensure you have the following environment variables:
1. The location of the Android Debug Bridge added to the path
2. An environment variable called `HORAI_SETTINGS` that leads to a writable file (settings will be written here as json)

### Mac OS

#### Environment variables
```
## ~/.zshenv
export PATH=$PATH:~/Library/Android/sdk/platform-tools/
export HORAI_SETTINGS=~/HORAI.SETTINGS
```


### Windows

TODO

## Development process

All settings are optional. The development should happen in such a manner that assumes the setting is not present or could be in a different format. Always try be backwards compatible.

## Features

  - Dynamic sub menus that are loaded at run time. This means you can have specific menu items for your app
  - Constant `adb devices` refresh with the tray. Allowing users to see what devices are connected
  - Quick recording option using scrcpy
  - Faster device navigation and manipulation

#### TODO
  - :white_check_mark: When opened, check for
    - :white_check_mark: settings
    - :white_check_mark: adb
      - if none present, dialog and exit
      - if present, read into a variable
  - :white_check_mark: After settings load
    - :white_check_mark: show a screen tray with devices
    - :white_check_mark: devices that are not listed as "device" must have a signal that there is a problem
    - :white_check_mark: allow device selection to be toggled by numbers 1 - 0 (10)
    - :white_check_mark: ~when a device is saved -~ check where the UI automator dumps output and save that with it
  - Menu system
    - :white_check_mark: Have a base menu
      - [CURRENT] Save settings
        - Have a menu item for general settings, e.g. save file location
        - Have a menu for per device settings
      - :white_check_mark: Load device settings
      - :white_check_mark: COMMAND+S will start scrcpy on all selected devices
    - ~Load menus from a folder~ : Not doing
      - Android menu: Current Activity name, Open settings, System report, Layout inspector, Quick navigate
      - Layout inspector
        - Improved search
        - Simple render
    - :white_check_mark: Load menus from a folder that is ignored in git
      - Have an example menu file
      - Must have package name, friendly name
      - Document the process of adding a new menu
    - Menus:
      - Inputs
        - Buttons
        - Text
      - Common Screens (settings, locale, accessibility, etc)
      - Accessibility
        - Toggle TalkBack
        - Toggle Voice Access
        - Toggle Switch Access
        - Toggle 3rd party tools
          - [Accessibility Broadcast Dev][3]
            - Toggle
            - Perform user actions (next, previous, open menu, etc)
          - [Accessibility scanner][4]
          - Find other great tools
        - Things to do with size
          - Font
          - Scale
        - Things to do with colour
          - Font
          - Scale
          - Dark mode toggle
        - Toggle Animations
          - toast state (whether they are on or not)

## About
This is a labour of love regarding automation. The goal is to allow developers access what they need to quicker and do less command line management. I wrote the original scripts in bash, then re-did them in Python, did a quick and dirty UI. Now I want to create an easy hackable interface, requiring a new re-write.

All images are subject to copyright on [FreePik][2] and are used with my personal paid subscription.


  [0]: https://github.com/Genymobile/scrcpy
  [1]: https://developer.android.com/studio/command-line/adb
  [2]: https://www.freepik.com
  [3]: https://github.com/qbalsdon/accessibility_broadcast_dev
  [4]: https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor
