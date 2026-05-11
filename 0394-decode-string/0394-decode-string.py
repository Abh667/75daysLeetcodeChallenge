class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            elif char == '[':
                # Push current number and string to stack
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0

            elif char == ']':
                # Pop from stack and build decoded string
                prev_string, num = stack.pop()
                current_string = prev_string + current_string * num

            else:
                # Normal character
                current_string += char

        return current_string
        