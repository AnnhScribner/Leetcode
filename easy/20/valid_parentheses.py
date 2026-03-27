class Solution:
    def isValid(self, s: str) -> bool:
        stack_temp = []

        close_to_open = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for char in s:
            if char in close_to_open: # if character is in dict keys, it is a close one
                # if stack not empty AND the peek character is equals to the character value in dict
                if stack_temp and close_to_open[char] == stack_temp[-1]: # stack_temp[-1] -> peek
                    stack_temp.pop()
                else:
                    return False
            else:
                stack_temp.append(char) # appending open character
        # if stack is empty, so all closers found their openers
        return not stack_temp

s = Solution()
print(s.isValid("()")) # true
print(s.isValid("()[]{}")) # true
print(s.isValid("(]")) # false
print(s.isValid("([])")) # true
print(s.isValid("([)]")) # false
print(s.isValid("[")) # false
print(s.isValid("((")) # false
print(s.isValid("))")) # false