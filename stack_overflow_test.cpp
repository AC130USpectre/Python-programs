#include <iostream>

void foo()
{
    int* m[1];
    std::cout << "Hello, World!" << std::endl;
    m[2] = m[3];
    return;
}

void bar()
{
    int* m[1];
    m[3] = m[2];
    m[2] = (int*) &foo;
    return;
}

int main()
{
    bar();
    return 0;
}
