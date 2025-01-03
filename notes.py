import os
import subprocess
import utilz

"""
Random Python Notes
"""
#--------------------------------------------------------------------------------------------------
utilz.adddescription("Call a startup script:")
os.system('python3 startup.py')
#--------------------------------------------------------------------------------------------------
utilz.adddescription("Read file and print the contents of this script:")
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
utilz.adddescription("Multiply with string prints n times")
print("%s" % ("he" * 10))
#--------------------------------------------------------------------------------------------------
utilz.adddescription("Run shell commands")
print(subprocess.run(["ls", "-larit"], capture_output=True, text=True).stdout)
print(subprocess.run(["python3", "greeting.py"], capture_output=True, text=True).stdout)
#--------------------------------------------------------------------------------------------------