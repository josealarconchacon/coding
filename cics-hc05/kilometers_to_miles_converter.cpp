

#include <iostream>
using namespace std;

int kilometers_to_miles_converter() {
    double kilometers;
    cout << "Enter number of kilometers: ";
    cin >> kilometers;

    // use formula
    const double mile = 0.621371;
    // Convert kilometers to miles
    double miles = kilometers * mile;
    cout << kilometers << " kilometers is equal to " << miles << " miles." << endl;

    return 0;
}

int main() {
    kilometers_to_miles_converter();
    return 0;
}