from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target, avoid_idx):
        l, r = 0, len(nums) - 1
        while l < r:
            cur = nums[l] + nums[r]
            if cur < target:
                l += 1
            elif cur > target:
                r -= 1
            else:
                if l != avoid_idx and r != avoid_idx:
                    yield [l, r]
                    l += 1
                    r -= 1
                elif l == avoid_idx:
                    l += 1
                else:
                    r -= 1
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        TARGET = 0
        nums.sort() 
        sums_avoid_idx = defaultdict(lambda: -1)
        for i, num in enumerate(nums):
            sums_avoid_idx[num] = i

        res = set()
        for sum, avoid_idx in sums_avoid_idx.items():
            if sum * 3 == TARGET:
                count_sum = nums.count(sum)
                res.add(tuple(sorted([sum, sum, sum]))) if count_sum >= 3 else None
                continue
            two_sums = self.twoSum(nums, TARGET - sum, avoid_idx)
            for two_sum in two_sums:
                res.add(tuple(sorted([sum, nums[two_sum[0]], nums[two_sum[1]]])))
        
        return list(res)
        
if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    expected = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
    expected = [tuple(x) for x in expected]
    actual = Solution().threeSum(nums)
    if sorted(actual) == sorted(expected):
        print('PASS')
    else:
        print(actual)
        diff = set(expected) - set(actual)
        print('FAIL, missing: {}'.format(diff))