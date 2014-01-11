#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int fibo(int n)
{
	if (n == 1 || n == 2)
	{
		return 1;
	}
	return fibo(n-1) + fibo(n-2);
}

int main()
{
	std::cout << "hello\n";

	ifstream ifs("in.txt");
	string line;
	getline(ifs, line);
	cout << line;

	int n = 15;
	std::cout << fibo(n);

	getchar();
	return 0;
}