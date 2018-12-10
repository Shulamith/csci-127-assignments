#include <iostream>

int add2(int a, int b){
	int c;
	c = a+b;
	return c;
}
int main(){
	std::cout << add2(3,5) << "\n";
	std::string s = "hello";

	for (int i=0; i < s.length(); i++){
		std::cout<< s[i] << "_";
	}
	std:: string words;
	getline(std::cin,words);
	std::cout << words;
}