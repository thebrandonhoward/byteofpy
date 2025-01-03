import os
import sys
import time

from pprint import pprint

# -------------------------------------------------------------------------------------------------
thisfile = __file__

class DTO():
    def __init__(self):
        self.greeting = "Hello!"
        self.startupMessage = f"Starting up {thisfile}..."
        self.clearPrompt = "Clear console before starting(y/n)? "
        self.shouldClear = False
        self.sleepTime = 5

# -------------------------------------------------------------------------------------------------
def startup(dto):
    prompt(dto)
    addline()

    print(dto.startupMessage)
    time.sleep(dto.sleepTime)
    greet(dto)
    addline()

    info()
    addline()

    print("-" * 45)
    addline()

def addline():
    print()

def prompt(dto):
    clrresp = input(dto.clearPrompt)
    if clrresp.lower() == 'y' or clrresp.lower() == "yes":
        os.system('clear')

def greet(dto):
    print(dto.greeting)

def info():
    print(sys.version)
    pprint(sys.version_info)
    print(sys.platform)
    print(sys.argv)
    pprint(globals())

# -------------------------------------------------------------------------------------------------
startup(DTO())