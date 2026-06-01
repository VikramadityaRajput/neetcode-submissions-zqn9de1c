class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = {}
        for num in nums:
            if num not in numdict:
                numdict[num] = []
            numdict[num].append(num)
        numdict2 = {}
        for key, value in numdict.items():
            numdict2[key] = len(value)
        buckets = []
        for i in range(len(nums)+1):
            bucket = []
            buckets.append(bucket)
        for key, val in numdict2.items():
            buckets[val].append(key)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res