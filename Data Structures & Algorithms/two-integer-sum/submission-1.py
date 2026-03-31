class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myset = {}
        for i in range(len(nums)):
            myset[nums[i]] = i
        
        marker = 0
        index1 = 0
        index2 = 0
        for i in range(len(nums)):
            if (marker == 0):
                if (((target - nums[i]) in myset) and (myset[target-nums[i]]!=i)):
                    index1 = i
                    marker = 1
                    continue
            if (marker == 1):
                if (nums[i] == (target - nums[index1])):
                    index2 = i
                    break
        
        return [index1,index2]