# This file implements controller part of mvc application for tally project
# Author: Dhruv Mohindru
import view

class Contoller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def welcome_mess(self):
        '''Print welcome message to user''' 
        print("Welcome to Kingston Impex Tally information project")

    
    def print_menu(self):
        '''Print menu for user'''
        print("Please select following options")
        print("1. For carton dispatch summary with value")
        print("(q) to quit")
    
    def accept_input(self):
        '''Accept input from user'''
        choice = input()
        return choice


def main():
    '''Main function entry'''
    my_cartons = {'(K-101) 2 Pcs': 2, '(K-202) 2 Pcs': 2, '(K-203) 1 Pcs': 1, '(K-151) 2 Pcs': 3 }
    my_invoices = {'1234': 21230.69, '1246': 35987.36, '1245': 10569.36, '1250': 25897.69 }
    c = Contoller(None, view.View())
    c.welcome_mess()
    while True:
        c.print_menu()
        choice = c.accept_input()
        if choice == 'q':
            break
        elif choice == '1':
            c.view.display_carton_dispatched(my_cartons)
            c.view.display_invoices_dispatched(my_invoices)


if __name__ == "__main__":
    main()

