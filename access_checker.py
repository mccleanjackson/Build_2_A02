"""
Jackson McClean
IS 303 - A02
Access Checker
This program checks the access level of a person based on their title, the day of the week, and the time of day. The program will determine if the person has access to the building and will display their name and access level


Inputs: 
-name (string)
-day of week (string)
-title: admin, employee, visitor
-time of day (in 24-hour format, string)- not integer because I want it to look like a time 

Process:
-input validation: ensure that the title is one of the three options, the day of the week is valid, and the time of day is in the correct format
- determine what kind of access each person has based on their title, day of the week, and time of the day
-Admins- unlimited access, any time, any day of the week
-Employees- access to building from 8am to 10pm on weekdays, and 8am to 2pm on weekends
-Visitors- access to building from 9am to 5pm on weekdays, and no access on weekends

Outputs:
-display the person's name and their access level including their title

"""

#Inputs
name = input("What is your name?: ")
day_of_week = input("What day of the week is it? ")
title = input("What is your title? (admin, employee, or visitor) ")
time_of_day = input("What time of day is it? (in 24-hour format 00:00) ")

access_granted = False

#Input Validation
valid_titles = ["admin", "employee", "visitor"]
valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

title_valid = title.lower() in valid_titles
day_valid = day_of_week.lower() in valid_days

if not title_valid:
    print(f"Invalid title entered. Please enter admin, employee, or visitor.")
if not day_valid:
    print(f"Invalid day of the week entered. Please enter a valid day of the week.")
if title_valid and day_valid:
    access_granted = True

    #Weekend Process and Outputs
    if day_of_week.lower() == "saturday" or day_of_week.lower() == "sunday":
        if title.lower() == "admin":
            access_granted = True
            print(f"(Admin) {name} has unlimited access granted")
        elif title.lower() == "employee" and (time_of_day >= "08:00" and time_of_day <= "14:00"):
            access_granted = True
            print(f"(Employee) {name} has limited weekend employee access granted")
        elif title.lower() == "employee":
            print(f"Access denied for {name} outside of employee hours on weekends")
        elif title.lower() == "visitor":
            print(f"Access denied for visitors on weekends")

    #Weekday Process and Outputs
    elif day_of_week.lower() == "monday" or day_of_week.lower() == "tuesday" or day_of_week.lower() == "wednesday" or day_of_week.lower() == "thursday" or day_of_week.lower() == "friday":
        if title.lower() == "admin":
            access_granted = True
            print(f"(Admin) {name} has unlimited access granted")
        elif title.lower() == "employee" and (time_of_day >= "08:00" and time_of_day <= "22:00"):
            access_granted = True
            print(f"(Employee) {name} has limited weekday employee access granted")
        elif title.lower() == "employee":
            print(f"Access denied for {name} outside of employee hours on weekdays")
        elif title.lower() == "visitor" and (time_of_day >= "09:00" and time_of_day <= "17:00"):
            access_granted = True
            print(f"(Visitor) {name} has limited weekday visitor access granted")
        elif title.lower() == "visitor":
            print(f"Access denied for {name} outside of visitor hours on weekdays")

    if not access_granted:
        print(f"Access denied for {name} {title} on {day_of_week} at {time_of_day}") 
        access_granted = False

