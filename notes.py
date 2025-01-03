import os
import subprocess
from utilz import adddescription, addline

"""
Random Python Notes
"""
#--------------------------------------------------------------------------------------------------
def printnotes():
    """Main method of execution"""
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
    adddescription("Multiply with string prints n times:")
    print("%s" % ("he" * 10))
    print("%s" % ("ho " * 10))
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Run shell commands with subprocess:")
    print(subprocess.run(["ls", "-larit"], capture_output=True, text=True).stdout)
    print(subprocess.run(["python3", "greeting.py"], capture_output=True, text=True).stdout)
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with string printf stype formatting:")
    a = 44.000
    b = 45.001
    price = a + b
    print('''%.2f %s %.2f %s %.2f''' % (a, "plus", b, "equals", price))
    print('''%.3f %s %.3f %s %.3f''' % (a, "plus", b, "equals", price))
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with string fstring stype formatting:")
    c = "Welcome"
    d = "Home"
    print(f"Welcome {d}")
    print(f"{c} Home")
    print(f"1 + 1 = {1+1}")
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with classes:")
    class Vehicle:
        def __init__(self, color, make, model, year):
            self.color = color
            self.make = make
            self.model = model
            self.year = year

        def __str__(self):
            return "{" + f"color: {self.color}, make: {self.make}, model: {self.model}, year: {self.year}" + "}"

        def getcolor(self):
            return self.color

    class Automobile(Vehicle):
        @classmethod
        def rundiagnostics(cls):
            print("Running diagnostics...Complete.")

    class Truck(Automobile):
        pass

    class Bicycle(Vehicle):
        pass

    vehicle = Vehicle("Green", "Model", "A", "1800")
    automobile = Automobile("Red", "Model", "B", "1801")
    truck = Truck("Black", "Pickup", "T", "1800")
    bicycle = Bicycle("Tan", "Shwinn", "T", "1800")

    print("Vehicle: %s" % vehicle)
    print("Vehicle: %s" % vehicle.getcolor())
    print("Vehicle: %s" % vehicle.year)
    print("Vehicle: %s" % vehicle.make)
    print("Vehicle: %s" % vehicle.model)
    print("Vehicle: %s" % vehicle.color)
    addline()
    print("Automobile: %s" % automobile)
    print("Automobile: %s" % automobile.getcolor())
    print("Automobile: %s" % automobile.year)
    print("Automobile: %s" % automobile.make)
    print("Automobile: %s" % automobile.model)
    print("Automobile: %s" % automobile.year)
    print("Automobile:", Automobile.rundiagnostics())
    addline()
    print("Truck: %s" % truck)
    print("Truck: %s" % truck.getcolor())
    print("Truck: %s" % truck.year)
    print("Truck: %s" % truck.make)
    print("Truck: %s" % truck.model)
    print("Truck: %s" % truck.color)
    addline()
    print("Bicycle: %s" % bicycle)
    print("Bicycle: %s" % bicycle.getcolor())
    print("Bicycle: %s" % bicycle.year)
    print("Bicycle: %s" % bicycle.make)
    print("Bicycle: %s" % bicycle.model)
    print("Bicycle: %s" % bicycle.color)
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with docstring:")
    print(printnotes.__doc__)
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with lists:")
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with dictionaries:")
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with tuples:")
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with sets:")
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with dates:")
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with json:")
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with regex:")
    addline()
    #--------------------------------------------------------------------------------------------------
    adddescription("Working with ranges:")
    addline()

# -Main -------------------------------------------------------------------------------------------
printnotes()

