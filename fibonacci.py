# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 1 or n == 0:
#             return n
        
#         return self.fib(n-1) + self.fib(n-2)

# class Solution:
#     def fib(self, n: int) -> int:
#         a = 0
#         b = 1
#         if n == 0:
#             return a
#         if n == 1:
#             return b
#         for i in range(n-1):
#             c = a + b
#             a = b
#             b = c
   
#         return c

class Solution:
    
    ls = {}
    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n

        if n in self.ls:
            return self.ls[n]

        self.ls[n] = self.fib(n-1) + self.fib(n-2)
        return self.ls[n]
sol = Solution()
print(sol.fib(10))