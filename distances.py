# Name: Kong Chang
# Student ID: 010127362
# C950 - Data Structures and Algorithms II

import csv
from package import Package
from truck import Truck

file_name = 'WGUPS Distance Table.csv'
# make a global list so we can use later after uploading all the data from the csv
distanceData = []
# make a global dictionary to refer back to
addressDictionary = {}
# Summary: Make a 2D array (Adjacency Matrix)
#          This will allow for a quick check for calculating distance between different places with using the dictionary as a guide

# open the distance csv and attirbute variable to it
with open(file_name) as data:

    rowData = []
    # assign a variable to keep reading the data
    reader = csv.reader(data)

    # Time Complexity O(N) since we are adding each row into the list
    for row in reader:
        distanceData.append(row)

# =================================================================================
# the reason why we are making a dictionary now is so that later on when we are calculating the distance we won't need to look for the position again causing another for loop

# Time complexity is O(N) for this loop
for x in range(0, 28):
    col_name = distanceData[0][x]
    addressDictionary[distanceData[0][x]] = x


# this function quickly utilizes the dictionary and gives us the distance 
# by using the 2D array position
def calculate_distance_between(address1, address2):
    # since we have the dictionary for the address, we can simply pull them up quickly rather than loop through the 2D array

    # Time complexity is O(N)
    col = addressDictionary.get(address1)
    # just in case we have to check for package object given or string
    if type(address2) == Package:
        row = addressDictionary.get(address2.get_deliver_address())
    else:
        row = addressDictionary.get(address2)
    return distanceData[col][row]


def minDistanceFrom(address1, truck, need_package):
    # making variable placeholder so we don't modify the original and prevent bugs
    truck_dummy = truck
    cargo = truck_dummy.cargo
    # making variable to start the first package to start comparing later on
    min_distance = 100
    # variable to hold the minimun distance address so we can return it at the end
    
    # Time Complexity is O(N) since we are calling calcuate_distance_between function which is only O(1)
    for x in cargo:
        # we need to check if the package within the truck is delivered
        if x.get_status() != 'delivered':
            distance = float(calculate_distance_between(address1, x))
            if distance < min_distance:
                min_distance = distance
                if need_package == False:
                    min_address = x.get_deliver_address()
                else: 
                    min_address = x

    return min_address
