n = open("mappedGooglePlayStore.txt", "r")  # open file, read-only

s = open("sortedGooglePlayStore.txt", "w") # open file, write

lines = n.readlines()   #reads in lines into an array and sorts them.
lines.sort()

for line in lines:     #rewrites lines in order
	s.write(line)
	
n.close()
s.close()
