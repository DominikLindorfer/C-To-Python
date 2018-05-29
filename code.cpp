#include <iostream>
#include <cmath>

class Foo{
    public:
        void bar(){
            std::cout << "Hello" << std::endl;
        }
};

extern "C" {
    Foo* Foo_new(){ return new Foo(); }
    void Foo_bar(Foo* foo){ foo->bar(); }
}


extern "C" double return_ten(double x)
{
  return 10.0;
}

extern "C" int square(int x)
{
  return x*x;
}

extern "C" {
    double sqrt(double);//C linkage
}
