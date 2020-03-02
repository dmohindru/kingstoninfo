# This file implements view part of mvc application for tally project
# Author: Dhruv Mohindru

class View(object):
    '''Main class to handle display of information'''
    
    def display_carton_dispatched(self, cartons):
        ''' 
        Function to display carton(s) dispatched
        @param: cartons is dictionary with key as model number and value as dispatched carton(s)
        '''
        i = 1
        total = 0
        print("----------------------------------")
        print("Dispatched cartons details")
        print("----------------------------------")

        for carton in cartons:
            print("{0}. {1} : {2} box(es)".format(i, carton, cartons[carton]))
            total = total + cartons[carton]
            i = i + 1
        print("Total: {0} box(es)".format(total))

    
    def display_invoices_dispatched(self, invoices):
        '''
        Function to display values of invoices dispatched
        @param: invoices is dictionary with key as invoice number and value as invoice amount
        '''
        i = 1
        total = 0
        print("----------------------------------")
        print("Dispatched invoices details")
        print("----------------------------------")
        for invoice in invoices:
            print("{0}. {1} : {2}".format(i, invoice, invoices[invoice]))
            total = total + invoices[invoice]
            i = i + 1
        print("Total: {0} ".format(total))

    