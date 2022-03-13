# Name: Kong Chang
# Student ID: 010127362
# C950 - Data Structures and Algorithms II

import csv
file_name = 'WGUPS Distance Table.csv'

# first we make the 2d array which hold our distance data
distanceData = []

with open(file_name) as data:
    reader = csv.reader(data)
    for row in reader:

        # make a list variable and loop through the total columns 
        info = [] 
        for i in range(0,29):
            info.append(row[i])

        # once the list if finished, we will append to the distanceData list
        distanceData.append(info)


for x in distanceData:
    print(x)

