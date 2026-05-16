class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False 
        
        num = x
        rev_sum = 0
        while x:
            digit = x % 10
            rev_sum = rev_sum * 10 + digit
            x = x // 10

        return rev_sum == num