
# include <iostream>
using namespace std;

int two_complement() {
    int x = 32;
    int b = 16;
    int number;

    cout << "Enter a number: ";
    cin >> number;

    if(number < 0) {
        cout <<"1";
        x += number;
    } else {
        cout << "0";
        x = number;
    }

    while (b > 0.5) {
        if (x >= b) {
            cout <<"1";
            x = x % b;
        } else {
            cout <<"0";
        }
        b = b / 2;
    }
    cout << endl;
    return 0;
}

int main() {
    two_complement();
    return 0;
}