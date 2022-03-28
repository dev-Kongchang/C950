# Name: Kong Chang
# Student ID: 010127362
# C950 - Data Structures and Algorithms II

from os import stat
from package import Package
from truck import Truck
from deliverPackages import truck1, truck2, truck3
from time import sleep
import datetime
import hash_table
from csv_reader import packageData
import colorama
from colorama import Fore

# keep a global variable so we can update package #9 once
updated = False

# truck start times
truck1_time = '8:00:00'
truck3_time = '9:05:00'
truck2_time = '10:20:00'

# global variable holder
supertime = ''

# so we don't see jinky code all over
# Time complexity = O(1)
def print_delivered(package):
    print(Fore.LIGHTGREEN_EX + '\nFor Package ID: ' + str(package.get_id()) + ' | address: ' + str(package.get_deliver_address()) + '| deadline: ' + str(package.get_deadline()) + ' | city: ' + str(package.get_deliver_city()) + ' | zip: ' + str(package.get_deliver_zip()) + ' | weight: ' + str(package.get_weight()) + ' | status: ' + str(package.get_status()) + ' | delivered at: ' + str(package.get_delivered_time()) + '\n')

# so we don't see jinky code all over
# Time complexity = O(1)
def print_not_delivered(package, status):
    if status == 'en route':
        print(Fore.LIGHTYELLOW_EX + '\nFor Package ID: ' + str(package.get_id()) + ' | address: ' + str(package.get_deliver_address()) + '| deadline: ' + str(package.get_deadline()) + ' | city: ' + str(package.get_deliver_city()) + ' | zip: ' + str(package.get_deliver_zip()) + ' | weight: ' + str(package.get_weight()) + ' | status: ' + status + '\n')
    if status == 'at the hub':
        print(Fore.RED + '\nFor Package ID: ' + str(package.get_id()) + ' | address: ' + str(package.get_deliver_address()) + '| deadline: ' + str(package.get_deadline()) + ' | city: ' + str(package.get_deliver_city()) + ' | zip: ' + str(package.get_deliver_zip()) + ' | weight: ' + str(package.get_weight()) + ' | status: ' + status + '\n')

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

# this function will be used to find the package status at a certain,
# if needed, can only return the status or print 
# Time complexity = O(N)
def get_package_status(userinput_time, id, need_status):
    # we first need to know if the package belongs to which truck
    for x in range(0,16):
        what = Package()
       
        what = truck1.cargo[x]
        if int(what.get_id()) == id:
            global truck1_time
            status = get_package_status_helper(userinput_time, what, truck1_time)
            if need_status == True:
                return status
            else:
                if status == 'at the hub':
                    print(Fore.RED + ' ' + str(userinput_time) + ': ID: ' +str(what.get_id()) + ', Status: ' + str(status) + ', address: ' + str(what.get_deliver_address()) + ', deadline: ' + str(what.get_deadline()) + ', city: ' + str(what.get_deliver_city()) + ', weight: ' + str(what.get_weight()))
                    break
                if status == 'en route':
                    print(Fore.LIGHTYELLOW_EX + ' ' + str(userinput_time) + ': ID: ' +str(what.get_id()) + ', Status: ' + str(status) + ', address: ' + str(what.get_deliver_address()) + ', deadline: ' + str(what.get_deadline()) + ', city: ' + str(what.get_deliver_city()) + ', weight: ' + str(what.get_weight()))
                    break

                if status == 'delivered':
                    print(Fore.LIGHTGREEN_EX + ' ' + str(userinput_time) + ': ID: ' +str(what.get_id()) + ', Status: ' + str(status) + ', delivered at: ' + str(what.get_delivered_time()) + ', address: ' + str(what.get_deliver_address()) + ', deadline: ' + str(what.get_deadline()) + ', city: ' + str(what.get_deliver_city()) + ', weight: ' + str(what.get_weight()))
                    break
        
        if x < 8:
            what = truck2.cargo[x]
            if int(what.get_id()) == id:
                global truck2_time
                status = get_package_status_helper(userinput_time, what, truck2_time)
                if need_status == True:
                    return status
                else:
                    if status == 'at the hub':
                        print(Fore.RED +' ' + str(userinput_time) + ': ID: ' +str(what.get_id()) + ', Status: ' + str(status) + ', address: ' + str(what.get_deliver_address()) + ', deadline: ' + str(what.get_deadline()) + ', city: ' + str(what.get_deliver_city()) + ', weight: ' + str(what.get_weight()))
                        break
                    if status == 'en route':
                        print(Fore.LIGHTYELLOW_EX + ' ' + str(userinput_time) + ': ID: ' +str(what.get_id()) + ', Status: ' + str(status) + ', address: ' + str(what.get_deliver_address()) + ', deadline: ' + str(what.get_deadline()) + ', city: ' + str(what.get_deliver_city()) + ', weight: ' + str(what.get_weight()))
                        break

                    if status == 'delivered':
                        print(Fore.LIGHTGREEN_EX +' ' + str(userinput_time) + ': ID: ' +str(what.get_id()) + ', Status: ' + str(status) + ', delivered at: ' + str(what.get_delivered_time()) + ', address: ' + str(what.get_deliver_address()) + ', deadline: ' + str(what.get_deadline()) + ', city: ' + str(what.get_deliver_city()) + ', weight: ' + str(what.get_weight()))
                        break
            

        what = truck3.cargo[x]
        if int(what.get_id()) == id:
            global truck3_time
            status = get_package_status_helper(userinput_time, what, truck3_time)
            if need_status == True:
                return status
            else:
                if status == 'at the hub':
                        print(Fore.RED +' ' + str(userinput_time) + ': ID: ' +str(what.get_id()) + ', Status: ' + str(status) + ', address: ' + str(what.get_deliver_address()) + ', deadline: ' + str(what.get_deadline()) + ', city: ' + str(what.get_deliver_city()) + ', weight: ' + str(what.get_weight()))
                        break
                if status == 'en route':
                    print(Fore.LIGHTYELLOW_EX +' ' + str(userinput_time) + ': ID: ' +str(what.get_id()) + ', Status: ' + str(status) + ', address: ' + str(what.get_deliver_address()) + ', deadline: ' + str(what.get_deadline()) + ', city: ' + str(what.get_deliver_city()) + ', weight: ' + str(what.get_weight()))
                    break

                if status == 'delivered':
                    print(Fore.LIGHTGREEN_EX +' ' + str(userinput_time) + ': ID: ' +str(what.get_id()) + ', Status: ' + str(status) + ', delivered at: ' + str(what.get_delivered_time()) + ', address: ' + str(what.get_deliver_address()) + ', deadline: ' + str(what.get_deadline()) + ', city: ' + str(what.get_deliver_city()) + ', weight: ' + str(what.get_weight()))
                    break
            
    
