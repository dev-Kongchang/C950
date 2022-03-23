# Name: Kong Chang
# Student ID: 010127362
# C950 - Data Structures and Algorithms II
from abc import update_abstractmethods
from package import Package
from truck import Truck
import deliverPackages
from time import sleep
import datetime

# keep a global variable so we can update package #9 once
updated = False


# this function will display all the truck's delivery
# Time Complexity = O(N)
def display_delivery(giventruck, num):
    truck = Truck
    truck = giventruck
    queue = truck.packages_delivered_queue
    what = Package()
    
    # Time Complexity = O(N)
    for x in queue:
        what = truck.get_cargo(int(x))
        global updated
        update = updated
        if update == False:
            if what.get_delivered_time() > datetime.timedelta(hours=10, minutes=20, seconds=0):
                print('\n')
                print('10:20:00: Package #9 was sucessfully updated with new address: 410 S State St., Salt Lake City, UT 84111 \n')
                updated = True
        print(str(what.get_delivered_time()) + ': Truck ' + str(num) +' delivered package #: ' + str(what.get_id()) + ' to address: ' + str(what.get_deliver_address()) + ', ' + str(what.get_deliver_city()) + ', ' + str(what.get_deliver_zip()))
        sleep(.1)