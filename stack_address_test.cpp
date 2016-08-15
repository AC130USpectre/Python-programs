#include <iostream>

#if TEST == 1
void bar()
{
	int i;
	std::cout << i << std::endl;
	return;
}

void foo()
{
	int i = 3;
	std::cout << i << std::endl;
	return;
}
#endif

#if TEST == 2
void bar()
{
	int i;
	std::cout << &i << std::endl;
	return;
}

void foo()
{
	int i = 3;
	std::cout << &i << std::endl;
	return;
}
#endif

#if TEST == 3
void bar()
{
	int i;
	std::cout << i << " " << &i << std::endl;
	return;
}

void foo()
{
	int i = 3;
	std::cout << i << " " << &i << std::endl;
	return;
}
#endif


int main()
{
	foo();
	bar();
	return 0;
}
