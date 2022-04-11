class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        t=[]
        for i in range(pow(2,len(nums))):
            a=[]
            x=i
            ind=len(nums)-1
            while x:
                r=x&1
                x=x>>1
                if r:
                    a+=[nums[ind]]
                ind-=1
            t+=[a]
        return t
