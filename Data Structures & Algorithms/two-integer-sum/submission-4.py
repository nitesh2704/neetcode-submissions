class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}

        for i,num in enumerate(nums):
            current=nums[i]
            complement=target-current

            if complement in result:
                return [result[complement],i]
        
            result[current]=i
