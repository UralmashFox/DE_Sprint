// Написать программу, которая определяет максимальное число
#include <iostream>
#include <string>

int main()
{
  int max_val = -1;
  int arr_size;
  std::cout << "what is lenth of array?" << std::endl;
  std::cin >> arr_size;
  int arr[arr_size];
  for (int i=0; i<arr_size; i++){
      std::cout << "enter the number" << std::endl;
      std::cin >> arr[i];
  }
  int i = 0;
  do{
      if (arr[i]>max_val){
          max_val = arr[i];
          }
      i++;
      }while (i<arr_size);
  std::cout << "the max value is " << max_val;
}