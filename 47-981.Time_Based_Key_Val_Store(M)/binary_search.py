class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # foo : [ [1,a], [3,b] ]
        values = self.store.get(key, [])
        start = 0
        end = len(values) - 1
        result = ""

        while start <= end:
            mid = (start + end) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                result = values[mid][1]
                start = mid + 1
            else:
                end = mid - 1

        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
