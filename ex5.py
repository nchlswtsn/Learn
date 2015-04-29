my_name = 'Charles N. Watson'
my_age = 23 # not a lie
my_height = 73 # inches
my_weight = 190 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
 
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth


print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight) 

input_weight = raw_input("Convert your weight to kg. Weight in lbs?")
input_height = raw_input("Convert your height to cm. Your height in inches?")
input_age = raw_input("Your age?")

print "kg:", float(input_weight) * .453592
print "cm:", float(input_height) * 2.54
print "age:", input_age

print "Your total is:"

print my_age + my_weight + my_height
