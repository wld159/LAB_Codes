#include <iostream>

int main(){

    std::cout << "hi" << std::endl
            << "my name is "
            << "Psi" << std::endl;

    int sum = 0;
    for (int i = 1; i <= 10; i++){
        sum += i;
    }

    std::cout << "합은 : " << sum << std::endl;
    return 0;

}