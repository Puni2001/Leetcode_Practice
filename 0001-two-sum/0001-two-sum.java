class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i=0; i<nums.length; i++){
            int cmpl = target - nums[i];
            if (seen.containsKey(cmpl)){
                return new int[] {seen.get(cmpl),i};
            }
            seen.put(nums[i],i);
        }
        return new int[] {};
       
    }
}