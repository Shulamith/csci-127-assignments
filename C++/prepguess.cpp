#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
int main()
{ int random, guess;
	srand(time(NULL));
  random = rand()%100;

  std::cout << "Guess a number from 0 to 99" << "\n";
  std::cin >> guess;
  while (guess != random){
  	if (guess > random) {
  		std::cout << "Your guess is too high, Guess again";
 }
  	else if (guess < random){
  		std::cout << "Your guess is too low, Guess again";
 }
 	std::cin >> guess;
 	guess = guess;

 }
 	if (guess == random){
 		std::cout << "You got it" << "\n";
 	}

  
	/* code */
	return 0;
}