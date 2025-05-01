
#include <iostream>
using namespace std;
int seasonal_greetings() {
    int month_of_year;
    cout << "Enter the month of the year (1-12): ";
    cin >> month_of_year;

    // "Happy Winter" if it is strictly before 3 or strictly larger than 11
    if (month_of_year < 3 || month_of_year > 11) {
        cout << "Happy Winter" << endl;
    // "Happy Spring" if it is 3 or greater, but strictly before 7, and
    } else if (month_of_year >= 3 && month_of_year < 7) { 
        cout << "Happy Spring" << endl;
    // "Happy Summer" if it is 7 or greater, but strictly before 9, and
    } else if (month_of_year >= 7 && month_of_year < 9) {
        cout << "Happy Summer" << endl;
    // "Happy Fall" otherwise.
    } else {
        cout << "Happy Fall" << endl;
    }
    return 0;
}

int main() {
    seasonal_greetings();
    return 0;
}