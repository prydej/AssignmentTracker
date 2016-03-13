"""
author: Julian Pryde
file: AddAssignment.py
name: Add Assignment
project: Homework Planner
purpose: Write new assignment to a file in json format
"""
import json


def add_assignment(ass_list, nextid):
    # Ask user for information about new ass
    ass_name = input('Name of assignment: ')
    ass_date = input('Due date: ')
    ass_time = input('Time to complete: ')
    ass_priority = input('Priority: ')
    ass_course = input('Class name: ')

    # Create dict to write to file
    ass_dict = {'name': ass_name, 'date': ass_date, 'time': ass_time, 'priority': ass_priority, 'course': ass_course,
                'ID': nextid, 'complete': 0.0}
    nextid += 1  # increment id by 1

    # Concatenate current dict with previous assignments
    ass_list.append(ass_dict)

    # Update nextid in new assignment
    # print(type(ass_dict))
    ass_list[0]["nextid"] = nextid

    # Write object to file
    with open('Asshole.json', 'w', 1) as asshole:
        json.dump(ass_list, asshole)

    print(ass_list)

    return nextid
