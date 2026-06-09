class Solution:
    def anagramcheck(self ,s, t) -> bool:
        if len(s) != len(t) :
            return False
        my_hash = {}
        my_hash2 = {}

        for char in s:
            my_hash[char] = my_hash.get(char,1) + 1
        for char2 in t:
            my_hash2[char2] = my_hash2.get(char2,1) + 1
        if my_hash == my_hash2:
            return True
        else:
            return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## sorted("cat")
        ## "".join(sorted("cat"))  # gives you "act"
        ## key = "".join(sorted(word))
        strs_anagram = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in strs_anagram:
                new_word = []
                strs_anagram[key] = new_word
            strs_anagram[key].append(word)
        return list(strs_anagram.values())

        
        ##dict.values() 
        
        