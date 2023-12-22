
'''https://leetcode.com/problems/palindrome-number/'''


class Solution(object):
    def isPalindrome(self, x):
        a= str(abs(x))[::-1]
        a=int(a)
        if x == a:
            return True
        else:
            return False
        
        
        
# class Solution(object):
#     def isPalindrome(self, x):
#         x = str(x)
#         return x == x[::-1]
# sol = Solution()
# print(sol.isPalindrome(121))
