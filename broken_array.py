# ID 69566012
def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        center = nums[middle]
        if center == target:
            return middle
        if nums[left] <= center:
            if nums[left] <= target < center:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if center < target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1
