class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #first sort the array
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            required_sum = 0-nums[i]
            while left<right:
                current_sum=nums[left]+nums[right]
                if current_sum == required_sum:
                    x=[nums[i],nums[left],nums[right]]
                    if x not in result:
                        result.append(x)
                    left+=1
                    right-=1
                elif current_sum<required_sum:
                    left+=1
                else:
                    right-=1
        return result
