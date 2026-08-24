class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        cleaned=""
        for c in s:
            if c.isalnum():
                cleaned+=c
        return cleaned[::]==cleaned[::-1]