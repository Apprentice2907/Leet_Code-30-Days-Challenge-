'''Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]'''











# My logic ChatGPT coded

class MyHashMap(object):

    def __init__(self):
        self.map = []

    def put(self, key, value):
        for pair in self.map:
            if pair[0] == key:
                pair[1] = value
                return
        self.map.append([key, value])

    def get(self, key):
        for pair in self.map:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                self.map.pop(i)
                return







# Leetcode Best soltuion

# class MyHashMap:

#     def __init__(self):
#         self.size = 1009  # A prime number to reduce collisions
#         self.buckets = [[] for _ in range(self.size)]

#     def _hash(self, key):
#         return key % self.size

#     def put(self, key, value):
#         h = self._hash(key)
#         for i, (k, v) in enumerate(self.buckets[h]):
#             if k == key:
#                 self.buckets[h][i] = (key, value)
#                 return
#         self.buckets[h].append((key, value))

#     def get(self, key):
#         h = self._hash(key)
#         for k, v in self.buckets[h]:
#             if k == key:
#                 return v
#         return -1

#     def remove(self, key):
#         h = self._hash(key)
#         self.buckets[h] = [(k, v) for k, v in self.buckets[h] if k != key]

