# Calculates value of each coin from weight, number of wrappers necessary
import math

def calculate():
	print "You have $%.2f of pennies and need %.0f wrappers." % ((pennies / 2.5) / 100.0, math.ceil((pennies / 2.5) / 50.0))
	print "You have $%.2f of nickles and need %.0f wrappers." % ((nickles / 5.0) / 20.0, math.ceil((nickles / 5.0) / 40.0))
	print "You have $%.2f of dimes and need %.0f wrappers." % ((dimes / 2.268) / 10.0, math.ceil((dimes / 2.268) / 50.0))
	print "You have $%.2f of quarters and need %.0f wrappers." % ((quarters / 5.67) / 4.0, math.ceil((quarters / 5.67) / 40.0))

measure = raw_input("Do you want to input pounds or grams (p/g): ")
pennies = float(raw_input("Enter weight of your pennies: "))
nickles = float(raw_input("Enter weight of your nickles: "))
dimes = float(raw_input("Enter weight of your dimes: "))
quarters = float(raw_input("Enter weight of your quarters: "))

if measure == "p":
	pennies = pennies * 453.592
	nickles = nickles * 453.592
	dimes = dimes * 453.592
	quarters = quarters * 453.592
	
	calculate()
	
else:
	calculate()