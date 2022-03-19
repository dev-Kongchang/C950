#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

import csv
from hash_table import hashtable
from package import package

# Make a hash table and read in the informaion into the a list and use the id as the key
file_name = 'WGUPS Package File.csv'
packageData = hashtable()
info = package()
with open(file_name) as data:
    reader = csv.reader(data)
    for row in reader:
        id = row[0]
        delivery_address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery_deadline = row[5]
        weight = row[6]
        notes = row[7]

        info.add(id, delivery_address, city, state, zip, delivery_deadline, weight, notes, 'at the hub')

        # we add the id as the key and the package object as the item for the hash table
        packageData.add(id, info)
    

    # to make it easier to know which trucks has priority we would add them to the assigned trucks first.

