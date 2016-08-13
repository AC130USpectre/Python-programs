#include <iostream>

void bar()
{
    int a;
    std::cout << a << std::endl;
    return;
}

void foo()
{
    int a = 3;
    std::cout << a << std::endl;
    return;
}

int main()
{
    foo();
    bar();
    return 0;
}
