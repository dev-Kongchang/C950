#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

from package import Package

class Truck:
    def __init__(self):
        self.max_capacity = 16
        self.capacity = 0
        self.cargo = []
        self.max_speed = 18
        self.driver = False
        

    def add(self, package):
        if self.capacity == self.max_capacity:
            print('truck is full')
            return False
        
        self.cargo.append(package)
        self.capacity += 1
        return True

    def get_cargo(self):
        if self.cargo == []:
            print('cargo is empty, please add some packages')
            return False
        else:
            return self.cargo
    
    def get_first_cargo_distance(self):
        if self.cargo == []:
            print('cargo is empty, please add some packages')
            return False
        else:
            return self.cargo[0]
    
    def get_current_package_address(self, index):
        # make variable placeholder to get address
        cargo = Package()
        cargo = self.cargo[index]
        if cargo.get_delivery_city() == '':
            print('delivery address is empty for package id: ' + str(cargo.get_id()))
            return False
        else:
            return cargo.get_delivery_city()