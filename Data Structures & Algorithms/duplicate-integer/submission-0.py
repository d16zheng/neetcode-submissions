from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        dictionary = defaultdict(int)
        for i in range(n):
            dictionary[nums[i]] += 1
            
            if dictionary[nums[i]] == 2:
                return True



        return False

        