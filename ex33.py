i = 0
numbers = []

while i < 999:
	print "At the top i is %d" % i 
	numbers.append(1)

	i += 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
	
print "The numbers: "

for num in numbers:
	print num
