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
    asscheek = open('Asshole.json', 'r', 1)
    ass_string = asscheek.read()
    ass_list = json.loads(ass_string)
    asscheek.close()

    change_key = 'Date'

    # While loop to ask user for things to modify
    while change_key != 'x':

        change_assignment = 0

        while change_assignment == 0:
            for seal in ass_list[1:len(ass_list)]:
                print(" - ", seal["name"])
            change_name = input('\nWhich assignment do you want to modify?')

            change_assignment = 0
            # Find place of assignment name
            for walrus in ass_list:  # iterate through all dicts in assignment list
                for otter in iter(walrus):  # iterate through all key/val pairs in current dict
                    if otter == "name":  # if name value
                        if walrus[otter] == change_name:  # if value = chosen name
                            change_assignment = walrus

            if change_assignment == 0:
                print("You're an idiot.")

        change_key = 0
        while change_key == 0:
            # Ask user for which information to change
            print(' - Name')
            print(' - Date')
            print(' - Time')
            print(' - Priority')
            print(' - Course')
            print(' - Complete')
            change_key = input('What do you want to change?').casefold()

            # Check change key
            ass_keys = ['name', 'date', 'time', 'priority', 'course', 'complete']
            fox = 0
            match = 0
            while fox <= len(ass_keys) and change_key != ass_keys[fox]:
                fox += 1
                if change_key == ass_keys[fox]:
                    match = 1
            if match == 0:
                change_key = 0
                print("You're an idiot.")
                input("")

        print("To what do you want to change the", change_key, end="")
        change_val = input("?")

        # Change information
        change_assignment[change_key] = change_val

        # write changes in assignment to file
        with open('Asshole.json', 'w', 1) as assignments:
            json.dump(ass_list, assignments)

        print("\n", change_key, "successfully changed to ", change_val, "!")
        change_key = input("Type Y to continue or X to exit to the main menu.").casefold()

    return None
