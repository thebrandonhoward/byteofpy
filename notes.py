"""Random Python Notes"""
import os
import subprocess

from utilz import adddescription, addline

#--------------------------------------------------------------------------------------------------
def printnotes():
    """Main method of execution"""
    adddescription("Call a startup script:")
    os.system('python3 startup.py')
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Read file and print the contents of this script:")
    this_file = str(__file__)

    file = None

    try:
        with open(this_file, encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError:
        print(f"{this_file} does not exist.")
    finally:
        if str(type(file)) == "<class '_io.TextIOWrapper'>":
            file.close()
            print("<<FILE SUCCESSFULLY CLOSED>>")

    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Multiply with string prints n times:")
    print("he" * 10)
    print("ho " * 10)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Run shell commands with subprocess:")
    print(subprocess.run(["ls", "-larit"], capture_output=True, text=True, check=False).stdout)
    print(subprocess.run(["python3", "greeting.py"], capture_output=True, text=True, check=False).stdout)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with string printf stype formatting:")
    a = 44.000
    b = 45.001
    price = a + b
    print('''%.2f %s %.2f %s %.2f''' % (a, "plus", b, "equals", price))
    print('''%.3f %s %.3f %s %.3f''' % (a, "plus", b, "equals", price))
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with string fstring stype formatting:")
    c = "Welcome"
    d = "Home"
    print(f"Welcome {d}")
    print(f"{c} Home")
    print(f"1 + 1 = {1+1}")
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with classes:")
    class Vehicle:
        """Parent Vehicle Class"""
        def __init__(self, color, make, model, year):
            self.color = color
            self.make = make
            self.model = model
            self.year = year

        def __str__(self):
            return "{" + f"color: {self.color}, make: {self.make}, model: {self.model}, year: {self.year}" + "}"

        def getcolor(self):
            """Gets vehicle color"""
            return self.color

    class Automobile(Vehicle):
        """Child type of vehicle class"""
        @classmethod
        def rundiagnostics(cls):
            """Statically does a diagnostic check on automobile"""
            print("Running diagnostics...Complete.")

    class Truck(Automobile):
        """Automobile type class"""
        pass

    class Bicycle(Vehicle):
        """Vehicle type class"""
        def __str__(self):
            return str(self.__dict__)

    vehicle = Vehicle("Green", "Model", "A", "1800")
    automobile = Automobile("Red", "Model", "B", "1801")
    truck = Truck("Black", "Pickup", "T", "1800")
    bicycle = Bicycle("Tan", "Shwinn", "T", "1800")

    print(f"Vehicle: {vehicle}")
    print(f"Vehicle: {vehicle.getcolor()}")
    print(f"Vehicle: {vehicle.year}")
    print(f"Vehicle: {vehicle.make}")
    print(f"Vehicle: {vehicle.model}")
    print(f"Vehicle: {vehicle.color}")
    addline()
    print(f"Automobile: {automobile}")
    print(f"Automobile: {automobile.getcolor()}")
    print(f"Automobile: {automobile.year}")
    print(f"Automobile: {automobile.make}")
    print(f"Automobile: {automobile.model}")
    print(f"Automobile: {automobile.year}")
    print(f"Automobile: {Automobile.rundiagnostics()}")
    addline()
    print(f"Truck: {truck}")
    print(f"Truck: {truck.getcolor()}")
    print(f"Truck: {truck.year}")
    print(f"Truck: {truck.make}")
    print(f"Truck: {truck.model}")
    print(f"Truck: {truck.color}")
    addline()
    print(f"Bicycle: {bicycle}")
    print(f"Bicycle: {bicycle.getcolor()}")
    print(f"Bicycle: {bicycle.year}")
    print(f"Bicycle: {bicycle.make}")
    print(f"Bicycle: {bicycle.model}")
    print(f"Bicycle: {bicycle.color}")
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with docstring:")
    print(printnotes.__doc__)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with lists:")
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with dictionaries:")
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with tuples:")
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with sets:")
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with dates:")
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with json:")
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with regex:")
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with ranges:")
    addline()

# -Main -------------------------------------------------------------------------------------------
printnotes()
