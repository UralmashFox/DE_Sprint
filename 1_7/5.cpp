// Написать программу, которая выводит таблицу квадратов десяти первых положительных чисел.
#include <iostream>
#include <string>

int main()
{
  int a[] = {1,2,3,4,5,6,7,8,9,10};
  for (int i = 0; i < 10; i++)
  {
      int sq = a[i]*a[i];
      std::cout << sq << std::endl;
  }
}