# Name: Kong Chang
# Student ID: 010127362
# C950 - Data Structures and Algorithms II

import csv

# make variable 
file_name = 'WGUPS Distance Table.csv'
distanceData = []
# Summary: Make a 2D array (Adjacency Matrix)
#          This will allow for a quick check for calculating distance between different places

# open the distance csv and attirbute variable to it
with open(file_name) as data:

    rowData = []
    # assign a variable to keep reading the data
    reader = csv.reader(data)

    # Time Complexity O(N) since we are adding each row into the list
    for row in reader:
        distanceData.append(row)
        
def calculate_distance_between(address1, address2):
    # make variable to hold address1 and address2
    col = 0
    row = 0
    
    # Since we are using an Adjacency Matrix, we only need to find the column and row position once
    # therefore only needing one loop, Time Complexity O(N)
    for x in range(0, 28):
        col_name = distanceData[0][x]

        if address1 == col_name:
            col = x
        if address2 == col_name:
            row = x

        if col != 0 and row != 0:
            break
    
    return distanceData[col][row]

print(calculate_distance_between('2835 Main St', '3060 Lester St'))