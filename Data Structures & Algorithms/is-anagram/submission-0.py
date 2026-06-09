class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_hash = {}
        my_hash2 = {}

        for char in s:
            my_hash[char] = my_hash.get(char, 0) + 1
        for char2 in t:
            my_hash2[char2] = my_hash2.get(char2, 0) + 1
        
        if my_hash == my_hash2:
            return True
        else:
            return False
        


            