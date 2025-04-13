class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        a.sort()
        b.sort()
        if a==b:
            return True
        else:
            return False
            
