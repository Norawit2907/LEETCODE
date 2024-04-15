class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1):
            return 1
        if(n == 2): 
            return 2
        onestep = 1
        twostep = 2
        totalstep = 0
        for i in range(3,n+1):
            totalstep = onestep + twostep
            onestep = twostep
            twostep = totalstep
        return totalstep
            

sol = Solution()

print(sol.climbStairs(5))