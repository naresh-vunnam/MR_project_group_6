s = open("mappedGooglePlayStore.csv")
r = open("reducedGooglePlayStore.csv", "w")

thisKey =""
thisValue =0.0

for line in s:

 data = line.strip().split(',')
 #store, amount
 rating, reviews = data

 if rating != thisKey:
   if thisKey:
     # output the last key value pair result
     r.write(thisKey + ',' + str(thisValue)+'\n')

   # start over when changing keys
   thisKey = rating
   thisValue = 0.0
 # apply the aggregation function
 thisValue += float(reviews)
# output the final entry when done (outside for loop)
r.write(thisKey + ',' + str(thisValue)+'\n')

s.close()
r.close()
