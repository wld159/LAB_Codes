#include <iostream>
#include <stdio.h>

using namespace std;

int main(){

    cout << "Unformatted table : " << endl;
    cout << "Daniel" << " " << "Gray" << "25" << endl;
    cout << "Stanley" << " " << "Woods" <<  "33" << endl;
    cout << "Jordan" << " " << "Parker" << "45" << endl;

    cout << endl;
    
    cout << "Formatted table : " << endl;
    // cout << setw(10) << "Daniel" << setw(10) << "Gray" << "25" << endl;
    cout << "Stanley" << " " << "Woods" <<  "33" << endl;
    cout << "Jordan" << " " << "Parker" << "45" << endl;
}