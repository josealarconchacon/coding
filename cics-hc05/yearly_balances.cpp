// Name: Jose Alarcon Chacon
// Email: jose.alarconchacon76@login.cuny.edu
// Date: May 12, 2025
// Display year balance with 3 percent until it reaches 1000


#include <iostream>
using namespace std;

int checking_input() {
    double starting_amount;
    cout << "Please, enter the starting amount: ";
    cin >> starting_amount;

    double interest_rate = 0.03;
    double balance = starting_amount;
    int amount_has_increased_more_than = 1000;
    int years = 0;

    while (balance - starting_amount <= amount_has_increased_more_than) {
        years++;
        balance = balance  * (1 + interest_rate);
        cout << "The balance is: " << balance << endl;
    }
    
    return 0;
}

int main() {
    checking_input();
    return 0;
}