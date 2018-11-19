f = open("googleplaystore.csv",encoding="Latin-1")  # open file, read-only raw data
o = open("mappedGooglePlayStore.csv", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split(",") 
    if len(data) == 12:
        app, category, rating, reviews, size, installs, appType, price, contentRating, genre, lastUpdate, currentVer = data
        o.write("{0},{1}\n".format(category, reviews))
f.close()
o.close()
