s = open("sortedGooglePlayStore.txt")   #opens file, read only
r = open("reducedGooglePlayStore.txt", "w")  #creates or reopens export file

#import date
from datetime import datetime as time
thisKey =""
thisValue =0.0
count = 0
date1="01/01/2018"
newdate1 = time.strptime(date1, "%d/%m/%Y")

for line in s:      #reads through inFile (sorted values)

 data = line.strip().split('\t')        #splits data into seperate values
 category, lastUpdate = data

 if category != thisKey:                  #writes category value to key pair.
   if thisKey:
     # output the last key value pair result
     r.write(thisKey + ',' + str(count)+'\n')

   # start over when changing keys
   thisKey = category
   thisValue = 0.0
 # apply the splitting the time function
 newdate2 = time.strptime(lastUpdate, "%d/%m/%Y")
 # start comparing the dates
if newdate2 > newdate1:
  count += 1
# output the final entry when done (outside for loop)
r.write(thisKey + '\t' + str(count)+'\n')

s.close()
r.close()

