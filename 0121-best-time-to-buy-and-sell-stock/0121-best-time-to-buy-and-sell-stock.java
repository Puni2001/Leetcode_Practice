class Solution {
    public int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE;
        int max = 0;
        for (int p:prices){
            if (p < min){
                min = p; 
            } else {
                int profit = p - min;
                max = Math.max(profit, max);
            }
        }
        return max;
    }
}