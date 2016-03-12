# Do good stuff

"""This is a homework planner that lists assignments based on importance and urgency."""

# Provide and process main menu


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
            print('You chose a')

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