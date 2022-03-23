#Name: Kong Chang
#Student ID: 010127362
# C950 - Data Structures and Algorithms II
import datetime

class Package:
    # we first set the constructors so that package class may have all the necessary compoments
    def __init__(self):
        self.id = 0
        self.deliver_address = ''
        self.deliver_deadline = ''
        self.deliver_city = ''
        self.deliver_zip = 0
        self.weight = 0
        self.deliver_status = ''
        self.delivered_time = datetime.timedelta()
    
    # function to add on all neccessary information 
    def add(self,id, address, city, state, zip, deadline, weight, notes, status):
        self.id = id
        self.deliver_address = address
        self.deliver_deadline = deadline
        self.deliver_city = city
        self.deliver_zip = zip
        self.weight = weight
        self.deliver_status = status
    
    # This is so that when we get the new address for the special package we can update it
    def update_address(self, new_address):
        self.deliver_address = new_address
    
    def update_city(self, newCity):
        self.deliver_city = newCity

    def update_zip(self, newZip):
        self.deliver_zip = newZip

    # Since we have to update package delivery times
    def update_delivered_time(self, new_time):
        self.delivered_time = new_time

    # Update the deliver status of package
    def update_deliver_status(self, new_status):
        self.deliver_status = new_status

    # Summary of get functions:
    # check to see if they are updated and if not then notifys user
    # if updated correctly, then will return the desire value 
    def get_id(self):
        if self.id == 0:
            print('ID is Null for package: ')
        else:
            return self.id

    def get_deliver_address(self):
        if self.deliver_address == '':
            print('Delivery address is Empty for package ID: ' + str(self.id))
        else:
           return self.deliver_address

    def get_deadline(self):
        if self.deliver_deadline == '':
            print('Delivery deadline is Empty for package ID: ' + str(self.id))
        else:
           return self.deliver_deadline

    def get_deliver_city(self):
        if self.deliver_city == '':
            print('Delivery city is Empty for package ID: ' + str(self.id))
        else:
           return self.deliver_city

    def get_deliver_zip(self):
        if self.deliver_zip == '':
            print('Delivery zip is Empty for package ID: ' + str(self.id))
        else:
           return self.deliver_zip
    
    def get_weight(self):
        if self.weight == '':
            print('Weight is Empty for package ID: ' + str(self.id))
        else:
           return self.weight

    def get_status(self):
        if self.deliver_status == '':
            print('Status was never inputted for package ID: ' + str(self.id))
        else:
           return self.deliver_status

    def get_delivered_time(self):
        if self.delivered_time == '':
            print('Delivery time is Empty for package ID: ' + str(self.id))
        else:
           return self.delivered_time 
