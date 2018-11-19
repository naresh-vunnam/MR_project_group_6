s = open("sortedGooglePlayStore.csv")   #opens file, read only
r = open("reducedGooglePlayStore.csv", "w")  #creates or reopens export file

thisKey =""
thisValue =0.0

for line in s:      #reads through inFile (sorted values)

 data = line.strip().split(',')        #splits data into seperate values
 category, reviews = data

 if category != thisKey:                  #writes category value to key pair.
   if thisKey:
     # output the last key value pair result
     r.write(thisKey + ',' + str(thisValue)+'\n')

   # start over when changing keys
   thisKey = category
   thisValue = 0.0
 # apply the aggregation function
 thisValue += float(reviews)
# output the final entry when done (outside for loop)
r.write(thisKey + ',' + str(thisValue)+'\n')

s.close()
r.close()
