class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        map<char,int> mp;
        int res=0;
        for(int i=0;i<jewels.length();i++){
            mp[jewels[i]]++;
        }
        for(int i=0;i<stones.length();i++){
            res+=mp[stones[i]];
        }
        return res;
    }
};