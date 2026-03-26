class Solution:
    # time: O(n)
    def romanToInt(self, s: str) -> int:

        # create a list of character of the given string
        list_char = list(s)

        # dict -> roman : int
        nums = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0

        # starting the loop from the end to the beginning
        for i in range(len(list_char) - 1, -1, -1):
            # if curr is bigger than previous AND i is bigger than zero (so it doesn't go to the end of the list when i is 0)
            if nums[list_char[i]] > nums[list_char[i - 1]] and i > 0:
                total+= nums[list_char[i]] - nums[list_char[i - 1]]
            # if i is a valid index AND curr is smaller than after
            elif i < len(list_char) - 1 and nums[list_char[i]] < nums[list_char[i + 1]]:
                total += 0 # ignore
            else:
                total+= nums[list_char[i]]

        return total

s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("IX"))
print(s.romanToInt("MCMXCIV"))
