#include <iostream>

int main(){

    // Compile time error
    std::cout << "Hello World!" << std::endl;
    return 0;

    // Run time error
    int value = 7/0;
    std::cout << "value : " << value << std::endl;
    return 0;

}