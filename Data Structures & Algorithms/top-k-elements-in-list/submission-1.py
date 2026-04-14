class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use a dictionary because tahts a map here;
        dictionary = {}
        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
        freq_list = [[] for i in range(len(nums) + 1)]

        for num, freq in dictionary.items():
            freq_list[freq].append(num)
        
        res = []

        for i in range(len(freq_list) - 1, 0 ,-1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res