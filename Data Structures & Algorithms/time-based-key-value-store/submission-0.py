class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #literally just adding a list to the value of the map
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = "" #initialize this way as per instructions
        values = self.store.get(key, [])
        #now do the binary search
        left, right = 0, len(values) - 1
        
        while left <= right:
            m = (left + right) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                left = m + 1
            else:
                right = m - 1
        
        return res
