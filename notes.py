"""Random Python Notes"""
import os
import functions as snippets
import subprocess
from numpie import startnumpy

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
    adddescription("Working with string slicing:")
    slc = "HELLO WORLD"
    print(f"{slc} [3:7] = {slc[3:7]}")
    print(f"{slc} [-8:-2] = {slc[-8:-2]}")
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Multiply with string prints n times:")
    print("he" * 10)
    print("ho " * 10)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Run shell commands with subprocess:")
    cmds = ["ls", "-larit"]
    print(subprocess.run(cmds, capture_output=True, text=True, check=False).stdout)
    cmds = ["python3", "greeting.py"]
    print(subprocess.run(cmds, capture_output=True, text=True, check=False).stdout)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with string printf stype formatting:")
    a = 44.000
    b = 45.001
    print("""%.2f %s %.2f %s %.2f""" % (a, "plus", b, "equals", a+b))
    print("""%.3f %s %.3f %s %.3f""" % (a, "plus", b, "equals", a+b))
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with string fstring stype formatting:")
    c = "Welcome"
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
            return str(self.__dict__)

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
    adddescription("Working with mutable functions:")
    snippets.mf(0)
    snippets.mf(1)
    snippets.mf(2)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with keyword calling functions(*,):")
    snippets.divide(left=1, right=7)
    snippets.divide(right=7, left=1)
    addline()
    snippets.divide(1, 7)
    snippets.divide(7, 1)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with keyword only functions(*,):")
    snippets.sum(left=1, right=7, verbose=True)
    snippets.sum(right=7, left=1, verbose=False)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with non-keyword calling functions(/):")
    snippets.add(1, 7)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with unlimited args calling functions(*):")
    snippets.sumall(10, 20, 30, 40)
    snippets.sumall(10, 10, 30)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with unlimited and required args calling functions(*):")
    snippets.sumallreq("Test2", 10, 20, 30, 40)
    snippets.sumallreq("Test1", 10, 10, 70)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with unlimited dictionary args calling functions(**):")
    snippets.printd(city="New Orleans", state="Louisiana", code=504)
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with unlimited dictionary and required args calling functions(**):")
    snippets.displaytree("Jack", "Jill", brother="JJ", sister="jj")
    addline()
    #----------------------------------------------------------------------------------------------
    adddescription("Working with lists:")
    list1 = ["Rohan", "Physics", 21, 69.75]
    list2 = [1, 2, 3, 4, 5]
    list3 = ["a", "b", "c", "d"]
    list4 = [25.50, True, -55, 1+2j]
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    list1.extend(list2)
    print(f"List1 extended: {list1}")
    list4.pop(1)
    print(f"List4 pop[1]: {list4}")
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
    # ----------------------------------------------------------------------------------------------
    adddescription("Working with request module:")
    addline()
    # ----------------------------------------------------------------------------------------------
    adddescription("Working with numpy:")
    addline()
    # ----------------------------------------------------------------------------------------------
    adddescription("Working with pandas:")
    addline()
    # ----------------------------------------------------------------------------------------------
    adddescription("Working with scipy:")
    addline()
    # ----------------------------------------------------------------------------------------------
    adddescription("Working with django:")
    addline()
    # ----------------------------------------------------------------------------------------------
    adddescription("Working with mysql:")
    addline()

# -Main -------------------------------------------------------------------------------------------
printnotes()
startnumpy()
