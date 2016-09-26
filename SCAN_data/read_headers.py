#For specified tab-delimited infile
#print (to standard output) the python index for each column

infile="occurrences.txt"

with open(infile, "r", encoding="utf-8") as infile:
    line1=infile.readline()
    elem=line1.split("\t")
    for item in elem:
        print(str(elem.index(item))+"\t"+str(item))
