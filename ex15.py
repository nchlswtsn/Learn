# imports argument variable
from sys import argv

# assigns values to argv
script, filename = argv

# assigns open command to txt variable with parameter filename
txt = open(filename)

print "Here's your file %r:" % filename
# gives txt function read with no parameters
print txt.read()
print txt.close()

print "Type the filename again:"
# file_again
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
print txt.close()