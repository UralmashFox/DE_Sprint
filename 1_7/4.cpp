#include <iostream>
#include <string>

int main()
{
  int a;
  std::cout <<"Enter number "<< std::endl ;
  std::cin >> a;
  if(std::cin.fail()) {
      std::cout << "Invalid value. Please, paste int only"<< std::endl;
      return 0;
  }
  if (a % 2 == 0) {
        std::cout << "Number is even" << std::endl;
    }
  else {
      std::cout << "Number is odd" << std::endl;
  }
    return 0;
}