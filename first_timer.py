# -*- coding: UTF-8 -*-

#               _   _      _            _      _
#              | | | | ___(_)_ __  _ __(_) ___| |__  _   _
#              | |_| |/ _ | | '_ \| '__| |/ __| '_ \| | | |
#              |  _  |  __| | | | | |  | | (__| | | | |_| |
#              |_| |_|\___|_|_| |_|_|  |_|\___|_| |_|\__, |
#                                                    |___/           _0.38_Alpha
#
#   Heinrichy - personal assistant made especially for GNU/Linux because we
#                   deserve our own version of siri too!
#								         by michpcx



# Script first_timer.py allows Heinrichy to analyse the environment to see if you can run Heinrichy.

from __future__ import print_function
import sys
from sys import platform as _platform
sys.dont_write_bytecode = True



try:
    # Python2
    input = raw_input
    range = xrange
except NameError:
    # Python3
    pass



# Functions
def check_os():
    if _platform == "linux" or _platform == "linux2":
        print("GNU/Linux detected...")
    else:
        print("You are not using GNU/Linux which is required for Heinrichy to work properly.")
        non_linux = input("Do you want to continue anyway? [Y/N]")
        if non_linux.lower() == "y":
            print("Very well then, continuing to proceed with the script...")
        elif non_linux.lower() == "n":
            print("Exiting...")
            sys.exit()
        else:
            print("Wrong command, exiting...")
            sys.exit()

def check_python_version():
    python_version = str(sys.version_info[:2])
    if not python_version == "(2, 7)" and not python_version == "(3, 5)":
        print("You are not using python 2.7 or python 3.5 which is recommended for Heinrichy to work properly...")
        unknown_version = input("Do you want to continue anyway? [Y/N]")
        if unknown_version.lower() == "y":
            print("Very well then, continuing to proceed with the script...")
        elif unknown_version.lower() == "n":
            print("Exiting...")
            sys.exit()
        else:
            print("Wrong command, exiting...")
            sys.exit()
    else:
        print("2.7 or 3.5 version of python detected...")

def check_dependencies():
    try:
        from bs4 import BeautifulSoup
        print("BeautifulSoup module detected...")
    except NameError:
        print("You don't have installed BeautifulSoup module which is required for Heinrichy.")
        print("Please run 'pip install beautifulsoup' as root and run this script again.")
        print("Exiting...")
        sys.exit()
    try:
        from colorama import *
        print("Colorama module detected...")
    except NameError:
        print("You don't have installed Colorama module which is required for Heinrichy.")
        print("Please run 'pip install colorama' as root and run this script again.")
        print("Exiting...")
        sys.exit()
    print("Warning; multimedia module in Heinrichy requires you to download about 5(+) dependencies. Are you sure you want to use this module? [Y/N]")
    user_input = input("[Y/N]>")
    if user_input.lower() == "n":
        print("To disable multimedia module just change value in config 'multimedia_module' from 'On' to 'Off'.")
    elif user_input.lower() == "y":
        try:
            import guessit
            import terminaltables
            import urllib
            import docopt
            import tqdm
            import colorama
        except NameError:
            print("One or more of the modules isn't loading, please make sure you have downloaded; ")
            dependencies_list = ["guessit", "terminaltables", "urllib", "docopt", "tqdm", "coloram"]
            for item in dependencies_list:
                print("-" + item)
    else:
        print("Wrong command, exiting...")
        sys.exit()

if __name__ == "__main__":
    print("Begining to scan the environment...")
    check_os()
    check_python_version()
    check_dependencies
    print("Looks like your system is able to run Heinrichy!")
    sys.exit()
