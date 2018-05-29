import ctypes
from ctypes import cdll
lib = cdll.LoadLibrary('./codelib.so')

#-----By default int is assumed as type -> needs to be changed for double functions-----
lib.return_ten.restype = ctypes.c_double
lib.sqrt.restype = ctypes.c_double

print(lib.square(4))
print(lib.return_ten(5))

#-----sqrt expects a double -> use ctypes.c_double()-----
print(lib.sqrt(ctypes.c_double(5)))


#-----Use the C++ Class like a Python class-----
class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)


f = Foo()
f.bar()
