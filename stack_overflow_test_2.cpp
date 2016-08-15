#include <iostream>

int foo(unsigned x);
int bar(unsigned x);

unsigned baz()
{
	return 0xa3;
}

int bar(unsigned x)
{
	unsigned u = 0xa5;
	unsigned* pu = &u;
	for(unsigned i = 0; i < 30; i++)
		std::cout << i << " " << std::hex << *(pu + i) << std::dec << std::endl;
	*(pu + 20) = 0xb1;
	for(unsigned i = 0; i < 30; i++)
		std::cout << i << " " << std::hex << *(pu + i) << std::dec << std::endl;
	return 0;
}

int foo(unsigned x)
{
	unsigned u = baz();
	bar(0xa4);
	std::cout << std::hex << u << std::dec << std::endl;
	return 0;
}

int main()
{
	unsigned a = 0xa1;
	foo(0xa2);
	return 0;
}
