#include <iostream>
#include <math.h>
float discriminant(float a, float b, float c){
	float answer = ( b*b -(4*a*c));
	return answer;
}
float quadsolve(float a, float b, float c){
	float disc = discriminant(a,b,c);
	if (disc >= 0){
		float root = ((-b + sqrt(disc)) / (2*a));
		//std::cout << "here" << root << "\n";
		return root;
	}
	 else if (disc < 0){
		//std::cout << "here\n";
		return 0;
	}
}
int main()
{
	std::cout << "Discriminant of 3,5,.5 \n" << discriminant(3,6,.5) << "\n";
	std::cout << "The root of the equation (if disc positive) is \n" << quadsolve(3,6,.5) << "\n";
	std::cout << "\n Disc of 9,4,6 \n"<< discriminant(9,4,6) <<"\nThe root of the equation (if disc positive) is \n" <<quadsolve(9,4,6)<<"\n";
	std::cout << "\n Disc of 1,1,0 \n"<< discriminant(1,1,0) <<"\nThe root of the equation (if disc positive) is \n" <<quadsolve(1,1,0)<<"\n";
	std::cout << "\n Disc of .5,10,3 \n"<< discriminant(.5,10,.3) << "\nThe root of the equation (if disc positive) is \n" <<quadsolve(.5,10,.3)<<"\n";
	std::cout << "\n Disc of 2,8,4 \n"<< discriminant(2,8,4) <<"\nThe root of the equation (if disc positive) is \n" <<quadsolve(2,8,4)<<"\n";
	std::cout << "\n Disc of 2,8,8 \n"<< discriminant(2,8,8) <<"\nThe root of the equation (if disc positive) is \n" <<quadsolve(2,8,8)<<"\n";
	/* code */
	return 0;
}