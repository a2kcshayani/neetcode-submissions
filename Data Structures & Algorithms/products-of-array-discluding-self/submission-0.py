class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        final = []
        product_track = 1
        for num in nums:
            left.append(product_track)
            product_track = product_track * num
        product_track = 1
        for num in reversed(nums):
            right.append(product_track)
            product_track = product_track * num
        right.reverse()
        for i in range(len(nums)):
            final.append(right[i] * left[i])
        return final
            