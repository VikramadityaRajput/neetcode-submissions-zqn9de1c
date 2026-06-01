class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        HasZero = False
        HasTwoZero = False
        for num in nums:
            if HasZero and num == 0:
                HasTwoZero = True
            if num == 0:
                HasZero = True
            else: prod = prod * num
        if HasTwoZero:
            for i in range(len(nums)):
                res.append(0)
            return res
        elif HasZero: 
            for num in nums:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res
        else:
            for num in nums:
                res.append(int(prod/num))
            return res