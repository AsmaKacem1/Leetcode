class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int result=0;
        for (string item:operations){
            if (item[1]=='+') result++;
            else result--;
            };
        return result;
    };
    
};