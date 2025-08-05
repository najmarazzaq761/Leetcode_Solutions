class MyHashSet:

    def __init__(self):
        self.size=10**6 + 1
        self.set =  [False]*self.size

    def add(self, key: int) -> None:
        
        self.set[key] = True
    def remove(self, key: int) -> None:
        self.set[key] = False
    def contains(self, key: int) -> bool:
        
        return self.set[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)