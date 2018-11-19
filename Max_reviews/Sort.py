n = open("reducedGooglePlayStore.csv", "r")  # open file, read-only
s = open("sortedGooglePlayStore.csv", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
	s.write(line)
n.close()
s.close()
