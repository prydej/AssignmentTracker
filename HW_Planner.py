# Do good stuff

"""This is a homework planner that lists assignments based on importance and urgency."""

# Provide and process main menu

from AddAssignment import *
from AssignmentStatus import *
import os

# Get last sequential ID number
asshole = open('Asshole.json', 'w+', 1)

# If new file is empty
if os.stat("Asshole.json").st_size:
    all_asses = json.loads(asshole.read())
else:
    asshole.write("[]")
    all_asses = []

# If new file, add array with only nextid
if "nextid" in all_asses:
    nextid = all_asses[0]["nextid"]
else:
    asshole.write('[{"nextid": 0}]')
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
            add_assignment(all_asses, nextid)

        elif choice == 'u':
            print('You chose u')

        elif choice == 'd':
            status()

        elif choice == 'c':
            print('You chose c')

        elif choice != 'x':
            print("You're an idiot.")
