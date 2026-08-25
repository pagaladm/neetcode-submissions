class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            ele = nums[i]
            sec_num = target - ele
            if sec_num in seen:
                return [seen[sec_num],i]
            seen[ele] = i