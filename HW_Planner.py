# Do good stuff

"""This is a homework planner that lists assignments based on importance and urgency."""

# Provide and process main menu

from AddAssignment import *
import time

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
def status():
    # Read and parse json file

    # Calculate priorities
    priorities = []
    for i in range(len(IDs)):
        tleft = time_diff(dues[i])
        priority = importances[i] * t2completes[i] / tleft
        priorities.append(priority)

    # Sort priorities and do the same to IDs
    prios = priorities
    ids = IDs
    sprios = []
    sids = []
    while len(prios) > 0:
        maxprio = 0
        for i in range(len(prios)):
            if prios[i] >= maxprio:
                maxprio = prios[i]
                k = i

        sprios.append(prios[k])
        sids.append(ids[k])
        del prios[k]
        del ids[k]

    # Loop through assignment IDs and find the order in which to print assignments
    order = []
    for i in sids:
        thisun = IDs.index(i)
        order.append(thisun)

    # Loop through assignments in order and print them
    for i in order:
        name = names[i]
        due = dues[i]
        t2complete = t2completes[i]
        priority = importances[i]
        course = courses[i]
        pctcomplete = pctcompletes[i]
        print('\n\n', name, '\n', course, '\nPriority ', priority, '\nDue ', due, '\nTime to complete: ', t2complete,
              '\n', pctcomplete, ' % Complete')

    return None


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


def time_diff(time2):

    """Takes two times in DTG and returns the time difference between them"""

    # Create DTG for current time
    time1 = time.strftime('%d%H%MR%b%y')

    # Casefold times
    time1 = time1.casefold()
    time2 = time2.casefold()

    # Determine year difference
    year1 = int(time1[10]) * 10 + int(time1[11])
    year2 = int(time2[10]) * 10 + int(time2[11])
    ydiff = year2 - year1
    yddiff = ydiff * 365

    # Determine month difference
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun','jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month1 = time1[7:10]
    month1 = months.index(month1)
    month2 = time2[7:10]
    month2 = months.index(month2)
    mdiff = 0
    for i in range(month1, month2 - 1):
        mdiff += mdays[i]

    # Determine day difference
    day1 = time1[0:2]
    day1 = int(day1)
    day2 = time2[0:2]
    day2 = int(day2)
    ddiff = day2 - day1
    tddiff = ddiff + mdiff + yddiff

    # Determine hour difference
    hour1 = time1[2:4]
    hour1 = int(hour1)
    hour2 = time[2:4]
    hour2 = int(hour2)
    hdiff = hour2 - hour1
    thdiff = hdiff + tddiff * 24

    # Determine minute difference
    min1 = time1[4:6]
    min1 = int(min1)
    min2 = time2[4:6]
    min2 = int(min2)
    mindiff = min2 - min1
    mhdiff = mindiff / 60

    tdiff = mhdiff + thdiff

    return tdiff
