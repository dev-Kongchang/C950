#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

# below is the class of hash table

class hashtable:
    # constructors
    def __init__(self):
        self.size = 10 # we are going to make a empty list entires 
        self.map = [None] * self.size
        
    # Make a function that hash the key for us
    # Time complexity is O(1)
    def get_hash(self, key): 
        hash = int(key)
        hash = hash % len(self.map)
        return hash 

    # Time complexity is O(N)
    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        # we check to see if the item is there, if it isn't then we add it
        if self.map[key_hash] is None: 
            self.map[key_hash] = list([key_value])
        else:
            for pair in self.map[key_hash]: # update the key if it already exist 
                if pair[0] == key:
                    pair[1] = value
            self.map[key_hash].append(key_value)
    
    # Time complexity is O(N)
    def get(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            # we go through to see if the item is in there
            for pair in self.map[key_hash]: 
                if pair[0] == str(key):
                    return pair[1]
        print('key Does not Exist for Key: ' + str(key))
        return None # in case the key does not exist\
    
    # Time complexity is O(N)
    def delete(self, key):
        key_hash = self.get_hash(key)

        # we check to see if item already exist
        for what in range(0, len(self.map[key_hash])):
            if self.map[key_hash][what][0] == key:
                self.map[key_hash].pop(what) # delete the item when found

    # Time complexity is O(N)
    def print(self):
        # simply iterate through and print all keys and items
        for item in self.map:
            if item is not None:
                print(str(item))


    # Time complexity is O(N)
    def update(self, key, value):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            # we go through to see if the item is in there
            for pair in self.map[key_hash]: 
                if pair[0] == key:
                    # update the item with the desired value
                    pair[1] = value
                    break

# CITATION
# author: Joe James
# Source: Youtube
# Title Video: Python: Creating a HASHMAP using Lists
# Date Accessed: 3/20/2022
