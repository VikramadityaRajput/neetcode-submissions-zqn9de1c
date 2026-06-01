class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortdict = {}
        for word in strs:
            w = "".join(sorted(word))
            if w not in sortdict:
                sortdict[w] = []
            sortdict[w].append(word)
        res = []
        for value in sortdict.values():
            res.append(value)
        return res