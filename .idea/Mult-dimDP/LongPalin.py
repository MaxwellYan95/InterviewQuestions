class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s;
        elif s[0] == s[len(s)-1]:
            result = longestPalindrome(s[1:len(s)-1]);
            if result == s[1:len(s)-1]:
                return s;
            else:
                return result;
        else:
            right = self.longestPalindrome(s[:len(s)-1]);
            left = self.longestPalindrome(s[1:]);
            if len(right) > len(left):
                return right;
            else:
                return left;

sol = Solution();
print(sol.longestPalindrome("cbbd"));
