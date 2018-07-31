class Solution():
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return 0
        minVal, maxVal = min(nums), max(nums)
        if minVal == maxVal: return 0
        bucketSize = max((maxVal - minVal) // len(nums), 1)
        bucketNumber = (maxVal - minVal) // bucketSize + 1
        bucket = [[None, None] for _ in range(bucketNumber)]
        for num in nums:
            k = (num - minVal) // bucketSize
            if bucket[k][0] is None: bucket[k][0] = num
            else: bucket[k][0] = min(bucket[k][0], num)
            if bucket[k][1] is None: bucket[k][1] = num
            else: bucket[k][1] = max(bucket[k][1], num)
        nonempty = []
        for i in range(bucketNumber):
            if bucket[i][0] is not None:
                nonempty.append(i)
        result = 0
        for i in range(1, len(nonempty)):
            result = max(result, bucket[nonempty[i]][0] - bucket[nonempty[i - 1]][1])
        return result

s = Solution()
print(s.maximumGap([3, 6, 9, 1]))
print(s.maximumGap([10]))
print(s.maximumGap([10, 1]))
print(s.maximumGap([1,10000000]))
print(s.maximumGap([1,1,1,1]))
print(s.maximumGap([1,1,1,1,1,5,5,5,5,5]))
print(s.maximumGap([92,30851,24320,20449,7333,29396,10949,17319,9810,26639,20622,3359,14259,4050,21966,22269,24440,20895,2386,25837,628,12174,4901,29663,2720,18750,15281,29858,1891,2833,11814,21685,8976,23961,14880,18778,4529,26957,22660,20715,23811,17025,30634,24177,12]))
