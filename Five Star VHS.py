# Copyright - Maisy Jones
# Student - University Of Northampton
# BSc Computer Network Engineering

# These Lines define the price of The New Movies and the Old Movies
NEWVID=3.00 #
OLDIES=2.00

#This Asks the clerk how many new and old movies the customer wants to purchase
CUSTNUM = int(input("How Many New Movies does the Customer Want to Purchase? "))
CUSTOLD = int(input("How Many Oldies does the Customer Want to Purchase? "))

#This code takes the quanity of the number of movies that are wanting to be purchased, and times it by the price of the movies
OLDCOST = CUSTOLD * OLDIES
NEWCOST = CUSTNUM * NEWVID

#This adds the cost for a grand total
TOTAL = OLDCOST + NEWCOST

#This codes adds the standard UK Tax of 20% onto the cost
#TOTALTAX = TOTAL * 1.20

#To Make the tax rate more configurable
TAX = 0.20 #Edit this 0.01 - 0.99 to indicate 1 to 99%
TAXCOST = TOTAL * TAX
TOTALTAX = TAXCOST + TOTAL

#This code outputs the total with and without the 20% VAT
print ("Subtotal is: £" + str(TOTAL) + "0 Without 20% VAT")
print ( " Your Total With 20% VAT Is: £" + str(TOTALTAX) + "0")