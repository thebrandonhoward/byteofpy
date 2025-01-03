import os
import subprocess
from utilz import adddescription, addspacer, addline

"""
Random Python Notes
"""
#--------------------------------------------------------------------------------------------------
def printNotes():
    adddescription("Call a startup script:")
    os.system('python3 startup.py')
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Read file and print the contents of this script:")
    thisFile = str(__file__)

    file = None

    try:
        file = open(thisFile)

        for f in file:
            print(str(f))

    except FileNotFoundError:
        print("%s %s" % (thisFile, "does not exist."))
    finally:
        if str(type(file)) == "<class '_io.TextIOWrapper'>":
            file.close()
            print("<<FILE SUCCESSFULLY CLOSED>>")

    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Multiply with string prints n times")
    print("%s" % ("he" * 10))
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Run shell commands")
    print(subprocess.run(["ls", "-larit"], capture_output=True, text=True).stdout)
    print(subprocess.run(["python3", "greeting.py"], capture_output=True, text=True).stdout)
    addline()

# -Main -------------------------------------------------------------------------------------------
printNotes()

