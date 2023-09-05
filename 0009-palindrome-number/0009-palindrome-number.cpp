class Solution {
public:
    bool isPalindrome(int x) {
            string str= to_string(x);
            string a=str;
            reverse(str.begin(),str.end());
            return str==a; 
    }    
};