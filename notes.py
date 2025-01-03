from pprint import pprint
import subprocess
import sys

"""
Random Python Notes
"""

prompt = input("Clear terminal before starting? ")
#--------------------------------------------------------------------------------------------------
lineLength = 95
#--------------------------------------------------------------------------------------------------
def adddescription(text):
    addspacer()
    print("| %s %s |" % (text, (" " * (lineLength - len(text)))))
    addspacer()

def addspacer():
    print(" --------------------------------------------------------------------------------------------------")

#--------------------------------------------------------------------------------------------------
adddescription("Handle user input")
if str(prompt).lower() == "y" or str(prompt).lower() == "yes":
    print(subprocess.run(["clear"], capture_output=True, text=True).stdout)
#--------------------------------------------------------------------------------------------------
adddescription("Print some python version details")
print(sys.version)
pprint(sys.version_info)
print(sys.platform)
print(sys.argv)
#--------------------------------------------------------------------------------------------------
adddescription("Print everything stored in globals to this point")
pprint(globals())
#--------------------------------------------------------------------------------------------------
adddescription("Read file and print the contents of this script")
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
#--------------------------------------------------------------------------------------------------
adddescription("Multiply with string prints n times")
print("%s" % ("he" * 10))
#--------------------------------------------------------------------------------------------------
adddescription("Run shell commands")
print(subprocess.run(["ls", "-larit"], capture_output=True, text=True).stdout)
print(subprocess.run(["python3", "hello.py"], capture_output=True, text=True).stdout)
#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
