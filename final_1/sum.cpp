#include <iostream>

int sumofsquares(int a, int b) {
	int sumsqr;
	int totalSum = 0;
	while (a<=b){
		sumsqr = a*a;
		totalSum = totalSum + sumsqr;
		a++; 
	}
	return totalSum;
}
int main()
{
	std::cout << "Sum of squares 5 through 10:\n" << sumofsquares(5,10)<< "\n";
	std::cout << "Sum of squares 6 through 10:\n" << sumofsquares(6,10)<< "\n";
	std::cout << "Sum of squares 1 through 2:\n" << sumofsquares(1,2)<< "\n";
	std::cout << "Sum of squares 10 through 30:\n" << sumofsquares(10,30)<< "\n";
	std::cout << "Sum of squares 4 through 7:\n" << sumofsquares(4,7)<< "\n";

	/* code */
	return 0;
}