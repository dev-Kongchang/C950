# Name: Kong Chang
# Student ID: 010127362
# C950 - Data Structures and Algorithms II

from audioop import add
import csv
from traceback import print_tb
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
    row = addressDictionary.get(address2)
    return distanceData[col][row]


def minDistanceFrom(address1, truck):
    # making variable placeholder so we don't modify the original and prevent bugs
    truck_dummy = Truck()
    truck_dummy = truck
    cargo = truck_dummy.get_cargo()
    # making variable to start the first package to start comparing later on
    min_distance = truck_dummy.get_first_cargo_distance()
    # variable to hold the minimun distance address so we can return it at the end
    min_address = ''

    # Time Complexity is O(N) since we are calling calcuate_distance_between function which is only O(1)
    for x in cargo:
        distance = calculate_distance_between(address1, x)
        if distance < min_distance:
            min_distance = distance
            min_address = x

    return min_address


#print(calculate_distance_between('2835 Main St', '3060 Lester St'))