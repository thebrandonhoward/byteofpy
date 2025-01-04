"""Startup module to do initial setup"""
import os
import sys
import time

from pprint import pprint

# -------------------------------------------------------------------------------------------------
THIS_FILENAME = __file__

class DTO():
    """Class to hold setup variables"""
    def __init__(self):
        self.greeting = "Hello!"
        self.startup_message = f"Starting up {THIS_FILENAME}..."
        self.clear_prompt = "Clear console before starting(y/n)? "
        self.should_clear = False
        self.sleep_time = 5

# -------------------------------------------------------------------------------------------------
def startup(dto):
    """Main method of execution"""
    prompt(dto)
    addline()

    print(dto.startup_message)
    time.sleep(dto.sleep_time)
    greet(dto)
    addline()

    info()
    addline()

    print("-" * 45)
    addline()

def addline():
    """Print an empty line"""
    print()

def prompt(dto):
    """Handle user prompts"""
    clrresp = input(dto.clear_prompt)
    if clrresp.lower() == 'y' or clrresp.lower() == "yes":
        os.system('clear')

def greet(dto):
    """Handle greeting message"""
    print(dto.greeting)

def info():
    """Prints system related info"""
    print(sys.version)
    pprint(sys.version_info)
    print(sys.platform)
    print(sys.argv)
    pprint(globals())

# -------------------------------------------------------------------------------------------------
startup(DTO())
