class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=0
        for i in nums:
            ans^=i
        c=1
        while ans:
            r=ans&1
            ans=ans>>1
            if r==1:
                break
            c+=1
        a=0
        b=0
        for i in nums:
            x=i
            for j in range(c-1):
                x=x>>1
            if x&1:
                a^=i
            else:
                b^=i
        return [a,b]
