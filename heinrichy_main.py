# -*- coding: UTF-8 -*-

#               _   _      _            _      _
#              | | | | ___(_)_ __  _ __(_) ___| |__  _   _
#              | |_| |/ _ | | '_ \| '__| |/ __| '_ \| | | |
#              |  _  |  __| | | | | |  | | (__| | | | |_| |
#              |_| |_|\___|_|_| |_|_|  |_|\___|_| |_|\__, |
#                                                    |___/           _0.35_Alpha
#
#   Heinrichy - personal assistant made especially for GNU/Linux because we
#                   deserve our own version of siri too!
#								         by michpcx



# Modules to import first and setting variables
from __future__ import print_function
print("Loading main modules...")
import os
import sys
import json
import time
import random
import httplib2
from time import sleep
from timeit import timeit
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
current_path = os.path.dirname(os.path.abspath(__file__))

try:
    # Python2
    input = raw_input
    range = xrange
    from urllib import urlopen, urlencode
except NameError:
    # Python3
    from urllib.request import urlopen
    from urllib.parse import urlencode

print("Setting variables...")
clear = lambda: os.system('clear')
sys.dont_write_bytecode = True
schedule_list_for_today = [];

print("Changing the size of the terminal...")
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=115))



# Checking for config file
config_file = current_path + "/config.conf"
is_config_file = os.path.isfile(config_file)

if not is_config_file:
    print("Heinrichy - personal assistant made especially for GNU/Linux because we deserve our own version of siri too!")
    print("Heinrichy wasn't able to detect config file which is required to run, please redownload\n Heinrichy with this file...")
    print("Exiting...")
    sys.exit()
else:
    import configparser
    config = configparser.ConfigParser()
    config.read(config_file)

    # Loading user info
    name = config.get('user_info', 'name')
    date_of_birth = config.get('user_info', 'date_of_birth')

    # Loading main settings
    show_version = config.get('main_settings', 'show_version')
    clear_commands = config.get('main_settings', 'clear_commands')
    additional_search = config.get('main_settings', 'additional_search')
    letter_color = config.get('main_settings', 'letter_color')

    # Loading schedule module settings
    schedule_module = config.get('schedule_module', 'schedule_module')
    schedule_date_format = config.get('schedule_module', 'schedule_date_format')

    # Loading multimedia module settings
    multimedia_module = config.get('multimedia_module', 'multimedia_module')
    movie_directory = config.get('multimedia_module', 'movie_directory')

    print("Config file loaded...")



# Loading schedule module & schedule file
if schedule_module == "On":
    print("Loading schedule module...")
    schedule_file = current_path + "/schedule.json"
    schedule_module_file = current_path + "/modules/schedule.py"
    is_schedule_file = os.path.isfile(schedule_file)
    is_schedule_module = os.path.isfile(schedule_module_file)

    if not is_schedule_file or not is_schedule_module:
        print("Heinrichy wasn't able to detect schedule module or schedule file which is required to run schedule module.\n Heinrichy will start without this module...")
        schedule_module = "Off"
        sleep(5)
    else:
        with open(schedule_file, "r+") as schedule_file_open:
            schedule = json.load(schedule_file_open)



# Loading multimedia module
if multimedia_module == "On":
    print("Loading multimedia module...")
    multimedia_module_file = current_path + "/modules/multimedia.py"
    is_multimedia_module = os.path.isfile(multimedia_module_file)

    if not is_multimedia_module:
        print("Heinrichy wasn't able to detect multimedia module which is required to run it.\n Heinrichy will start without this module...")
        multimedia_module = "Off"
        sleep(5)
    elif is_multimedia_module:
        import modules.multimedia



# Classes & functions
print("Loading classes and functions...")

class bcolors:
    """ Load colors for the terminal """
    PINK = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = '\033[90m'

def list_schedule():
    """ List the schedule """
    total_task_number_today = 0
    print("Your today's schedule;")
    for task in schedule["schedule_list"].keys():
        if schedule["schedule_list"][task] == todays_date:
            print("- " + task)
            total_task_number_today = total_task_number_today + 1
    if total_task_number_today == 0:
        print("- Your schedule is empty for today!")
    print("\n")

