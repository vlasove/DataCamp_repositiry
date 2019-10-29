#include <iostream> 
#include <string>
#include <algorithm>
#include <locale>
using namespace std; 

void string_tolower(string &s, const locale &loc)
{
    for (string::iterator i=s.begin(), j=s.end(); i!=j; ++i)
        *i = tolower(*i, loc);
}


string Clear(string s){
    
    for (int i = 0, len = s.size(); i < len; i++) 
    { 
        
        // check whether parsing character is punctuation or not 
        if (ispunct(s[i]) || isspace(s[i])) 
        { 
            s.erase(i--, 1); 
            len = s.size(); 
        } 
    }

    
    return s;

}


  
int main()  
{ 
    string lines;
    getline(cin, lines);
    
    string_tolower(lines, locale("rus_rus.866"));
    cout<<lines<<endl;
    //cout<<Clear(lines)<<endl;
    return 0; 
} 