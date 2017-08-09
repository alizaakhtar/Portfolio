import time

class User:
    # Define the fields and methods for your object here.
	def __init__(self, name):
		self.name = name
		self.connections = []
	
	def makeConnections(self, connections):
		self.connections.append(connections) 

class Network:
    # Define the fields and methods for your object here.
	def __init__(self):
		self.users = []
		
	def addusers(self, users2add):
		self.users.append(users2add)

def operations():
	choice = input("What would you like to do? a) Make a user, b) Print users, c) Add connections, d) Print connections, or e) Exit")
	if choice == "a":
		username = input("Enter your username.")
		users2add = User(username)
		my_network.addusers(users2add)
		print(users2add.name)
		operations()
	if choice == "b":
		print("Here are the users in your network: ")
		time.sleep(1)
		print(" ")
		for i in range (0, len(my_network.users)):
			print(my_network.users.pop(0).name)
		operations()
	if choice == "c":
		print("Enter who you would like to connect.")
		user1 = input("First user:")
		user2 = input("Second user:")
		operations()
	if choice == "d":
		print("Here are the connections in your network: ")
		operations()
	if choice == "e":
		time.sleep(1)
		print("Thanks for visiting, come again!")
		time.sleep(3)
		exit()

def main():
# Define the program flow for your user interface here.
	global my_network
	my_network = Network()
	operations()

	
	
main()
