# LeetCode Q-283

class Solution:
    def moveZeroes(self,num: List[int])->None:
        l =0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r] = nums[r],nums[l]

                l+=1
        return nums