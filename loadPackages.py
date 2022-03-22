#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

from package import Package
from truck import Truck
from csv_reader import packageData

# This module will focus on loading the packages into the trucks

truck1 = Truck() # this truck will have all the deadline packages
truck2 = Truck() # this truck will have the special condition packages and EOD
truck3 = Truck() # this truck will have all the delayed/need to update packages

truck1.add(packageData.get(1))
truck1.add(packageData.get(13))
truck1.add(packageData.get(14)) # must be delivered with 15, 19
truck1.add(packageData.get(15)) 
truck1.add(packageData.get(16)) # must be delivered with 13, 19
truck1.add(packageData.get(19))
truck1.add(packageData.get(20)) # must be delivered with 13, 15
truck1.add(packageData.get(29))
truck1.add(packageData.get(30))
truck1.add(packageData.get(31))
truck1.add(packageData.get(34))
truck1.add(packageData.get(37))
truck1.add(packageData.get(40))
truck1.add(packageData.get(2))
truck1.add(packageData.get(4))
truck1.add(packageData.get(5))


truck2.add(packageData.get(3))
truck2.add(packageData.get(9))
truck2.add(packageData.get(18))
truck2.add(packageData.get(36))
truck2.add(packageData.get(38))
truck2.add(packageData.get(28))
truck2.add(packageData.get(35))
truck2.add(packageData.get(39))

truck3.add(packageData.get(6))
truck3.add(packageData.get(25))
truck3.add(packageData.get(32))
truck3.add(packageData.get(7))
truck3.add(packageData.get(8))
truck3.add(packageData.get(10))
truck3.add(packageData.get(11))
truck3.add(packageData.get(12))
truck3.add(packageData.get(17))
truck3.add(packageData.get(21))
truck3.add(packageData.get(22))
truck3.add(packageData.get(23))
truck3.add(packageData.get(24))
truck3.add(packageData.get(26))
truck3.add(packageData.get(27))
truck3.add(packageData.get(33))


