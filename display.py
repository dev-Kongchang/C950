# Name: Kong Chang
# Student ID: 010127362
# C950 - Data Structures and Algorithms II

import string
from package import Package
from truck import Truck
import deliverPackages
from time import sleep
import datetime
from csv_reader import packageData

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
                print(' 10:20:00: Package #9 was sucessfully updated with new address: 410 S State St., Salt Lake City, UT 84111 \n')
                updated = True
        print(' ' + str(what.get_delivered_time()) + ': Truck ' + str(num) +' delivered package #: ' + str(what.get_id()) + ' to address: ' + str(what.get_deliver_address()) + ', ' + str(what.get_deliver_city()) + ', ' + str(what.get_deliver_zip()))
        sleep(.1)

# this function will contain our menu options for the user
# we will keep this modular so we can come back to it if needed without
# restarting the program, making us UI more user-friendly AND ANNOYING
# Time Complexity = O(N)
def menu():
    print(' What do you want to view next?')
    userinput = input(' 1.) Check a Package?\n 2.) Check Package Statuses between 8:35 am to 9:25 am? \n 3.) Check Package Statuses between 9:35 am to 10:25 am? \n 4.) Check Package Statuses between 12:03 pm to 1:12 pm?\n\n')
    # error-checking for user input
    convert = 0
    try:
        convert = int(userinput)
    except ValueError:
        print(' Please enter an valid option...')
        menu()
    return convert

def check_package():
    print('Please choose one of the following options for a Package/Packages:')
    print(' 1.) View Package by ID?')
    print(' 2.) View Package by delivery address?')
    print(' 3.) View Package by delivery deadline?')
    print(' 4.) View Package by delivery city?')
    print(' 5.) View Package by delivery zip code?')
    print(' 6.) View Package by weight?')
    print(' 7.) View Package by status?')
    print(' 8.) Go back to previous screen?')
    userinput = input(' 9.) Quit? \n')

    convert = 0
    try:
        convert = int(userinput)
    except ValueError:
        print(' Please enter an valid option...')
        check_package()
    
    # we quit the program
    if convert == 9:
        print(' Thank you for your time, Have a great day!')
        exit(0)

    # go back to the menu section
    if convert == 8:
        sleep(.1)
        menu()

    # to check package by id, we will loop through the hash table
    if convert == 1:
        check_package_id()
    
        


def check_package_id():
    sleep(.1)

    userinput = input(' Please Enter the Package ID: \n')

    try:
        int(userinput)
    except ValueError:
        print(' You did not enter an ID Number, Please try again...')
    # always using placeholder, so we don't modify the original
    what = packageData() 
    package = Package() 
    package = what.get()
    if 