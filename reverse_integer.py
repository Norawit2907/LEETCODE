class Solution:
    def reverse(self, x: int) -> int:
        negative = "no"
        if x < 0:
            x *= -1
            negative = "yes"

        x = str(x)
        check = x

        reversed_x = ""
        for s in x:
            reversed_x = s + reversed_x
        # print(reversed_x)

        reversed_x = (int(reversed_x))
    
        if(negative == "yes"):
            reversed_x *= -1
        if -2147483648 <= reversed_x and reversed_x <= 2147483648 - 1:
            # print(reversed_x)
            return reversed_x
        else:
            # print(0)
            return 0
        
         
sol = Solution()
intinp = int(input("enter number : "))
sol.reverse(intinp)