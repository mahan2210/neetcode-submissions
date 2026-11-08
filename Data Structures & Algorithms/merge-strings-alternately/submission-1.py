class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        # zip pairs characters until the shorter string ends
        for a, b in zip(word1, word2):
            res.append(a + b)
        
        # Slicing handles the remainders safely 
        res.append(word1[len(word2):])
        res.append(word2[len(word1):])
        
        return "".join(res)