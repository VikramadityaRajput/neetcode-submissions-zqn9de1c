class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        count = 0
        for num in nums:
            if num == 0:
                count += 1
        for num in nums:
            if num != 0:
                product *= num
        if count > 1:
            for num in nums:
                res.append(0)
        elif 0 in nums:
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(product)
        else: 
            for num in nums:
                add = int(product / num)
                res.append(add)
        return res

            