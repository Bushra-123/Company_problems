class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for index,value in enumerate(nums):
            if(target-value in d):
                return(d[target-value],index)
            else:
                d[value] = index
                
 

/*SOLTUION 2*/



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
                
