class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        res = 0

        s = s.lstrip()

        i = 0
        if i < len(s) and s[i] in ('-', '+'):
            if s[i] == '-':
                negative = True
            i += 1

        while i < len(s) and s[i].isnumeric():
            res *= 10
            res += int(s[i])
            i += 1

        if negative:
            res *= -1

        return max(min(INT_MAX, res), INT_MIN)