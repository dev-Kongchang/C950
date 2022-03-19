#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

import csv
from multiprocessing.connection import deliver_challenge
from hash_table import hashtable
from package import package

# Make a hash table and read in the informaion into the a list and use the id as the key
file_name = 'WGUPS Package File.csv'
packageData = hashtable()

# from this point we must figure out package sorting so we know which trucks can carry what packages
truck1 = [] # this truck will hold all the deadline packages that needs to be delivered
truck2 = [] # this truck will contain the special packages that needs to be in this truck
truck3 = [] # this truck will stay behind for the delayed packages that will be updated

# To make life easier, instead of doing another function, 
# we will add all deadline packages into a list that we will sort later
priorityPackages = []

with open(file_name) as data:
    reader = csv.reader(data)
    for row in reader:
        # create a package object everything so it can be reuse as the item for the Hash Table
        info = package()
        id = row[0]
        delivery_address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery_deadline = row[5]
        weight = row[6]
        notes = row[7]

        info.add(id, delivery_address, city, state, zip, delivery_deadline, weight, notes, 'at the hub')

        if delivery_deadline != 'EOD':
            priorityPackages.append(id)

        # we add the id as the key and the package object as the item for the hash table
        packageData.add(id, info)
    

# after all the packages are inserted in to the hash table, we will start sorting out the priorty packages

for x in priorityPackages:
    print(x)

# Package 6 is delayed so we will put it in truck 3 and pop it out
truck3.append(6)
priorityPackages.pop(1)

# Package 25 is delayed so we will put it in truck 3 and pop it out
truck3.append(25)
priorityPackages.pop(6)

# now we look at the special conditions for packages that need to go with others
# in our priorityPackages list we have 
# 14 which needs 15, 19, 
# 16 which needs 13, 19, 
# 20 which needs 13, 15
# so we need to add package 19 since we already have 13 and 15

priorityPackages.append(19)

# now we have 13 packages left and make this our truck1 

truck1 = priorityPackages

# Next we are going to add all the packages that need address update to truck 3
# since package 6, 25 is already in truck 3 we need to add the rest
truck3.append()

for x in priorityPackages:
    print(x)


