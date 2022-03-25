# Name: Kong Chang
# Student ID: 010127362
# C950 - Data Structures and Algorithms II

import deliverPackages
from time import sleep
from package import Package
import display

class Main:
    print('     Hello! Welcome to the C950 - Data Structures and Algorithms II \n')
    print('     Performance Assessment - WGUPS Program\n')

    userinput = input(' What do you want to do?: \n' + '1 - Start Program excution?\n' + '2 - Quit?\n \n')

    try:
        what = int(userinput) 
    except ValueError:
        print(' You did not enter a valid option....\n')
        
    if what != 1 and what!= 2 : 
        print(' Please choose a valid option... \n')
       
    else:
        userinput = what

    if userinput == 1:
        print(' Starting Delivery simulation..... \n')
        sleep(1)
        orderlist = deliverPackages.truck1.cargo
        what = Package()

        print(' Truck 1 Package Loading:')
        # Time Complexity = O(N)
        for x in range(0, len(orderlist)):
            what = orderlist[x]
            print(' Package #' + str(what.get_id()) + ' is loaded into Truck 1')
            sleep(.01)

        
        orderlist = deliverPackages.truck2.cargo
        print('\n')
        print(' Truck 2 Package Loading:')
        # Time Complexity = O(N)
        for x in range(0, len(orderlist)):
            what = orderlist[x]
            print(' Package #' + str(what.get_id()) + ' is loaded into Truck 2')
            sleep(.01)

        
        orderlist = deliverPackages.truck3.cargo
        print('\n')
        print(' Truck 3 Package Loading:')
        # Time Complexity = O(N) 
        for x in range(0, len(orderlist)):
            what = orderlist[x]
            print(' Package #' + str(what.get_id()) + ' is loaded into Truck 3')
            sleep(.01)


        # ====================== Delivery Execution ===========================
        print('\n')
        print(' Starting Delivery Execution')
        print('\n')

        print(' Truck 1 Delivery:')
        # Time Complexity = O(N)
        display.display_delivery(deliverPackages.truck1, 1)

        print(' ' + str(deliverPackages.truck1.get_current_time()) + ': Truck 1 went back to base hub to switch drivers with Truck 2')

        print('\n')
        print(' Truck 3 Delivery')
        # Time Complexity = O(N)
        display.display_delivery(deliverPackages.truck3, 3)
        print(' ' + str(deliverPackages.truck3.get_current_time()) + ': Truck 3 went back to base hub')

        print('\n')
        print(' Truck 2 Delivery')
        # Time Complexity = O(N)
        display.display_delivery(deliverPackages.truck2, 2)
        print(' ' + str(deliverPackages.truck2.get_current_time()) + ': Truck 2 went back to base hub')

        # now we display the total miles of each truck and all together
        print('\n')
        print(' Day Ended at: ' + str(deliverPackages.truck3.get_current_time()))
        sleep(.01)
        print(' Truck 1 Total Miles: ' + str(deliverPackages.truck1.get_miles()))
        sleep(.01)
        print(' Truck 2 Total Miles: ' + str(deliverPackages.truck2.get_miles()))
        sleep(.01)
        print(' Truck 3 Total Miles: ' + str(deliverPackages.truck3.get_miles()))
        sleep(.01)

        total = float(deliverPackages.truck1.get_miles()) + float(deliverPackages.truck2.get_miles()) + float(deliverPackages.truck3.get_miles())
        print(' Total Miles for the whole system is: ' + str(total)+ '\n')
        # 

        userinput = display.menu()

        while userinput != 10:
            if userinput == 2: exit(1)
            if userinput == 1: display.check_package()

            userinput = display.check_package()


    else:
        print('Thank you for your time and Have a Awesome Day!')
    
    