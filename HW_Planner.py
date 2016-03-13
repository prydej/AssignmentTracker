# Do good stuff

"""This is a homework planner that lists assignments based on importance and urgency."""

# Provide and process main menu

from AddAssignment import *
from AssignmentStatus import *
import os

# Get last sequential ID number
asshole = open("Asshole.json", "a+", 1)
asshole.seek(0, 0)
asses = asshole.read()

# If file is empty
if os.stat("Asshole.json").st_size:
    ass_string = json.loads(asses)
    nextid = ass_string[0]["nextid"]
else:
    asshole.write('[{"nextid": 0}]')
    ass_string = []
    nextid = 0

asshole.close()

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
            nextid = add_assignment(ass_string, nextid)

        elif choice == 'u':
            print('You chose u')

        elif choice == 'd':
            status()

        elif choice == 'c':
            print('You chose c')

        elif choice != 'x':
            print("You're an idiot.")
