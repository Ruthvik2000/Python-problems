from collections import Counter
class solution:
    def allanagrams(self,l,s):
        k=len(s)
        hashmap=Counter(s)
        count=len(hashmap)
        i=0
        j=0
        ans=[]
        while j<len(l):
            if s[j] in hashmap:#calculations for the ans
                hashmap[s[j]]-=1
                if hashmap[s[j]]==0:
                    count-=1
            if j-i+1<k:#incrementing j
                j+=1
            if j-i+1==k:#window size matches to the k
                if count==0:#ans which wants to be returned
                    ans.append(s[i])#movement of window to the next
                if s[i] in hashmap:
                    hashmap[s[i]]+=1
                    if hashmap[s[i]] == 1:
                        count += 1
                i+=1
        return ans

a=[m for m in input().split()]
b=[m for m in input().split()]            
k=solution()
k.allangrams(a,b)