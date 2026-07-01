class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prev_Map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_Map:
                return [prev_Map[diff], i]
            prev_Map[n] = i
            
        