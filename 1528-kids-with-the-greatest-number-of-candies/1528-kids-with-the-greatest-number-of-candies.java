import java.util.*;
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max=0,n;
        for(int i:candies){
            if (max<i) max=i;
        }
        n=candies.length;
        ArrayList<Boolean> result=new ArrayList<Boolean>();
        for (int i=0;i<n;i++){
            if ((candies[i]+extraCandies)>=max) result.add(true);
            else result.add(false);
        }
        return result;
        
    }
}