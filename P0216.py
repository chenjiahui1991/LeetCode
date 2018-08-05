class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(nums, k, rest, subset, set):
            if k == 1:
                if rest in nums:
                    subset.append(rest)
                    set.append(subset[:])
                    subset.pop()
                else:
                    return
            if len(nums) < k or sum(nums[:k]) > rest or rest > sum(nums[-k:]):
                return
            for i in range(len(nums)):
                subset.append(nums[i])
                dfs(nums[i + 1:], k - 1, rest - nums[i], subset, set)
                subset.pop()
        nums = range(1, 10)
        result = []
        dfs(nums, k, n, [], result)
        return result


s = Solution()
print(s.combinationSum3(3, 9))
