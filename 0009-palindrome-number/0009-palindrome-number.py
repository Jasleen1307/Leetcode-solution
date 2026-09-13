
class Solution(object):
    def isPalindrome(self, x):
        original = x
        reverse = 0

        if x < 0:
            return False

        elif x % 10 == 0 and x != 0:
            return False

        else:
            while x != 0:
                digit = x % 10
                reverse = reverse * 10 + digit
                x = x // 10

            if original == reverse:
                return True
            else:
                return False

