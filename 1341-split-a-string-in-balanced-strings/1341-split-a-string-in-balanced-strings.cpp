class Solution {
public:
    int balancedStringSplit(string s) {
        int res=0,sum=0;
        for(char x:s){
            if(x=='R') sum++;
            else sum--;
            if(sum==0){
                res++;
                sum=0;
            }
        }
        return res;
    }
};