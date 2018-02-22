"""Detect OS"""
from platform import system


def detect_os(bypass=False):
    """Check OS, as multithreading may not work properly on Windows and macOS"""
    if bypass is True:
        return

    os_name = system()

    if os_name in ['Windows']:
        print("It seems that you are running this code from {}, on which the Python multithreading may not work properly. Consider running this code on Linux.".format(os_name))
        print("Exiting..")
        exit()
    else:
        print("Linux is fine! Python multithreading works.")
