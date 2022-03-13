#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II

import csv
file_name = 'WGUPS Distance Table.csv'

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


