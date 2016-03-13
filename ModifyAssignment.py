"""
Author: Julian Pryde
File: ModifyAssignment.py
Name: Modify Assignment
Project: Homework Planner
Purpose: Modify assignments in Homework Tracker
"""
import json

def modify_assignment():

    # Open assignments file
    assignment_log = open('Assignment_log.json', 'r', 1)
    assignment_data = assignment_log.read()
    assignment_list = json.loads(assignment_data)
    assignment_log.close()

    change_key = 'Date'

    # While loop to ask user for things to modify
    while change_key != 'x':

        change_assignment = 0

        while change_assignment == 0:
            print()
            for seal in assignment_list[1:len(assignment_list)]:
                print(" - ", seal["name"])
            change_name = input('\nWhich assignment do you want to modify? ')

            change_assignment = 0
            # Find place of assignment name
            for walrus in assignment_list:  # iterate through all dicts in assignment list
                for otter in iter(walrus):  # iterate through all key/val pairs in current dict
                    if otter == "name":  # if name value
                        if walrus[otter] == change_name:  # if value = chosen name
                            change_assignment = walrus

            if change_assignment == 0:
                print("You're an idiot.")

        change_key = 0
        while change_key == 0:
            # Ask user for which information to change
            print(' n. Name')
            print(' d. Due Date')
            print(' t. Time Required')
            print(' p. Priority')
            print(' c. Course')
            print(' o. Progress')
            change_key = input('What do you want to change? ').casefold()

            # Assign a key
            if change_key == 'n':
                change_key = 'name'
                field = 'Name'
            elif change_key == 'd':
                change_key = 'date'
                field = 'Due Date (DTG)'
            elif change_key == 't':
                change_key = 'time'
                field = 'Time Required (hours)'
            elif change_key == 'p':
                change_key = 'priority'
                field = 'Priority (1 - 10)'
            elif change_key == 'c':
                change_key = 'course'
                field = 'Course'
            elif change_key == 'o':
                change_key = 'complete'
                field = 'Progress (percentage)'

            # Check change key
            assignment_keys = ['name', 'date', 'time', 'priority', 'course', 'complete']
            fox = 0
            match = 0
            while fox <= len(assignment_keys) and match == 0:
                if change_key == assignment_keys[fox]:
                    match = 1
                fox += 1
            if match == 0:
                change_key = 0
                print("You're an idiot.")
                input("")

        print("To what do you want to change the", field, end="")
        change_val = input("? ")

        # Change information
        change_assignment[change_key] = change_val

        # write changes in assignment to file
        with open('Assignment_log.json', 'w', 1) as assignments:
            json.dump(assignment_list, assignments)

        change_key = input("\nType Y to continue or X to exit to the main menu. ").casefold()

    return None
