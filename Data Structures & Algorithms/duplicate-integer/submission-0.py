class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}

        for i in range(len(nums)):
            current=nums[i]

            if current in hashmap:
                return True
            else:
                hashmap[current]=i
        return False