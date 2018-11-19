s = open("sortedGooglePlayStore.csv")
r = open("reducedGooglePlayStore.csv", "w")

thisKey =""
thisValue =0.0

for line in s:

 data = line.strip().split(',')
 #store, amount
 category, reviews = data

 if category != thisKey:
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
