class Solution:
    def isPalindrome(self, s: str, b: int, f: int) -> bool:
        if(b == f):
            return True
        if(s[b] != s[f]):
            return False
        if b > f + 1:
            return self.isPalindrome(s. b+1, f-1)

        return True

inputstr = input()
s = Solution()
print(s.isPalindrome(inputstr, 0, len(inputstr)-1))


        
    