# C-to-Python Template

This simplistic template uses Python's *ctypes* to import functions and classes from C++ code directly into the Python code.
The C++ file is compiled as a library which is then imported into Python.

## Usage & Compilation on Linux:

To compile and execute the current code execute
```
./MakeFile.sh
```
or compile the libraries from source by 
```
g++ -c -fPIC code.cpp -o code.o
g++ -shared -Wl,-soname,codelib.so -o codelib.so code.o
```
and then executing the Python file on your local machine.


**Any Questions or Bug Reports?** Send me an e-Mail: dominik.lindorfer@jku.at
