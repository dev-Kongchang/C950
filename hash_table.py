#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

# below is the class of hash table

class hashtable:
    def __init__(self):
        self.size = 10 # we are going to make a empty list entires 
        self.map = [None] * self.size
        
    # Make a function that hash the key for us
    def get_hash(self, key): 
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        # we check to see if the item is there, if it isn't then we add it
        if self.map[key_hash] is None: 
            self.map[key_hash] = list([key_value])
        else:
            for pair in self.map[key_hash]: # update the keyt if it already exist 
                if pair[0] == key:
                    pair[1] = value
            self.map[key_hash].append(key_value)
    
    def get(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            # we go through to see if the item is in there
            for pair in self.map[key_hash]: 
                if pair[0] == key:
                    return pair[1]
        return None # in case the key does not exist
    
    def delete(self, key):
        key_hash = self.get_hash(key)
        bucket = self.map[key_hash]

        # we check to see if item already exist
        for what in range(0, len(self.map[key_hash])):
            if self.map[key_hash][what][0] == key:
                self.map[key_hash].pop(what) # delete the item when found

    def print(self):
        # simply iterate through and print all keys and items
        for item in self.map:
            if item is not None:
                print(str(item))


