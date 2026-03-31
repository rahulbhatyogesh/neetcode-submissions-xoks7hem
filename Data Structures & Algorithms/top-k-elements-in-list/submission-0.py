class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1

        mydict1 = {i: [] for i in range(0, len(nums)+1)}
        for i in mydict:
            mydict1[mydict[i]].append(i)

        li = []
        j = len(nums)
        while k>0:
            if (mydict1[j] != []):
                for num in mydict1[j]:
                    li.append(num)
                    k -= 1
                    if k == 0:
                        return li
                j-=1
                continue
            j-=1
        
        return li