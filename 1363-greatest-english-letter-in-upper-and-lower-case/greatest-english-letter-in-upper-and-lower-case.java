class Solution {
    public String greatestLetter(String s) {
        boolean[] upper = new boolean[26];
        boolean[] lower = new boolean[26];

        for (char c : s.toCharArray()) {
            if (c >= 'A' && c <= 'Z') {
                upper[c - 'A'] = true;
            } else if (c >= 'a' && c <= 'z') {
                lower[c - 'a'] = true;
            }
        }

        // Check backwards from 'Z' to 'A' to return the greatest letter
        for (int i = 25; i >= 0; i--) {
            if (upper[i] && lower[i]) {
                return String.valueOf((char) ('A' + i));
            }
        }

        return "";
    }
}