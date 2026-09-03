class Solution {
    public boolean isThree(int n) {
        int root = (int) Math.round(Math.sqrt(n));
        
        // n must be a perfect square greater than 1
        if (root * root != n || root < 2) {
            return false;
        }

        // Check if root is prime
        for (int i = 2; i * i <= root; i++) {
            if (root % i == 0) {
                return false;
            }
        }

        return true;
    }
}