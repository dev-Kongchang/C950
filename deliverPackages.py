#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

from package import Package
from truck import Truck
from csv_reader import packageData
from loadPackages import truck1, truck2, truck3
import distances
import datetime

def caculate_time(truckTime, time):
    # 60 minutes
    newtime = time * 60 
# Since we already manually uploaded all the packages already from loadPackages.py 
# we can start the travel
# We are going to have truck3 stay till 9:05 so it can get all the packages that arrive and leave accordingly
# We are then going to have truck1 leave early and lastly have truck2 leave last

truck1_time = '8:00:00'
truck2_time = '9:05:00'

(h, m, s) = truck1_time.split(':')
truck1_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

(h, m, s) = truck2_time.split(':')
truck2_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# The neat thing is that since we already submitted 'at the hub' by default when loading up the packages in the truck, 
# we only need to update truck1's package statuses
# Time Complexity = O(N)
for x in truck1.cargo:
    what = Package()
    what = x
    what.update_deliver_status('en route')

# now we update the information
# Time Complexity = O(1)
#update_global_timekeeper(truck1_time)\



# Using Nearest Neighbor algorithm to find the best opitmal path for the truck
# we start at the hub as the first address
hub = '4001 South 700 East'
address = hub
# Starting the delivery for truck1
# 1.) update driver
truck1.driver = True
# 2.) Getting Mininal distance and updating the deliver time and miles of the truck
# Time Complexity = O(N)^2
while truck1.packages_delivered < 16:
    # Time Complexity = O(N)
    minaddress = distances.minDistanceFrom(address, truck1)
    # Time Complexity = O(1)
    miles = float(distances.calculate_distance_between(address, minaddress))

    # now we calculate the time
    speed = float(truck1.max_speed)
    timetoDeliver = miles/speed
    print(timetoDeliver)

    address = minaddress
    truck1.packages_delivered += 1

















# this function focuses on the time used for each package delivery
def truckDeliverPackages(given_truck):
    # create a variable holder so we can access the object functions 
    # and not modify the original object in any way
    what = Package()
    

