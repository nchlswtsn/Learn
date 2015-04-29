from sys import argv

script, user_name, favorite_drink = argv
prompt = '***~~~***'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "do you like me, %s?" % user_name
likes = raw_input(prompt)

print "I heard your favorite drink is %s,  true?" % favorite_drink
drink = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Also, you answered %r to your favorite drink being %r.
""" % (likes, lives, computer, drink, favorite_drink)