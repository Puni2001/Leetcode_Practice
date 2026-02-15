class Solution {
    public int longestConsecutive(int[] nums) {
        int longest = 0;
        Set<Integer> set = new HashSet<>();
        for (int num:nums){
            set.add(num);
        }

        for (int num: set){
            if (!set.contains(num - 1)){
                int curr = num;
                int streak = 1;

                while(set.contains(curr+1)){
                    curr += 1;
                    streak += 1;
                }
                longest = Math.max(longest, streak);
            }
        }
        return longest;
    }
}
