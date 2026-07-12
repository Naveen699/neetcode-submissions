class Solution:
    def isValid(self, s: str) -> bool:
        
        matches = {")" : "(", "}" : "{", "]" : "["}

        stack = []

        for char in s: 
            if char in matches:
                if stack and matches[char] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)

        return True if not stack else False