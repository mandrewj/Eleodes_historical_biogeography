#Takes QC'd SCAN occurrences - counts number of collections represented
#Outputs the collections' information and # of records
#Output in 'CollCount_qc.txt'

infile="occurrences_qc.txt"
outfile="CollCount_qc.txt"
with open(infile, "r", encoding="utf-8") as infile:
    with open(outfile, "w", encoding="utf-8") as outfile:

        coll=[]
        inst=[]
        number=[]
        for line in infile:
            elem=line.split("\t")
            if elem[2] in coll:
                number[coll.index(elem[2])]+=1
            else:
                coll.append(elem[2])
                inst.append(elem[1])
                number.append(1)





        #
        for item in coll:
            outfile.write(inst[coll.index(item)] + "\t" + item +"\t" + str(number[coll.index(item)])+"\n")