# returns the status depending of the time given and the package delivery condition
# the logic is:
# if the given time is less than the package delivery time but less start time, we know it is at the hub
# if the given time is after the delivery time and start time, we know the package is delivered
# if the given time is after the start time but before the delivery time of the packege, then the package was en route
# Time Complexity = O(1)
def get_package_status_helper(userinput_time, package, start_time):
    what = Package()
    what = package
    packagetime = datetime.timedelta()
    # convert the string into time format so we can compare 
    packagetime = str(what.get_delivered_time())
    (h, m, s) = packagetime.split(':')
    packagetime =datetime.timedelta(hours=int(h), minutes=int(m))
    (h, m, s) = start_time.split(':')
    start_time = datetime.timedelta(hours=int(h), minutes=int(m))
    (h, m, s) = userinput_time.split(':')
    userinput_time = datetime.timedelta(hours=int(h), minutes=int(m))

    # 'at the hub' if the give time is before the truck start time
    if userinput_time < start_time:
        return 'at the hub'
    # 'en route' if given time is after start time but after delivered time
    if userinput_time > start_time and userinput_time < packagetime:
        return 'en route'
    if userinput_time > start_time and userinput_time >= packagetime:
        return 'delivered'


# this function will contain our menu options for the user
# we will keep this modular so we can come back to it if needed without
# restarting the program, making us UI more user-friendly AND ANNOYING
# Time Complexity = O(1)
def menu():
    print(Fore.WHITE + ' What do you want to view next?\n')
    userinput = input(' 1.) Check a Package?\n 2.) Quit? \n\n')
    # error-checking for user input
    convert = 0
    try:
        convert = int(userinput)
    except ValueError:
        print(' \n Please enter an valid option...')
        menu()
    if convert == 2:
        print(' Thank you! Have a great day!!!')
        exit(0)
    return convert


# Time Complexity = O(1)
def check_package():

    userinput = input(Fore.WHITE +'Please Enter a time (ex: 10:12): ')
    convertTime = datetime.timedelta()
    try:
        (h, m) = userinput.split(':')
        userinput = datetime.timedelta(hours=int(h), minutes=int(m))
        convertTime = userinput
    except ValueError:
        print(Fore.WHITE +'\n You did not enter an time, Please try again...')
        check_package()

    package_menu(convertTime)

