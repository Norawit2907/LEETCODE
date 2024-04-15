class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = []
        output = 0
        for i in range(len(s)):
            ls.append(s[i])
            for j in range(i+1, len(s)):
                if(s[i] != s[j] and s[j] not in ls):
                    ls.append(s[j])
                    # print(ls)
                else:
                    if len(ls) > output:
                        output = len(ls)
                    # print(ls, "-")
                    ls = []
                    break
            if len(ls) > output:
                output = len(ls)
            ls = []
        return output
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
#abcdabcbb