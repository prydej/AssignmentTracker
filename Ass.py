"""
Author: Julian Pryde
File: Ass.py
Name: Ass
Purpose: Assignment object
"""


class Ass:

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
