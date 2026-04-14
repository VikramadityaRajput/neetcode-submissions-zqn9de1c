class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a new dictionary with a list for each sorted string
        dictionary = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dictionary:
                dictionary[sorted_word] = []
            dictionary[sorted_word].append(word)
        final_list = []
        for group in dictionary.values():
            final_list.append(group)
        return final_list
            
        


