print "-----------------------------------------------------------------------"
print """ ~ You approach the mansion slowly, taking in the immense size of the
structure as more and more detail is revealed with each step you 
take into the fog."""
raw_input("(Press Enter to continue...)")
print "----------------------------------------"
print """ ~ Stepping up to the front door you grab the polished brass door knocker
and slam it down on the massive oak door."""
raw_input("(Press Enter to continue...)")
print "----------------------------------------"
print """ ~ To your surprise the knocker does not let out even the slightest 
sound..."""
raw_input("(Press Enter to continue...)")
print "----------------------------------------"
print """ ~ The door moves ever so slightly, so subtly that you are not sure 
if your eyes deceive you."""
raw_input("(Press Enter to continue...)")
print "----------------------------------------"
print """ ~ Reaching out you slowly push the mansion door open, listening for
heavy creaking as one would expect for a door of this size, or any size really,
but nothing more than unbroken silence comes forth. Peering into the entryway, 
darkness swallows everything beyond the threshold. You'll have to step inside 
if you wish to learn more..."""
raw_input("(Press Enter to continue...)")
print "----------------------------------------"
print "Do you choose to enter?"
print "Type 1 if you choose to enter."
print "Type 2 if you choose to remain outside."
begin = raw_input(">> ")

if begin == "1" or begin == "yes" or begin == "sure" or begin == "y":
	print " ~ You step forward into the darkness, the heavy door slamming behind!"

elif begin == "2" or begin == "n" or begin == "no":
	import game1_no
	
else:
	print """ ~ Suddenly dizzy, you stumble as your vision blurs and goes 
	dark... A noise in your head is calling for you but you can't tell 
	where it's coming from... You realize your eyes are shut and you are
	laying in bed, at home, having only been dreaming."""