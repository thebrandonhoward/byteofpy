#--------------------------------------------------------------------------------------------------
lineLength = 95

#--------------------------------------------------------------------------------------------------
def adddescription(text):
    addspacer()
    print("| %s %s |" % (text, (" " * (lineLength - len(text)))))
    addspacer()

def addspacer():
    print(" --------------------------------------------------------------------------------------------------")
