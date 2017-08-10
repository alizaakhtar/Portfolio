import csv
import string
import time

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
#print(countries[0])
#print(countries)

def operations():
	item = input("What country would you like to search? (click e to exit)")
	if item == "e":
		exit()
	def binarySearch(countries, item):
		first = 0
		last = len(countries)-1
		found = False

		while first<=last and not found:
			midpoint = (first + last)//2
			if countries[midpoint] == item:
				found = True
				print(item + " was found.")
			else:
				if item < countries[midpoint]:
					last = midpoint-1
				else:
					first = midpoint+1
			
		if not found:
			print("Sorry, " + item + " was not found.") 
		return found
		
	binarySearch(countries, item)

while True:
	operations()
	time.sleep(1)