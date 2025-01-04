"""Various utility functions"""
#--------------------------------------------------------------------------------------------------
LINE_LENGTH = 83

#--------------------------------------------------------------------------------------------------
def adddescription(text):
    """Formats a description header"""
    addspacer()
    print(f"| {text}" + (" " * (LINE_LENGTH - len(text))) + " |")
    addspacer()

def addspacer():
    """Adds a spacer line"""
    print(" -------------------------------------------------------------------------------------")

def addline():
    """Adds a blank line"""
    print('')
