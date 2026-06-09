import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq = {}
        #top_n_keys = heapq.nlargest(n, hash_map, key=hash_map.get)

        for key in nums:
            most_freq[key] = most_freq.get(key, 0) + 1
        
        return heapq.nlargest(k, most_freq, key=most_freq.get)



        
        