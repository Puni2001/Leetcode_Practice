class Solution {
    public long minNumberOfSeconds(int h, int[] wt) {
        long l = 1, r = 0;

        for (int w : wt) {
            r = Math.max(r, (long) w * h * (h + 1) / 2);
        }

        while (l < r) {
            long m = l + (r - l) / 2;

            if (ok(m, h, wt)) {
                r = m;
            } else {
                l = m + 1;
            }
        }

        return l;
    }

    private boolean ok(long t, int h, int[] wt) {
        long sum = 0;

        for (int w : wt) {
            long x = (long) ((Math.sqrt(1 + 8.0 * t / w) - 1) / 2);
            sum += x;

            if (sum >= h) return true;
        }

        return false;
    }
}