class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        frq=[0]*26
        frq1=[0]*26
        l=len(p)
        l1=len(s)
        if l>l1:
            return []
        t=[]
        for i in range(len(p)):
            frq[ord(p[i])-97]+=1
            frq1[ord(s[i])-97]+=1
        for i in range(len(s)-(l-1)):
            ref=0
            for j in range(26):
                if frq[j]!=frq1[j]:
                    ref=1
                    break
            if ref==0:
                t+=[i]
            if (i+l)<l1:
                frq1[ord(s[i])-97]-=1
                frq1[ord(s[i+l])-97]+=1
        return t
