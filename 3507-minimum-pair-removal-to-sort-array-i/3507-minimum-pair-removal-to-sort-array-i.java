class Solution {
    public int minimumPairRemoval(int[] nums) {
        int ops = 0;

        while (!isSorted(nums)) {
            int minSum = Integer.MAX_VALUE;
            int idx = 0;

            // Find leftmost adjacent pair with minimum sum
            for (int i = 0; i < nums.length - 1; i++) {
                int sum = nums[i] + nums[i + 1];
                if (sum < minSum) {
                    minSum = sum;
                    idx = i;
                }
            }

            // Build new array after merging
            int[] next = new int[nums.length - 1];
            int k = 0;

            for (int i = 0; i < nums.length; i++) {
                if (i == idx) {
                    next[k++] = nums[i] + nums[i + 1];
                    i++; // skip merged element
                } else {
                    next[k++] = nums[i];
                }
            }

            nums = next;
            ops++;
        }

        return ops;
    }

    private boolean isSorted(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < nums[i - 1]) return false;
        }
        return true;
    }
}
