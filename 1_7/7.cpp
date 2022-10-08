// Написать программу, которая выводит таблицу значений функции y=-2 * x^2 - 5 * x - 8 в диапазоне от –4 до +4, с шагом 0,5
#include <iostream>
#include <string>

int main()
{
    float x=-4;
    float y;
    while (x<4.5){
        y = -2*x*x-5*x-8;
        std::cout << "x = " << x << ", y = " << y << std::endl;
        x += 0.5;
        }
}