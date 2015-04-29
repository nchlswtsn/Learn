from sys import exit

def procrastinate():
	raw_input("Do you procrastinate?")
	if mentality == "yes":
		personality = "You procrastinate."
	elif mentality == "no":
		personality = "You don't procrastinate."
	else:
		print "To procrastinate is to put something off until later."
		mentality = raw_input("Do you procrastinate?")

def start():
	print "Becoming hungry, you wonder if you should go to the store for a snack."
	print "You get up off you r couch, but then stop to decide if you should go..."
	print "What is your decision? store/stay"

	choice = raw_input(">> ")
	
	if choice == "store":
		print "You get up off the couch and walk to the local store."
		store()
	elif choice == "stay":
		couch('You sit back down and think about what to do next')
	else:
		decision("You feel rushed for time and need to quickly decide.")


def store():
	print "Entering the store, you walk the aisles."
	print "Check out the fruit or the candy? candy/fruit"
	
	choice == raw_input(">> ")
	
	if choice == "candy":
		head_home('Choosing candy, you begin your short journey home.')
	elif choice == "fruit":
		print mentality
	else:
		store("You feel rushed for time and need to quickly decide.")
	exit(0)

start()