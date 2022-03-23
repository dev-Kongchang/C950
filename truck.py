#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

from package import Package
import datetime

class Truck:
    def __init__(self):
        self.max_capacity = 16
        self.capacity = 0
        self.cargo = []
        self.max_speed = 18
        self.driver = False
        self.miles = 0.0
        self.packages_delivered = 0
        self.packages_delivered_queue = []
        self.current_time = datetime.timedelta()
        
    # Time Complexity = O(1)
    def add(self, package):
        if self.capacity == self.max_capacity:
            print('truck is full')
            return False
        
        self.cargo.append(package)
        self.capacity += 1
        return True

    # Time Complexity = O(1)
    def update_current_time(self, newTime):
        self.current_time = newTime

    # Time Complexity = O(1)
    def get_current_time(self):
        return self.current_time

    # Time Complexity = O(1)
    def add_to_queue(self, package_id):
        self.packages_delivered_queue.append(package_id)

    # This function returns the last package object that was delivered
    # Time Complexity = O(N)
    def get_last_delivered_package(self):
        id = self.packages_delivered_queue[len(self.packages_delivered_queue) - 1]
        # look for the package infomation
        for x in self.cargo:
            if x.get_id() == id:
                return x
                

    # Time Complexity = O(N)
    # this returns a Package Object 
    def get_cargo(self, id):
        what = Package()
        if self.cargo == []:
            print('cargo is empty, please add some packages')
            return False
        else:
            for x in self.cargo:
                what = x
                if int(what.get_id()) == id:
                    return what
                    
    
    # Time Complexity = O(1)
    def get_first_cargo_distance(self):
        if self.cargo == []:
            print('cargo is empty, please add some packages')
            return False
        else:
            return self.cargo[0]
    
    # Time Complexity = O(1)
    def get_current_package_address(self, index):
        # make variable placeholder to get address
        cargo = Package()
        cargo = self.cargo[index]
        if cargo.get_delivery_city() == '':
            print('delivery address is empty for package id: ' + str(cargo.get_id()))
            return False
        else:
            return cargo.get_delivery_city()

    # Time Complexity = O(1)
    def update_miles(self, miles):
        self.miles += miles

    # Time Complexity = O(1)
    def get_miles(self):
        if self.miles == 0:
            print('Truck 1: Miles = 0')
            return self.miles
        else:
            return self.miles

    # this function returns a dictionary consisting of 
    # of the package id and it's status
    # Time Complexity = O(N)
    def get_packages_status(self):
        # make a Package object so we can use its functions
        what = Package()
        # make a dict to hold the id and status of each packages
        book = dict()

        # Time complexity O(N)
        for x in range(0, len(self.cargo)):
            book[what.get_id()] = what.get_status()
            
        return book