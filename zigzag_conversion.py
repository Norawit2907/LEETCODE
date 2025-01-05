class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction = "down"
        counter = 0
        ans = []
        if numRows == 1:
            # print(s)
            return s
# preping ans
        for i in range(numRows):
            ans.append([])

# insert each letter to each row
        for i, s in enumerate(s):
            if direction == "down":
                ans[counter].append(s)
                if counter == numRows - 1:
                    direction = "up"
                    counter -= 1
                else:
                    counter += 1

            elif direction == "up":
                ans[counter].append(s)
                if counter == 0:
                    direction = "down"
                    counter += 1
                else:
                    counter -= 1
            print(ans)


# assembling ans
        ansstr = ""
        for row in ans:
            for s in row:
                ansstr += s
        print(ansstr)
        return ansstr

sol = Solution()
str_inp = input("enter str : ")
numrow_inp = int(input("enter numrows : "))
sol.convert(str_inp, numrow_inp)