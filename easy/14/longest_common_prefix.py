class Solution:
    # Runtime O(n * m)

    def longestCommonPrefix(self, strs) -> str:
        # get the smallest word len
        smallest_word = min(strs, key=len)
        str_to_return = ""

        # for each character in the smallest word
        for i in range(len(smallest_word)):
            total_letters = 0
            # for each worf in the given strs
            for word in strs:
                # if the char in the smallest word is different than the char in word
                if smallest_word[i] != word[i]:
                    # stop counting
                    return str_to_return
                else:
                    # otherwise, count + 1
                    total_letters += 1
            # if the total_letters equals to the len of the given strs,
            # it means all the words have that specific char
            if total_letters == len(strs):
                str_to_return += smallest_word[i]

        return str_to_return


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
