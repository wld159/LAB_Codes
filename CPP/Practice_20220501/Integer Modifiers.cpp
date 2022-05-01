#include <iostream>

using namespace std;

int main(){
    
    signed int value1 {10};
    signed int value2 {-300};

    cout << "value1 : " << value1 << endl;
    cout << "value2 : " << value2 << endl;
    cout << "sizeof(value1) : " << sizeof(value1) << endl;
    cout << "sizeof(value2) : " << sizeof(value2) << endl;

    unsigned int value3 {4};
    // unsigned int value4 {-5}; // Compile error

    return 0;

}