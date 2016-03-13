"""
author: Jason Koch
file: AssignmentStatus.py
name: Assignment Status
project: Assignment Planner
purpose: give information on current assignments

"""
import time
import json
import string
from Colors import *


def time_diff(time2):

    """Takes two times in DTG and returns the time difference between them"""

    # Create DTG for current time
    time1 = time.strftime('%d%H%MZ%b%y', time.gmtime())

    # Casefold times
    time1 = time1.casefold()
    time2 = time2.casefold()

    # Determine if Daylight Savings Time is active
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun','jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mind = months.index(time2[7:10])
    day = int(time2[0:2])
    dst = (mind > 2 or (mind == 2 and day >= 13)) and (mind < 10 or (mind == 10 and day <= 6))

    # Convert provided time to Z
    alphabet = list(string.ascii_lowercase)
    alphabet.remove('j')
    zone2s = time2[6]
    zone2 = alphabet.index(zone2s)
    if zone2 < alphabet.index('n'):
        convert = zone2 + 1

    elif zone2s == 'z':
        convert = 0

    else:
        convert = alphabet.index('n') - zone2 - 1
        if dst:
            convert += 1

    hour2 = int(time2[2:4])
    hour2 += convert

    ddef = True
    mdef = True
    ydef = True

    if hour2 < 24:
        hdef = False

    else:
        day2 = int(time2[0:2]) + 1
        hour2 -= 24
        hdef = False

        month2 = months.index(time2[7:10])

        if day2 <= mdays[month2] and day2 >= 10:
            ddef = False

        else:
            month2 += 1
            ddef = False

            if month2 <= 12:
                mdef = False

            else:
                year2 = int(time2[10:12]) + 1
                month2 = 1
                mdef = False

                if year2 >= 10:
                    ydef = False

    # Determine year difference
    year1 = int(time1[10]) * 10 + int(time1[11])

    if ydef:
        year2 = int(time2[10]) * 10 + int(time2[11])

    ydiff = year2 - year1
    yddiff = ydiff * 365

    # Determine month difference
    for i in range(ydiff + 1):
        if (year1 + i) % 4 == 0:
            mdays[1] += 1

    month1 = time1[7:10]
    month1 = months.index(month1)

    if mdef:
        month2 = time2[7:10]
        month2 = months.index(month2)

    mdiff = 0
    for i in range(month1, month2 - 1):
        mdiff += mdays[i]

    # Determine day difference
    day1 = time1[0:2]
    day1 = int(day1)

    if ddef:
        day2 = time2[0:2]
        day2 = int(day2)

    ddiff = day2 - day1
    tddiff = ddiff + mdiff + yddiff

    # Determine hour difference
    hour1 = time1[2:4]
    hour1 = int(hour1)

    if hdef:
        hour2 = time2[2:4]
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


# Display status
def status():
    # Read and parse json file
    assignment_log = open('Assignment_log.json', 'r', 1)
    assignment_data = assignment_log.read()
    assignment_data = json.loads(assignment_data)
    
    # Create lists for data
    names = []
    dues = []
    t2completes = []
    importances = []
    courses = []
    pctcompletes = []
    IDs = []
    
    # Sort the data
    for i in range(len(assignment_data) - 1):
        assignment_dict = (assignment_data[i + 1])
        names.append(assignment_dict['name'])
        dues.append(assignment_dict['date'])
        t2completes.append(float(assignment_dict['time']))
        importances.append(int(assignment_dict['priority']))
        courses.append(assignment_dict['course'])
        pctcompletes.append(float(assignment_dict['complete']))
        IDs.append(assignment_dict['ID'])

    # Calculate priorities
    priorities = []
    for i in range(len(IDs)):
        tleft = time_diff(dues[i])
        priority = importances[i] * t2completes[i] * (1 - (pctcompletes[i] / 100)) / tleft
        priorities.append(priority)

    # Sort priorities and do the same to IDs
    prios = priorities.copy()
    ids = IDs.copy()
    sprios = []
    sids = []
    while len(prios) > 0:
        maxprio = prios[0]
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
        if sprios[i] < 1:
            color = Colors.Red
        elif sprios[i] < .5:
            color = Colors.Yellow
        else:
            color = Colors.Green

        if pctcomplete != 100:
            print('\n')
            print(color + name)
            print(color + course)
            print(color + 'Priority ', priority)
            print(color + 'Due ', due)
            print(color + 'Time to complete: ', t2complete)
            print(pctcomplete, '% Complete' + color)

    input()
    color = Colors.Default
    print('' + color)

    return None
