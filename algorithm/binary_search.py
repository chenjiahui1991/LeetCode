def binary_search(nums, val):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] == val: return mid
        if nums[mid] < val: left = mid + 1
        else: right = mid - 1
    return -1


print(binary_search([2,7,11,15], 117))
