f = open("googleplaystore.txt", "r")  # open file, read-only raw data
o = open("mappedGooglePlayStore.txt", "w") # open file, write - just our key, value pairs

for line in f:                     #reads in file line by line
    
    data = line.strip().split("\t")
    
    if len(data) == 13:      #confirms each line is the correct size
        App, Category, Rating, Reviews, Size, Installs, Type, Price, Content_Rating, Genres, Last_Updated, Current_Ver, Android_Ver = data   #takes in each value into data
        o.write("{0}\t{1}\n".format(Category, Rating))    #writes to file category and review
        
f.close()
o.close()