# Time complexity = O(N)
def package_menu(time):

    time_string = str(time)
    global supertime
    (h, m, s) = time_string.split(':')
    time_string = datetime.timedelta(hours=int(h), minutes=int(m))
    
    supertime = str(time_string)

    print(Fore.WHITE +'\n Please choose one of the following options for a Package/Packages:')
    print(' 0.) Check all packages as of time: ' + str(time_string))
    print(' 1.) View Package by ID?')
    print(' 2.) View Package by delivery address?')
    print(' 3.) View Package by delivery deadline?')
    print(' 4.) View Package by delivery city?')
    print(' 5.) View Package by delivery zip code?')
    print(' 6.) View Package by weight?')
    print(' 7.) View Package by status?')
    print(' 8.) Check another time?')
    print(' 9.) Go back to previous screen?')
    userinput = input(' 10.) Quit? \n')

    convert = 0
    try:
        convert = int(userinput)
    except ValueError:
        print(' Please enter an valid option...')
        check_package()
    
    # we quit the program
    if convert == 10:
        print(' Thank you for your time, Have a great day!')
        exit(0)

    # go back to the menu section
    if convert == 9:
        sleep(.1)
        menu()

    if convert == 0:
        # check for input errors
        print('Please choose the following time period:\n')
        what = input('1.) am \n2.) pm\n')
        try:
            what = int(what)
        except ValueError:
            print('Please choose a valid option ...')
            package_menu(time)
        global morning

        if what == 2: 
            time_string = str(time)
            (h, m, s) = time_string.split(':')
            h = int(h) + 12
            time_string = datetime.timedelta(hours=int(h), minutes=int(m))
            supertime = str(time_string)
                
        # O(N)
        for x in range(1, 41):
            get_package_status(supertime, x, False)
        package_menu(time)
            
    # to check package by id, we will loop through the hash table
    if convert == 1: view_package_id(supertime)
    
    if convert == 2: view_package_address(supertime)

    if convert == 3: view_package_deadline(supertime)

    if convert == 4: view_package_city(supertime)

    if convert == 5: view_package_zip(time)

    if convert == 6: view_package_weight(supertime)

    if convert == 7: view_package_status(supertime)

    if convert == 8: check_package()


# Time complexity = O(N)
def view_package_id(time):
    sleep(.1)

    userinput = input(' Please Enter the Package ID: ')

    try:
        int(userinput)
    except ValueError:
        print(' You did not enter an ID Number, Please try again...')
        view_package_id()

    if int(userinput) < 1 or int(userinput) > 40:
        print('You did not enter a valid ID (1 - 40)')
        view_package_id(time)

    # always using placeholder, so we don't modify the original
    what = hash_table.hashtable()
    what = packageData
    package = Package() 
    package = what.get(int(userinput))
    
    # Time Complexity = O(N)
    status = get_package_status(time, int(package.get_id()), True)
    if package != None:
        if status == 'delivered':
            print_delivered(package)
        else:
            print_not_delivered(package, status)
    
    package_menu(time)


# Time Complexity = O(N)^2
def view_package_address(time):
    sleep(.1)

    userinput = input(' Please Enter a address: ')
    
    # always using placeholder, so we don't modify the original
    package = Package() 
    found = False

    for x in range(1, 41):
        # Time Complexity = O(N)
        package = packageData.get(x)
        if package.get_deliver_address() == userinput:
            # Time Complexity = O(N)
            status = get_package_status(time, int(package.get_id()), True)

            found = True
            if status == 'delivered':
                print_delivered(package)
            else:
                print_not_delivered(package, status)
    
    if found == False:
        print('No packages with the address: ' + str(userinput))
    
    package_menu(time)
    
