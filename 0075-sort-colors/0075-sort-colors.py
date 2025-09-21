class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        low, mid, high = 0, 0, n - 1

        while mid <= high:
            if nums[mid] == 0:
                swap(nums, low, mid)
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                swap(nums, mid, high)
                high -= 1
