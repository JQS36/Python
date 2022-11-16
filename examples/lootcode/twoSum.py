class Solution:

    """def __init__(self, nums, target):
        print(self.twoSum(nums, target))"""

    def twoSum(nums, target):
        """hash_table = {}
        for i in range(len(nums)):
            i_number = nums[i]
            if i_number in hash_table:
                t = hash_table[nums[i]]
                return [t, i]
            else:
                tt = target - nums[i]
                hash_table[tt] = i
        return hash_table"""  
        """for idx, val in enumerate(nums):
            r = nums[idx + 1:]
            t = target - val
            if t in r:
                last = nums[idx + 1:].index(target - val) + (idx + 1)
                return [idx, last]"""
        """for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i, j])"""
        hast_target = {}
        for index, value in enumerate(nums):
            print("\033[93m : "+str(hast_target), target - value)
            if target - value in hast_target:
                return [hast_target[target - value], index]
            else:
                hast_target[value] = index
nums = [16, 7, 13, 15, 2]
print(len(nums))
target = 28
print(Solution.twoSum(nums, target))