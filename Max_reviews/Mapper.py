f = open("googleplaystore.csv",encoding="Latin-1")  # open file, read-only raw data
o = open("mappedGooglePlayStore.csv", "w") # open file, write - just our key, value pairs

for line in f:                     #reads in file line by line
    
    data = line.strip().split(",")
    
    if len(data) == 12:      #confirms each line is the correct size
        app, category, rating, reviews, size, installs, appType, price, contentRating, genre, lastUpdate, currentVer = data   #takes in each value into data
        o.write("{0},{1}\n".format(category, reviews))    #writes to file category and review
        
f.close()
o.close()
