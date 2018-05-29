######Compile the foo2.cpp into a library#####

g++ -c -fPIC code.cpp -o code.o
g++ -shared -Wl,-soname,codelib.so -o codelib.so  code.o

#####StartUp Python#####
python Py_Cpp.py
