class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_sort = {}
        for key in strs:
            i = str(sorted(key))
            if i not in word_sort:
                word_sort[i] = [key]
            else:
                word_sort[i].append(key)
        return list(word_sort.values())