#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

from struct import pack
from package import Package
from truck import Truck
from csv_reader import packageData
from loadPackages import truck1, truck2, truck3
import distances
import datetime

# this function does the time calculation for miles driven 
# return the updated time
# Time Complexity = O(1)
def update_time(miles, speed, time):
    timetoDeliver = miles/speed
    second = timetoDeliver * 3600
    convertTime = datetime.timedelta(seconds=second)
    time = datetime.timedelta()
    time = time + convertTime
    return time

# Since we already manually uploaded all the packages already from loadPackages.py 
# we can start the travel
# We are going to have truck3 stay till 9:05 so it can get all the packages that arrive and leave accordingly
# We are then going to have truck1 leave early and lastly have truck2 leave last

truck1_time = '8:00:00'
truck3_time = '9:05:00'
truck2_time = '10:20:00'

(h, m, s) = truck1_time.split(':')
truck1_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

(h, m, s) = truck3_time.split(':')
truck3_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

(h, m, s) = truck2_time.split(':')
truck2_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# The neat thing is that since we already submitted 'at the hub' by default when loading up the packages in the truck, 
# we only need to update truck1's package statuses
# Time Complexity = O(N)
for x in truck1.cargo:
    what = Package()
    what = x
    what.update_deliver_status('en route')


# This function is used to deliver the packages within the truck
# Time complexity = O(N)^2
def deliver(truck, time):
    # Using Nearest Neighbor algorithm to find the best opitmal path for the truck
    # we start at the hub as the first address
    hub = '4001 South 700 East'
    address = hub
    # Starting the delivery for truck1
    # 1.) update driver
    truck.driver = True
    # 2.) Getting Mininal distance and updating the deliver time and miles of the truck
    # Time Complexity = O(N)^2
    while truck.packages_delivered < truck.capacity:
        # a.) we find the closest address
        #     Time Complexity = O(N)
        minaddress = distances.minDistanceFrom(address, truck, False)
        
        # b.) We update the truck miles within the truck Object
        #     Time Complexity = O(1)
        miles = float(distances.calculate_distance_between(address, minaddress))
        truck.update_miles(miles)

        # c.) Variable Placeholder to hold the returned Package Object
        #     Time Complexity = O(N)
        package = Package()
        package = distances.minDistanceFrom(address, truck, True)

        # d.)now we calculate the time which is distance/avd speed
        speed = float(truck.max_speed)
        timetoDeliver = miles/speed
        # then we convert the hours into seconds
        second = timetoDeliver * 3600

        # e.) convert the time and record it
        convertTime = datetime.timedelta(seconds=second)
        time = time + convertTime

        address = minaddress

        # f.) we udpate the hash table with the time delivered and status
        #     with the cloned package object returned @ step c
        #     Time Complexity = O(1)
        package.update_deliver_status('delivered')

        #     Time Complexity = O(1)
        package.update_delivered_time(time)

        # add the package that is delivered to the delivered queue within Truck object
        #     Time Complexity = O(1)
        truck.add_to_queue(package.get_id())

        # update the truck's current time
        #     Time Complexity = O(1)
        truck.update_current_time(time)

        # once the clone is update, we update the package object that has the package id within
        # the hash table 
        #     Time Complexity = O(N)
        packageData.update(package.get_id(), package)

        # g.) update the truck so we can get out of while loop
        truck.packages_delivered += 1

# =================================================================
# offical start of the delivery process
# 1.) start the truck 1 delivery process
deliver(truck1, truck1_time)

# 2.) return truck 1 back to the hub so we can start truck 3
#      a.) we need to get the last package that was delivered so we can 
#          calculate the distance and time the truck needs to go back base
hub = '4001 South 700 East'
what = Package()
what = truck1.get_last_delivered_package()
miles = float(distances.calculate_distance_between(what.get_deliver_address(), hub))
truck1.update_miles(miles)
newTime = truck1.get_current_time() + update_time(miles, 18, truck1_time)
truck1.update_current_time(newTime)
# we then make truck 1 driver false
truck1.driver = False

# =================================================================
# 3.) Start the truck 3 delivery process
#     we are going to use truck 1 time since it traveled back to the base
#     we can continue using that time since no time pass when move driver to different trucks

# Update package statuses
# Time Complexity = O(N)
for x in truck3.cargo:
    what = Package()
    what = x
    what.update_deliver_status('en route')

deliver(truck3, truck3_time)

hub = '4001 South 700 East'
what = Package()
what = truck3.get_last_delivered_package()
miles = float(distances.calculate_distance_between(what.get_deliver_address(), hub))
truck3.update_miles(miles)
newTime = truck3.get_current_time() + update_time(miles, 18, truck3_time)
truck3.update_current_time(newTime)

# =================================================================
# 4.) Start the truck 2 delivery process
# Update package statuses and package #9's delivery address
# Time Complexity = O(N)
for x in truck2.cargo:
    what = Package()
    what = x
    what.update_deliver_status('en route')
    if int(x.get_id()) == 9:
        # Update truck Package object
        x.update_address('410 S State St')
        x.update_city('Salt Lake City')
        x.update_zip('84111')
        # Update Hash table as well
        packageData.update(x.get_id(), x)

deliver(truck2, truck2_time)
hub = '4001 South 700 East'
what = Package()
what = truck2.get_last_delivered_package()
miles = float(distances.calculate_distance_between(what.get_deliver_address(), hub))
truck2.update_miles(miles)
newTime = truck2.get_current_time() + update_time(miles, 18, truck2_time)
truck2.update_current_time(newTime)
