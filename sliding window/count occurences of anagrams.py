from collections import Counter
class Solution:
    def findAnagrams(self, s, p):   
        hashmap = Counter(p)
        i = j = 0
        count = len(hashmap)
        counts=0
        k = len(p)
        while j < len(s):
            if s[j] in hashmap:
                hashmap[s[j]] -= 1
                if hashmap[s[j]] == 0:
                    count -= 1
            if (j-i+1) < k:
                j += 1
            elif (j-i+1) == k:
                if count == 0:
                    counts+=1
                j += 1
                if s[i] in hashmap:
                    hashmap[s[i]] += 1
                    if hashmap[s[i]] == 1:
                        count += 1
                i += 1
        return counts

"""
Input : aabaabaa
        aaba
Output : 4
"""
"""
Input : forxxorfxdofr
        for
Output : 3
"""
