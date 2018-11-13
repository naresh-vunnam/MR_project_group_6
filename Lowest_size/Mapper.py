f = open("d.txt","r")  # open file, read-only raw data
o = open("o.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split("    ") 
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        o.write("{0}\t{1}\n".format(store, cost))
f.close()
o.close()




