class Solution {
    public int balancedStringSplit(String s) {
        int ans = 0;
        int diff = 0;

        for (char ch : s.toCharArray()) {
            if (ch == 'L') {
                diff++;
            } else {
                diff--;
            }

            if (diff == 0) {
                ans++;
            }
        }

        return ans;
    }
}