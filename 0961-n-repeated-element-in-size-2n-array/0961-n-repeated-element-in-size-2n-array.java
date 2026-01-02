class Solution {
    public int repeatedNTimes(int[] nums) {
        int n = nums.length/2;
        Map<Integer, Integer> count = new HashMap<>();
        for (int num:nums){ 
            count.put(num, count.getOrDefault(num,0)+1);
        }
        for(Map.Entry<Integer, Integer> entry : count.entrySet()){
            
            if ( entry.getValue()  == n) return entry.getKey();
        }
        return -1;
}
}