# Prints the main
def print_main_screen():
    """ Print main 'Heinrichy' text """

    # Main 'Heinrichy' text
    print("___________________________________________________________________________________________________________________")
    print("|                                                                                                                 |")
    print("|                                                                                                                 |")
    print("|        " + color_changer + "ooooo   ooooo            o8o                        o8o            oooo" + bcolors.WHITE + "                                  |")
    print("|        " + color_changer + "`888'   `888'             ''                        `'            `888" + bcolors.WHITE + "                                   |")
    print("|         " + color_changer + "888     888   .ooooo.  oooo  ooo. .oo.   oooo d8b oooo   .ooooo.   888 .oo.   oooo    ooo" + bcolors.WHITE + "               |")
    print("|         " + color_changer + "888ooooo888  d88' `88b `888  `888P'Y88b  `888""8P  `888   d88' `'Y8  888P'Y88b   `88.   .8'" + bcolors.WHITE + "               |")
    print("|         " + color_changer + "888     888  888ooo888  888   888   888   888      888  888        888   888    `88..8'" + bcolors.WHITE + "                 |")
    print("|         " + color_changer + "888     888  888    .o  888   888   888   888      888  888   .o8  888   888     `888'" + bcolors.WHITE + "                  |")
    print("|        " + color_changer + "o888o   o888o `Y8bod8P' o888o o888o o888o d888b    o888o `Y8bod8P' o888o o888o     .8'" + bcolors.WHITE + "                   |")
    print("|                                                                                       " + color_changer + ".o..P'" + bcolors.WHITE + "                    |")
    if show_version == "True":
        print("|                                                                                       " + color_changer + "`Y8P'" + bcolors.WHITE + "        _0.35_Alpha  |")
    elif show_version == "False":
        print("|                                                                                       " + color_changer + "`Y8P'" + bcolors.WHITE + "                     |")
    print("|_________________________________________________________________________________________________________________|")

def print_schedule():
    """ Check if schedule module is on then print it """
    print("\n")
    if schedule_module == "On":
        list_schedule()
    elif schedule_module == "Off":
        print("\n")

def check_birthday():
    """ Check if its users' birthday """
    if schedule_date_format_type == 1:
        if date_of_birth[:5] == str(time.strftime("%d/%m")):
            print(bcolors.YELLOW + "Happy Birthday, " + name + "!\n" + bcolors.WHITE)
    elif schedule_date_format_type == 2:
        if date_of_birth[:5] == str(time.strftime("%m/%d")):
            print(bcolors.YELLOW + "Happy Birthday, " + name + "!\n" + bcolors.WHITE)
    elif schedule_date_format_type == 3:
        if date_of_birth[5:10] == str(time.strftime("%m/%d")):
            print(bcolors.YELLOW + "Happy Birthday, " + name + "!\n" + bcolors.WHITE)
    elif schedule_date_format_type == 4:
        if date_of_birth[5:10] == str(time.strftime("%d/%m")):
            print(bcolors.YELLOW + "Happy Birthday, " + name + "!\n" + bcolors.WHITE)

def response(query):
    """ Gets answer for users' query from wolframalpha servers """
    query = query.lower()
    query_original = query
    query = urlencode({'input':query})
    app_id = "Q6254U-URKKHH9JLL"
    wolfram_api = "http://api.wolframalpha.com/v2/query?appid="+app_id+"&format=plaintext&podtitle=Result&"+query
    resp, content = httplib2.Http().request(wolfram_api)
    root = ET.fromstring(content)
    error = root.get('error')
    success = root.get('success')
    numpods = root.get('numpods')
    answer= ''
    if success and int(numpods) > 0 :
        for plaintext in root.iter('plaintext'):
            if isinstance(plaintext.text, str) :
                answer = answer + plaintext.text
        return answer
    elif error:
        me_no_english1 = "Sorry, I didn't understood that."
        me_no_english2 = "I didn't get that."
        me_no_english3 = "I can't understand what you said."
        me_no_english4 = "It seems like I can't answer this question."
        me_no_english = [me_no_english1, me_no_english2, me_no_english3, me_no_english4]

        if additional_search == "True":
            query_original = query_original.replace(" ", "_")
            r = urlopen("https://www.evi.com/q/" + query_original).read()
            whole_content = BeautifulSoup(r, "lxml")
            answer = str(whole_content.find(class_="tk_common"))
            length = int(len(str(answer)))
            first_length = length - 9
            answer = answer[25:first_length]
            if answer.find('None'):
                return random.choice(me_no_english)
            else:
                return answer

        elif additional_search == "False":
            return random.choice(me_no_english)

        elif additional_search == "Ask":
            print("It seems like I can't answer this question.")
            print("Do you want me to send query to Evi? [Y/N]")
            user_input = input("[Y/N] >")
            if user_input == "Y" or user_input == "y":
                query_original = query_original.replace(" ", "_")
                r = urlopen("https://www.evi.com/q/" + query_original).read()
                whole_content = BeautifulSoup(r, "lxml")
                answer = str(whole_content.find(class_="tk_common"))
                length = int(len(str(answer)))
                first_length = length - 9
                answer = answer[25:first_length]
                if answer.find('None'):
                    return random.choice(me_no_english)
                else:
                    return answer
            elif user_input == "N" or user_input == "n":
                return "\n Press enter to reset."
            else:
                return "Wrong command."



