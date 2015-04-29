def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_one(arg1):
	print "arg1: %r" % arg1
	
def print_none():
	print "I got nothin'."

def john_goddard(john1, john2):
	print "%r %r" % (john1, john2)

print_two("Charles","Watson")
print_two_again("Charles","Watson")
print_one("Charles!")
print_none()
john_goddard("Apples","Oranges")