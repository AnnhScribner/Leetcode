class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Create an empty string that will store the final merged result
        new_word = ""

        # We loop using an index i from 0 up to the length of the longer word.
        for i in range(max(len(word1), len(word2))):
        
            # If i is still a valid index for word1,
            if i < len(word1):
                # keeping adding
                new_word += word1[i]
                
            # If i is still a valid index for word2,
            if i < len(word2):
                # keep adding
                new_word += word2[i]
               
        # After the loop finishes, new_word contains all characters from both
        # strings, merged in alternating order as much as possible.
        return new_word
        
        
s = Solution()
print(s.mergeAlternately(['a', 'b', 'c', 'd'], ['p', 'q', 'r']))
print(s.mergeAlternately(['p', 'q', 'r'], ['a', 'b', 'c', 'd']))
