"""
author: Julian Pryde
file: AddAssignment.py
name: Add Assignment
project: Homework Planner
purpose: Write new assignment to a file in json format
"""
import json


def add_assignment(assignment_list, nextid):
    # Ask user for information about new ass
    assignment_name = input('Name of assignment: ')
    assignment_date = input('Due date: (DTG) ')
    assignment_time = input('Time required to complete: ')
    assignment_priority = input('Priority: ')
    assignment_course = input('Class name: ')

    # Create dict to write to file
    assignment_dict = {'name': assignment_name, 'date': assignment_date, 'time': assignment_time,
                       'priority': assignment_priority, 'course': assignment_course, 'ID': nextid, 'complete': 0.0}
    nextid += 1  # increment id by 1

    # Concatenate current dict with previous assignments
    assignment_list.append(assignment_dict)

    # Update nextid in new assignment
    # print(type(assignment_dict))
    assignment_list[0]["nextid"] = nextid

    # Write object to file
    with open('Assignment_log.json', 'w', 1) as assignment_log:
        json.dump(assignment_list, assignment_log)

    return nextid
