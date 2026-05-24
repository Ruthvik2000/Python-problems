class Solution:
    def sortSentence(self, s: str) -> str:
        d={}
        k=s.split()
        for i in k:
            d[i[-1]] = i[:-1]
        return ' '.join(d[j] for j in sorted(d))
"""
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
"""