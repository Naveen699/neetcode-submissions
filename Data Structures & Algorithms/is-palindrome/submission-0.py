class Solution:
    def isPalindrome(self, s: str) -> bool:
        returnString = ""

        for char in s: 
            if char.isalnum():
                returnString += char.lower()
        
        return returnString == returnString[::-1]