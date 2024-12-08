# Solution 1, this solution works but takes too long
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         longest_palindrome = ""
#         if(len(s) == 1):
#             return s
#         for i in range(len(s)-1):
#             for j in range(i, len(s), 1):
#                 substring = s[i:j+1]
#                 # print(i, j, substring)
#                 if self.isPalindrome(substring):
#                     if(len(longest_palindrome) < len(substring)):
#                         longest_palindrome = substring
#         return longest_palindrome    

#     def isPalindrome(self, s: str):
#         if(len(s) == 1):
#             return True
#         for i in range(len(s)-1):
#             if (i == len(s)-1-i and s[i] == s[len(s)-1-i]):
#                 return True
#             elif (len(s)-1-i - i == 1 and s[i] == s[len(s)-1-i]):
#                 return True
#             elif s[i] != s[len(s)-1-i]:
#                 return False

# Solution 2, thanks japanese guy
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        def expandPalindrome(s, left, right):
            while( left >= 0 and right < len(s) and s[left] == s[right] ):
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        end = 0
        
        for i in range(len(s)):
            odd = expandPalindrome(s, i, i)
            even = expandPalindrome(s, i, i+1)
            max_palin = max(odd, even)
            if(max_palin > end - start):
                start = i - (max_palin - 1) // 2
                end = i + (max_palin // 2)
        
        return s[start:end+1]

                    
input = input()
sol = Solution()
print(sol.longestPalindrome(input))