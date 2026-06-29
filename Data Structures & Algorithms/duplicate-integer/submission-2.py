class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hash = {}
        for key in nums:
            if key not in my_hash:
                my_hash[key] = 0

            my_hash[key] +=1
            if my_hash[key] > 1: return True
        return False
                
        
           
