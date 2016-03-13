# Do good stuff

"""This is a homework planner that lists assignments based on importance and urgency."""

# Provide and process main menu

from AddAssignment import *
from AssignmentStatus import *
from ModifyAssignment import *
import os

# Get last sequential ID number
assignment_log = open("Assignment_log.json", "a+", 1)
assignment_log.seek(0, 0)
assignment_data = assignment_log.read()

# If file is empty
if os.stat("Assignment_log.json").st_size:
    assignment_list = json.loads(assignment_data)
    nextid = assignment_list[0]["nextid"]
else:
    assignment_log.write('[{"nextid": 0}]')
    assignment_list = [{"nextid": 0}]
    nextid = 0

assignment_log.close()

if __name__ == '__main__':

    # Loop
    choice = 'l'
    while choice != 'x':

        # Print menu
        print('What do you want to do?')
        print('a. Add assignment')
        print('u. Update assignment')
        print('d. Display status')
        print('c. Mark assignment as complete')
        print('x. Exit the program')

        # Take input
        choice = input()
        choice = choice.casefold()

        # Call appropriate function
        if choice == 'a':
            nextid = add_assignment(assignment_list, nextid)

        elif choice == 'u':
            modify_assignment()

        elif choice == 'd':
            status()

        elif choice == 'c':
            print('You chose c')

        elif choice != 'x':
            print("You're an idiot.")