# this function will ask for deadline from user
# Time Complexity = O(N)^2
def view_package_deadline(time):
    sleep(.1)

    userinput = input(' Please Enter a deadline (ex: time - 10:35) or (EOD): ')
    convertTime = datetime.timedelta()
    if input != 'EOD':
        try:
            (h, m) = userinput.split(':')
            userinput = datetime.timedelta(hours=int(h), minutes=int(m))
            convertTime = userinput
        except ValueError:
            print('\n You did not enter an time, Please try again...')
            view_package_deadline(time)

        # always using placeholder, so we don't modify the original
        package = Package() 
        found = False
        # Time Complexity = O(N)
        for x in range(1, 41):
            # Time Complexity = O(N)
            package = packageData.get(x)
            # get the time and convert it back to string and only get the hours and minutes
            package_time = str(package.get_deadline())
            if package_time != 'EOD':
                (h, m, s) = package_time.split(':')
                package_time = datetime.timedelta(hours=int(h), minutes=int(m))

                # compare, if found, then print
                if package_time == convertTime:
                    found = True
                    status = get_package_status(time, int(package.get_id()), True)
                    if status == 'delivered':
                        print_delivered(package)
                    else:
                        print_not_delivered(package, status)

        if found == False:
            print('\n No Package deadline found at the time you inputted')

    if input == 'EOD':
        # always using placeholder, so we don't modify the original
        package = Package() 
        found = False
        # Time Complexity = O(N)
        for x in range(1, 41):
            # Time Complexity = O(N)

            package = packageData.get(x)
            if package.get_deadline() == userinput:
                found = True
                # Time Complexity = O(N)
                status = get_package_status(time, int(package.get_id()), True)
                if status == 'delivered':
                    print_delivered(package)
                else:
                    print_not_delivered(package, status)
    
    package_menu(time)

# Time Complexity = O(N)^2
def view_package_city(time):
    sleep(.1)

    userinput = input(' Please Enter a City: ')
    
    # always using placeholder, so we don't modify the original
    package = Package() 
    found = False
    # Time Complexity = O(N)
    for x in range(1, 41):
        # Time Complexity = O(N)
        package = packageData.get(x)
        if package.get_deliver_city() == userinput:
            found = True
            # Time Complexity = O(N)
            status = get_package_status(time, int(package.get_id()), True)
            if status == 'delivered':
                print_delivered(package)
            else:
                print_not_delivered(package, status)

    if found == False:
        print('No packages with the city: ' + str(userinput))

    package_menu(time)

# Time Complexity = O(N)^2
def view_package_zip(time):
    sleep(.1)

    userinput = input(' Please Enter a zip: ')
    
    # always using placeholder, so we don't modify the original
    package = Package() 
    found = False
    # Time Complexity = O(N)
    for x in range(1, 40):
        # Time Complexity = O(N)
        package = packageData.get(x)
        if package.get_deliver_zip() == userinput:
            found = True
            # Time Complexity = O(N)
            status = get_package_status(time, int(package.get_id()), True)
            if status == 'delivered':
                print_delivered(package)
            else:
                print_not_delivered(package, status)
    
    if found == False:
        print('No packages with the zip: ' + str(userinput))

    package_menu(time)

# time Complexity = O(N)^2
def view_package_weight(time):
    sleep(.1)

    userinput = input(' Please Enter a weight: ')
    check = 0
    try:
        check = int(userinput)
    except ValueError:
        print('\n   You did not enter a valid weight, please enter integers only...')
        view_package_weight(time)
    
    userinput = check
    # always using placeholder, so we don't modify the original
    package = Package() 
    found = False
    # Time Complexity = O(N)
    for x in range(1, 41):
        # Time Complexity = O(N)
        package = packageData.get(x)
        if int(package.get_weight()) == userinput:
            found = True
            # Time Complexity = O(N)
            status = get_package_status(time, int(package.get_id()), True)
            if status == 'delivered':
                print_delivered(package)
            else:
                print_not_delivered(package, status)
    
    if found == False:
        print('No packages with the weight: ' + str(userinput))

    package_menu(time)

# Time complexity = O(N)^2
def view_package_status(time):
    sleep(.1)

    print(' 1.) delivered')
    print(' 2.) en route')
    print(' 3.) at the hub')
    userinput = input(' Please choose a status: ')
    
    if userinput != '1' and userinput != '2' and userinput != '3':
        print(' You did not choose a valid option....')
        view_package_status(time)
    
    found = False
    # always using placeholder, so we don't modify the original
    package = Package() 
    # Time Complexity = O(N)
    for x in range(1, 41):
        # Time Complexity = O(N)
        package = packageData.get(x)
        status = get_package_status(time, int(package.get_id()), True)

        if int(userinput) == 1:
            if status == 'delivered':
                found = True
                print_delivered(package)
        if int(userinput) == 2:
            if status == 'en route':
                found = True
                print_not_delivered(package, status)
        if int(userinput) == 3:
            if status == 'at the hub':
                found = True
                print_not_delivered(package, status)
    
    if found == False:
        print(' There was no packages found for the following option: ' + str(userinput) + ' for the given time: ' + str(time))
    package_menu(time)

