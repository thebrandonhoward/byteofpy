"""Various functon related notes"""
def mf(val, values=[]):
    """Behavior of mutable default in function"""
    values.append(val + 1)
    print(values)

def divide(left, right):
    """Behavior of calling method using the keywords"""
    print(f"Divide: {left} / {right} = {left / right}")

def sum(*, left, right):
    """Forces the method to be called only by keyword"""
    print(f"Sum: {left} + {right} = {left + right}")

def sum(left, right, *, verbose=False):
    """Forces one method argument to be called only by keyword"""
    if verbose:
        print(f"Sum: {left} + {right} = {left + right}")
    else:
        print("Not verbose. No display.")

def add(left, right, /):
    """Forces the method to be called only by non-keyword"""
    print(f"Sum: {left} + {right} = {left + right}")

def sumall(*args):
    """Sums infinite list of arguments"""
    s = 0

    for i in args:
        s += i

    print(s)

def sumallreq(req, *args):
    """Sums infinite list of arguments"""
    s = 0

    for i in args:
        s += i

    print(f"Required:{req}, Sum: {s}")

def printd(**kwargs):
    """Print keyword arguments dictionary"""
    for k,v in kwargs.items():
        print(f"{k}:{v}")

def displaytree(father, mother, **siblings):
    """Print keyword arguments dictionary with required args"""
    print(father)
    print(mother)
    for k,v in siblings.items():
        print(f"{k}:{v}", end=" ")
