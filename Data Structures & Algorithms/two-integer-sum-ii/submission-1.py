class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result=[]
        l,r=0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                result.append(l+1)
                result.append(r+1)
                break
            else:
                if numbers[l]+numbers[r]<target:
                    l+=1
                elif numbers[l]+numbers[r]>target:
                    r-=1
        return result