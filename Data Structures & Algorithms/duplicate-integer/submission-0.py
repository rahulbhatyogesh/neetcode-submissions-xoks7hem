class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        val = False
        for i in range(len(nums)):
            if (nums[i] not in myset):
                myset.add(nums[i])
            else:
                val = True
                break
        return val