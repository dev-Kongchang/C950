#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

import csv
from hash_table import hashtable

# Make a hash table and read in the informaion into the a list and use the id as the key
file_name = 'WGUPS Package File.csv'
table = hashtable()
with open(file_name) as data:
    reader = csv.reader(data)
    for row in reader:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        weight = row[6]
        notes = row[7]

        info = [address, city, state, zip, delivery, weight, notes]

        table.add(id, info)
        

    def get_hash_table():
        return table

    # to make it easier to know which trucks has priority we would add them to the assigned trucks first.

