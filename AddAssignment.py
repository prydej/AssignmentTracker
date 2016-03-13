"""
Author: Julian Pryde
File: AddAssignment.py
Name: Add Assignment
Project: Homework Planner
Purpose: Write new assignment to file for Assignment Tracker
"""
import json


def add_assignment(all_asses, nextid):
    # Ask user for information about new ass
    ass_name = input('Name of assignment: ')
    ass_date = input('Due date: ')
    ass_time = input('Time to complete: ')
    ass_priority = input('Priority: ')
    ass_course = input('Class name: ')

    # Assign ID Number
    ass_id = nextid
    nextid += 1

    # Create dict to write to file
    ass_dict = {'name': ass_name, 'date': ass_date, 'time': ass_time, 'priority': ass_priority, 'course': ass_course,
                'ID': ass_id}

    # Create json string from object
    new_ass_string = json.dumps(ass_dict, sort_keys=True, indent=4, separators=(',', ': '))
    print(new_ass_string)

    # Concatenate current dict with previous assignments
    all_asses.append(ass_dict)

    # Update nextid in new assignment
    print(type(ass_dict))
    all_asses[0] = {"nextid": 0}

    # Write object to file
    with open('Asshole.json', 'w', 1) as asshole:
        json.dump(new_ass_string, asshole)

    return None
