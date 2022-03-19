#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II
from package import package

class truck:
    def __init__(self):
        self.max_capacity = 16
        self.capacity = 0
        self.cargo = []
        self.max_speed = 18
        
    def add(self, package as package):
        if self.capacity == self.max_capacity:
            
        
        self.cargo.append(package)
        self.capacity += 1

