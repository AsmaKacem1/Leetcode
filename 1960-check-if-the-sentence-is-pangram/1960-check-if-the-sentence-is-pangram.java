class Solution {
    public boolean checkIfPangram(String sentence) {
        HashSet<Character> set=new HashSet<Character>();
        for (char c:sentence.toCharArray()) set.add(c);
        return set.size()==26;

        
    }
}