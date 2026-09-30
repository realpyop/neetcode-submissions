class TimeMap:

    def __init__(self):
        self.myMap = {}
        # {
            # "alice" : ["happy", 1], ["sad", 3]
        # }

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myMap:
            self.myMap[key] = []
        self.myMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Binary search on self.myMap[1], if it less than mid then set it at result cause we want most recent
        res, values = "", self.myMap.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res