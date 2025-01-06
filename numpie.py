"""Using numpy to work with arrays"""
import numpy as np
from utilz import adddescription, addline

def startnumpy():
    adddescription("Working with numpy:")
    print(f"numpy version: {np.__version__}")
    np_array = np.array([1, 2, 3, 4, 5])
    addline()
    print(np_array)
    print(type(np_array))
    addline()

    tuple4nparray = (5, 4, 3, 2, 1, 1)
    nptuple = np.array(tuple4nparray)
    print(nptuple)
    print(type(nptuple))
    addline()

    twod_np_array = np.array([[1,3,5],[2,4,6]])
    print(twod_np_array)
    print(f"dimensions: {twod_np_array.ndim}")
    addline()

    threed_np_array = np.array([[[2,4,6],[1,3,5]]])
    print(threed_np_array)
    print(f"dimensions: {threed_np_array.ndim}")
    threed_np_array = np.array([1,2,3,4,5,6,], ndmin=3)
    print(threed_np_array)
    print(f"dimensions: {threed_np_array}")
    print(threed_np_array[0][0][0])
    print(threed_np_array[0][0][1])
    # ----------------------------------------------------------------------------------------------
    addline()
    # ----------------------------------------------------------------------------------------------
