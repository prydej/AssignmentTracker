"""
Author: Julian Pryde
File: AddAssignment.py
Name: Add Assignment
Purpose: Write new assignment to file for Assignment Tracker
"""
import json


def add_assignment():

    # Ask user for information about new ass
    ass_name = input('Name of assignment: ')
    ass_date = input('Due date: ')
    ass_time = input('Time to complete: ')
    ass_priority = input('Priority: ')
    ass_course = input('Class name: ')

    # # Create object of class Ass
    # ass = Ass(ass_name, ass_date, ass_time, ass_priority, ass_class)
    #
    # # Create dictionary
    # ass = dict(ass)

    ass_dict = {'name': ass_name, 'date': ass_date, 'time': ass_time, 'priority': ass_priority,
                'course': ass_course}

    print("ass_dict['name']", ass_dict['name'])

    # Write object to file
    with open('Asshole.json', 'a', 1) as asshole:
        json.dump(ass_dict, asshole)

    return None
