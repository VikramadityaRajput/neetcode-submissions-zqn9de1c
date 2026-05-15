class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for word in strs:
            sorted_word = "".join(sorted(word)) #sorted returns a list so u convert to a string
            if sorted_word not in d:
                d[sorted_word] = [] #make a new list if theres a new anagram
            d[sorted_word].append(word) #add a word to its respective list
        for g in d.values():
            res.append(g)
        return res   
            
