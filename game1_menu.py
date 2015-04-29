print "-----------------------------------------------------------------------"
print " *** Welcome to the MANSION game menu ***"

raw_input("(Press Enter to continue...)")

print """ ~ Are you interested in learning a bit more, or would you rather jump
right in?\n ~ Type the number 1 if you wish to play the intro before entering the 
main game.\n ~ Type the number 2 if you say \"Let's Go ALREADY!!!\" and wish to 
jump right in."""

game = raw_input(">> ")

if game == "1" or game == "more":
	print "-------------------------------------------------------------------"
	print """ ~ You are a curious teenager who finds yourself stranded on a 
path. With no idea where you are or from where you came, you begin to look 
around. Fearful to stray from the path you decide to follow it up a hill and
around a large hedge of highly maintained evergreens. As you step into the 
secluded foggy courtyard you notice a massive dark shape protruding from the 
hazy background..."""
	
	print " ~ A mansion."
	print "----------------------------------------"
	
	print """ ~ Do you wish to approach the mansion and begin the game,
or quit?\nType 1 for \"ONWARD!\"\nType 2 for "NOPE, Nope, nope... Quit please!\""""
	
	mansion = raw_input(">> ")

	if mansion == "1" or mansion == "begin" or mansion == "ONWARD!":
		import game1
		
	elif mansion == "2" or mansion == "Nope":
		print "Thank you for your interest! Goodbye!"
		end()
elif game == "2" or game == "play" or game == "Let's Go ALREADY!!!":
	import game1
	
else:
	print "Type the numeric \"1\" to learn more, or \"2\" to begin"