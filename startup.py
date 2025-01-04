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
        self.startup_message = f"Starting up {THIS_FILENAME}."
        self.clear_prompt = "Clear console before starting(y/n)? "
        self.should_clear = False
        self.sleep_time = 1

    def __str__(self):
        return str(self.__dict__)

    def setshouldclear(self, should_clear):
        """Set clear terminal value"""
        self.should_clear = should_clear
# -------------------------------------------------------------------------------------------------
def startup(dto):
    """Main method of execution"""
    prompt(dto)
    addline()

    greet(dto)
    print(dto.startup_message)

    for s in range(0, 5):
        print("-> ->", end=" ")
        sys.stdout.flush()
        time.sleep(dto.sleep_time)

    addline()
    addline()

    info(dto)
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
        dto.setshouldclear(True)
        os.system('clear')

def greet(dto):
    """Handle greeting message"""
    print(dto.greeting)

def info(dto):
    """Prints system related info"""
    print(sys.version)
    pprint(sys.version_info)
    print(sys.platform)
    print(sys.argv)
    print(dto)
    pprint(globals())

# -------------------------------------------------------------------------------------------------
startup(DTO())
