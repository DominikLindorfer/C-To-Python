# C-to-Python Template

This simplistic template uses Python's *ctypes* to import functions and classes from C++ code directly into the Python code.
The latter is achieved by compiling the C++ file as a library which is then imported into Python.

## Usage & Compilation on Linux:

To execute the current code execute
```
./MakeFile.sh
´´´

or compile from source by 

```
g++ -c -fPIC code.cpp -o code.o
g++ -shared -Wl,-soname,codelib.so -o codelib.so code.o
´´´

and then executing the Python file.


**Any Questions or Bug Reports?** Send me an e-Mail: dominik.lindorfer@jku.at
