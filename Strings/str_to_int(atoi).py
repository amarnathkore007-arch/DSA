class Solution:
    def myAtoi(self, s):

        i = 0
        n = len(s)

        # Step 1: Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Step 2: Check sign
        sign = 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        # Step 3: Read digits
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # Apply sign
        num = num * sign

        # Step 4: Clamp to 32-bit integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN

        if num > INT_MAX:
            return INT_MAX

        return num


obj = Solution()

s = "   -042"

result = obj.myAtoi(s)
print(result)