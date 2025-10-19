class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        for pair in self.map[h]:
            if pair[0] == key:
                pair[1] = value
                return
        self.map[h].append([key, value])

    def get(self, key: int) -> int:
        h = self.hash(key)
        for pair in self.map[h]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        for i, pair in enumerate(self.map[h]):
            if pair[0] == key:
                self.map[h].pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)