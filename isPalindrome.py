class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        xs = str(x)
        if xs == xs[::-1]:
            return True
        else:
            return False
