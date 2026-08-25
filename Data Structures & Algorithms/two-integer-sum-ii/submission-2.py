class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            c_sum = numbers[left]+numbers[right]
            if c_sum == target:
               return [left + 1 , right + 1 ]
            if c_sum <target:
                left+=1
            else:
                right -= 1