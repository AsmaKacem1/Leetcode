class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string res;
        int l=s.length();
        char ind[l];
        for(int i=0;i<l;i++){
            ind[indices[i]]=s[i];
        }
        
        for(int i=0;i<l;i++){
            res+=ind[i];
        }
        
        return res;
    }
};