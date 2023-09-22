class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        int n1=nums1.length,n2=nums2.length;
        HashSet<Integer> set1=new HashSet<Integer>();
        HashSet<Integer> set2=new HashSet<Integer>();
        ArrayList<Integer> arr1=new ArrayList<Integer>();
        ArrayList<Integer> arr2=new ArrayList<Integer>();
        for (int i:nums1) set1.add(i);
        for (int i:nums2) set2.add(i);
        for (int i:set1) if (!set2.contains(i)) arr1.add(i);
        for (int i:set2) if (!set1.contains(i)) arr2.add(i);
        ArrayList<List<Integer>> result=new ArrayList<List<Integer>>();
        result.add(arr1);
        result.add(arr2);
        return result;
      
        
    }
}