# Setting up the colour of the letters
if letter_color == "BLUE":
    color_changer = bcolors.BLUE
elif letter_color == "GREY":
    color_changer = bcolors.GREY
elif letter_color == "PINK":
    color_changer = bcolors.PINK
elif letter_color == "YELLOW":
    color_changer = bcolors.YELLOW
elif letter_color == "GREEN":
    color_changer = bcolors.GREEN
elif letter_color == "RED":
    color_changer = bcolors.RED
elif letter_color == "WHITE":
    color_changer = bcolors.WHITE



# Setting up format of the dates
print("Setting up the format of the dates...")
if schedule_date_format == "DD/MM/YYYY":
    schedule_date_format_type = 1
    todays_date = str(time.strftime("%d/%m/%Y"))
elif schedule_date_format == "MM/DD/YYYY":
    schedule_date_format_type = 2
    todays_date = str(time.strftime("%m/%d/%Y"))
elif schedule_date_format == "YYYY/MM/DD":
    schedule_date_format_type = 3
    todays_date = str(time.strftime("%Y/%m/%d"))
elif schedule_date_format == "YYYY/DD/MM":
    schedule_date_format_type = 4
    todays_date = str(time.strftime("%Y/%d/%m"))
else:
    print("Invalid date format, please change 'schedule_date_format' in config file  to suitable format.")
    print("Exiting...")
    sys.exit()
todays_date = str(time.strftime("%d/%m/%Y"))



# -----------------------------------  Main  -----------------------------------

sleep(1)
clear()

if clear_commands == "True":
    while True:

        # Printing main 'Heinrichy' text
        clear()
        print_main_screen()

        # Printing out schedule
        print_schedule()

        # Printing out 'happy birthday'
        check_birthday()

        # Asking for user input
        print("How can I help you today, " + name + "?")
        user_input = input(">")
        if user_input == "schedule":
            if schedule_module == "On":
                exec(compile(open(schedule_module_file).read(), schedule_module_file, 'exec'))
            elif schedule_module == "Off":
                print("Schedule module has been turned off. Please change the config and restart Heinrichy.")
                pause = input()
        elif any(command in user_input for command in ("movies index", "movie index", "movies list", "movie list")) and multimedia_module == "Off":
            print("multimedia module has been turned off. Please change the config and restart Heinrichy.")
            pause = input()
        elif any(command in user_input for command in ("movies index", "movie index", "movies list", "movie list")) and multimedia_module == "On":
            if user_input == "movies index" or user_input == "movie index":
                modules.multimedia.index_all()
                pause = input()
            elif user_input[:11] == "movies list" or user_input[:10] == "movie list":
                if user_input.find("--") == -1:
                    args = "none"
                    modules.multimedia.list_all(args)
                else:
                    args = "--" + user_input.split('--', 1)[1]
                    modules.multimedia.list_all(args)
                pause = input()
        elif user_input == "movies help" or user_input == "movie help":
            modules.multimedia.movies_help()
            pause = input()
        else:
            print(response(user_input))
            pause = input()

elif clear_commands == "False":

    # Printing main 'Heinrichy' text
    print_main_screen()

    # Printing out schedule
    print_schedule()

    # Printing out 'happy birthday'
    check_birthday()

    # Asking for user input
    while True:

        print("How can I help you today, " + name + "?")
        user_input = input(">")
        if user_input == "schedule":
            if schedule_module == "On":
                exec(compile(open(schedule_module_file).read(), schedule_module_file, 'exec'))
            elif schedule_module == "Off":
                print("Schedule module has been turned off. Please change the config and restart Heinrichy.")
                pause = input()
        elif any(command in user_input for command in ("movies index", "movie index", "movies list", "movie list")) and multimedia_module == "Off":
            print("multimedia module has been turned off. Please change the config and restart Heinrichy.")
            pause = input()
        elif any(command in user_input for command in ("movies index", "movie index", "movies list", "movie list")) and multimedia_module == "On":
            if user_input == "movies index" or user_input == "movie index":
                modules.multimedia.index_all()
                pause = input()
            elif user_input[:11] == "movies list" or user_input[:10] == "movie list":
                if user_input.find("--") == 12:
                    args = "--" + user_input.split('--', 1)[1]
                    modules.multimedia.list_all(args)
                elif user_input.find("--") == -1:
                    args = "none"
                    modules.multimedia.list_all(args)
                else:
                    print("Seems like there is an error with your command.")
                pause = input()
        elif user_input == "movies help":
            modules.multimedia.movies_help()
            pause = input()
        else:
            print(response(user_input))
            pause = input()

else:
    print("Variable clear_commands has invalid value, please change it in config file to either True or False.")
    print("Exiting...")
    sys.exit()
