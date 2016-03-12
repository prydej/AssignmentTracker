"""
Author: Julian Pryde
File: AddAssignment.py
Name: Add Assignment
Purpose: Write new assignment to file for Assignment Tracker
"""
import json
from Ass import *


def add_assignment():

    # Ask user for information about new ass
    ass_name = input('Name of assignment: ')
    ass_date = input('Due date: ')
    ass_time = input('Time to complete: ')
    ass_priority = input('Priority: ')
    ass_class = input('Class name: ')

    # Create object of class Ass
    ass = Ass(ass_name, ass_date, ass_time, ass_priority, ass_class)

    # Write object to file
    with open('Asshole.json', 'a', 1) as asshole:
        json.dump(ass, asshole)

    return None

