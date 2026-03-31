class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        found = 0
        for i in range(j):
            done = 0
            while True:
                if (numbers[i] + numbers[j] > target):
                    done = 1
                    j -= 1
                if (numbers[i] + numbers[j] < target):
                    if (done == 1):
                        j += 1
                    break
                if (numbers[i] + numbers[j] == target):
                    return([i+1, j+1])
                