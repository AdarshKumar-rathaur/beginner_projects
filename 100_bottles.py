# Prints the song

count = 100
while count > 1:
	print "%d bottles of beer on the wall\n%d bottles of beer\nyou take one down, pass it around\n%d bottles of beer on the wall\n\n" % (count, count, count-1)
	count -= 1
	
if count == 1:
	print "%d bottle of beer on the wall\n%d bottle of beer\nyou take one down, pass it around\n%s bottles of beer on the wall\n\n" % (count, count, "no")
	print "That is all!"