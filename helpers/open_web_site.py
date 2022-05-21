#!/usr/bin/env python3
from subprocess import run
from sys import platform

"""
Helper module to open a web page
"""

def open_web_page(url_string):
    # TODO: test windows version
    if platform == "win32":
        run(["rundll32", "url.dll,FileProtocolHandler", url_string], capture_output=False)
        return
    run(["open",url_string], capture_output=False)

if __name__ == "__main__":
    open_web_page("https://qbalsdon.github.io/")
