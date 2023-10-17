# Copyright - Maisy Jones
# Student - University Of Northampton
# BSc Computer Network Engineering

HOURS = 365 * 24
MINUTES = HOURS * 60

CUSTHOURS = int(input("How Many Days do you want to convert to minutes?: "))
SUBTOTAL = CUSTHOURS * 24
TOTAL = SUBTOTAL * 60

print("There are " + str(TOTAL) + " Minutes In " + str(CUSTHOURS) + " Day(s)")