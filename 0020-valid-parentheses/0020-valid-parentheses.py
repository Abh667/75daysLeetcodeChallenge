class Solution(object):
    def isValid(self, s):
        
        stack = []

        # mapping of closing to opening brackets
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            # if opening bracket, push to stack
            if char in mapping.values():
                stack.append(char)
            else:
                # if stack is empty OR top doesn't match
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        # valid only if stack is empty
        return len(stack) == 0
        