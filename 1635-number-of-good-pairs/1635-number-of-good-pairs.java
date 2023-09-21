class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int result = 0;
        
        for (int i : nums) {
            if (map.containsKey(i)) {
                int x = map.get(i);
                map.put(i, x + 1);
            } else {
                map.put(i, 1);
            }
        }
        
        for (int x : map.values()) {
            result += (x * (x - 1)) / 2;
        }
        
        return result;
    }
}
