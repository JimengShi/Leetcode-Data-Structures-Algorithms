class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}
        
    def get(self, key: int) -> int:
        if key in self.values: 
            val =  self.values.pop(key)
            self.values[key] = val
            return val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values.pop(key)
            self.values[key] = value
        elif self.capacity > len(self.values):
            self.values[key] = value
        else:
            to_remove = list(self.values.keys())[0]
            self.values.pop(to_remove)
            self.values[key] = value
            
# Time: O(1)
# Space: O(capacity)