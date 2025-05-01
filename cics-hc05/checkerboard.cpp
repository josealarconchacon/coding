 

#include <iostream>
using namespace std;
int checkerboard() {
    // define variables
    int i, j, size; 
    // prompt user for input of the checkerboard size
    cout << "Enter the number for the checkerboard: "; 
    cin >> size;

    // loop through the rows
    for (i = 0; i < size; i++) {
        // loop through the columns
        for (j = 0; j < size; j++) {
            // sum  row and column and if even, "#", else "*"
            if ((i + j) % 2 == 0) {
                cout << "#"; 
            } else {
                cout << "*";
            }
        }
        cout << endl;
    }
    return 0;
}

int main() {
    checkerboard();
    return 0;
}