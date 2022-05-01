#include <iostream>

using namespace std;

int main(){
    int age;
    string name;

    cout << "Please type in your Last name and age, sepearted by spaces : " << endl;

    cin >> name >> age; // Input name and age

    cout << "Hello " << name << "! You are " << age << " years old." << endl;

    return 0;
}