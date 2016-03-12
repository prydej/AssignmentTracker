# Do good stuff

"""This is a homework planner that lists assignments based on importance and urgency."""

# Provide and process main menu

from AddAssignment import *

if __name__ == '__main__':

    # Loop
    choice = 'l'
    while choice != 'x':

        # Print menu
        print('What do you want to do?\n')
        print('a. Add assignment\n')
        print('u. Update assignment\n')
        print('d. Display status\n')
        print('c. Mark assignment as complete\n')
        print('x. Exit the program\n')

        # Take input
        choice = input()
        choice = choice.casefold()

    # Call appropriate function
        if choice == 'a':
            add_assignment()

        elif choice == 'u':
            print('You chose u')

        elif choice == 'd':
            print('You chose d')

        elif choice == 'c':
            print('You chose c')

        elif choice != 'x':
            print("You're an idiot.")


# Display status


# Mark assignment as complete


# Create new assignment


# Update assignment

class Ass(object):

    # Fields
    ass_name = ""
    ass_date = ""
    ass_time = ""
    ass_priority = ""
    ass_course = ""

    # Methods
    def __init__(self, name, date, time, priority, course):

        self.ass_name = name
        self.ass_date = date
        self.ass_time = time
        self.ass_priority = priority
        self.ass_course = course


def make_ass(name, date, time, priority, course):

    ass = Ass(name, date, time, priority, course)
    return ass
