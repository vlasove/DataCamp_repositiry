#include <iostream>
#include <string>

using namespace std;

bool IsPalindrom(string s) {
    for (size_t i = 0; i < s.size() / 2; ++i) {
        if (s[i] != s[s.size() - i - 1]) {
            return false;
        }
    }
    return true;
}

int main(){

    cin.ignore (std::numeric_limits<std::streamsize>::max(),'\n'); //wait for newline
    cin.get();




    return 0;
}