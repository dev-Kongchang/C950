#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

import csv
from hash_table import hashtable
from package import Package

# Make a hash table and we are going to use the package id as the key and the package object as the item 
# when storing into the hash table
file_name = 'WGUPS Package File.csv'
packageData = hashtable()

# Nested loops
# Time Complexity = O(N)^2
with open(file_name) as data:
    reader = csv.reader(data)
    # Time Complexity = O(N)
    for row in reader:
        # create a package object everything so it can be reuse as the item for the Hash Table
        info = Package()
        id = row[0]
        delivery_address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery_deadline = row[5]
        weight = row[6]
        notes = row[7]

        # time complexity = O(N)
        info.add(id, delivery_address, city, state, zip, delivery_deadline, weight, notes, 'at the hub')

        # we add the id as the key and the package object as the item for the hash table
        # Time Complexity = O(N)
        packageData.add(id, info)
    