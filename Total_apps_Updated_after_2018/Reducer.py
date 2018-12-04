s = open("sortedGooglePlayStore.txt")   #opens file, read only
r = open("reducedGooglePlayStore.txt", "w")  #creates or reopens export file

import re
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
     r.write("{0}\t{1}\n".format(thisKey, str(count)))

   # start over when changing keys
   thisKey = category
   thisValue = 0.0
 # start comparing the dates
 if(re.match(r'[0-9]{2}/[0-9]{2}/2018', lastUpdate, re.M|re.I)):
   count += 1
# output the final entry when done (outside for loop)
r.write("{0}\t{1}\n".format(thisKey, str(count)))
s.close()
r.close()

