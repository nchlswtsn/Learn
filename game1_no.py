print "----------------------------------------"
print """ ~ You take your hand off the door and step back - the door slamming
shut."""
print "----------------------------------------"

	
print """ ~ Turning to look around, you notice a gate built into a stone wall off
to the right of the front door... \"Curious...\" you say to yourself."""

enter = raw_input("(Press Enter to continue...)")


print " ~ Do you want to check out the gate or keep looking around?"
print "Type 1 to approach the gate." 
print "Type 2 to continue looking around the front of the house. "
print "----------------------------------------"

gate = raw_input(">> ")

if gate == "1":
	print " ~ You step down off the front steps and walk up to the ivy covered gate."
	print " ~ Open gate? Type 1"
	print " ~ Look through gate? Type 2"
	print " ~ Explore along stone wall? Type 3"
	
	# if gate 123 playout needed.
	
elif gate == "2":
	print """ ~ You look around the front step and notice a keyring laying in 
	the grass"""
	print "Pick up keyring? Type 1"
	print "Ignore and keep looking? Type 2"
	print "Decide to try the front door again? Type 3"
	
	keyring = raw_input(">> ")

	# elif keyring if playout needed.