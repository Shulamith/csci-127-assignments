#include <iostream>
int main()
{int i;
int some_variable, another_variable;
double d;
float f;
char c;
c = 'z';
 i =20;
 i= i+ some_variable;
 std::cout << "i = " << i << "\n"; 
 d=d/4.2;
 std::cout << "d= " << d << "\n"; 

 std::cout << c << "\n";

 std::cout <<true << "\n";
 std::cout << (i>100) << "\n";
 std::cout << (i<100) << "\n";
 std::cout << "Please enter a number:";
 std::cin >> i;
 std::cout << "You entered: " << i << "\n";

 if (i>10) {
 	std::cout << "i is greater than 10\n";
 } else {
 	std::cout << "is is lesss or equal\n";
 }
 
 return 0;
 }