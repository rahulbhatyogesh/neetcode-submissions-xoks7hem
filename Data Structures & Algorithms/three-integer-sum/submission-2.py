class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        myset = set()
        newset = set()
        for k in range(len(nums)):
            if (nums[k] in newset):
                continue
            newset.add(nums[k])
            i = 0
            j = len(nums) - 1
            target = -(nums[k])
            while(i<j):
                done = 0
                if (i == k):
                    i+=1
                    continue
                if (j == k):
                    j-=1
                while (True and (i<j)):
                    if ((nums[i] + nums[j])>target):
                        j-=1
                        if (i == k):
                            i+=1
                            continue
                        if (j == k):
                            j-=1
                        done = 1
                        continue
                    if ((nums[i] + nums[j]) < target):
                        if (done == 1):
                            j+=1
                            if (i == k):
                                i+=1
                                continue
                            if (j == k):
                                j-=1
                        i+=1
                        if (i == k):
                            i+=1
                            continue
                        if (j == k):
                            j-=1
                        continue
                    if ((nums[i] + nums[j]) == target):
                        lst = [nums[i], nums[j], -target]
                        lst.sort()
                        myset.add(tuple(lst))
                        i+=1
                        if (i == k):
                            i+=1
                            continue
                        if (j == k):
                            j-=1
                        continue
            
        list_of_lists = [list(t) for t in myset]
        return(list_of_lists)    