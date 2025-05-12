# include <iostream>
using namespace std;

int checking_inputs() {
    int year;
    cout <<"Enter Year: ";
    cin >> year;
    int based_on_year = 2018;
    
    while(year > based_on_year) {
        cout << "Year must be 2018 or earlier." << endl;
        cout <<"Enter Year: ";
        cin >> year;
    } 
    cout << "Year entered: " << year << endl;
    return 0;
}

int main() {
    checking_inputs();
    return 0;
}