s = open("sortedGooglePlayStore.txt", "r")   #opens file, read only
r = open("reducedGooglePlayStore.txt", "w")  #creates or reopens export file

oldkey = None
thisKey = ""
thisValue = 0.0
count = 0.0

for line in s:
    data = line.strip().split('\t')
    if len(data) != 2:  # if bad input line
        continue  # ignore it

# read into variables
    Category, Rating = data  

    if Category != thisKey:
        if thisKey:
# resultant ouput in the form of key value pair
            r.write(thisKey + '\t' + str(thisValue/count) + '\n')
            print(thisKey + '\t' + str(thisValue/count) + '\n')

# start over when changing keys
        thisKey = Category
        thisValue = 0.0
        count = 0.0

# apply the aggregation function
    thisValue += float(Rating)
# apply the count function
    count += 1
# final ouput in the key value pair i.e.,(country, average)
r.write(thisKey + '\t' + str(thisValue/count) + '\n')
print(thisKey + '\t' + str(thisValue/count) + '\n')

s.close()
r.close()



