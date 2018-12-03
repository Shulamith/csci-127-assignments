#include <iostream>
int main()
{
	int i, guess,response;
	/* code */
	std::cout << "Type an integer between 0 and 99 inclusive" << "\n";
	std::cin << i;


	
	while (response != 0) {
		int response, guess;
		guess = 0;
		std::cout << "Did you pick" << guess << "? If yes type 0 if the number is higher type 1, if the number is lower type -1" << "\n";
		std::cin << response;
		guess = guess + response;
	

}
	std::cout << "End of the game";

	return 0;
}