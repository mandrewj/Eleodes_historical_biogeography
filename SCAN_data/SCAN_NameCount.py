#Takes QC'd SCAN occurences - count by "ScientificName"
#outputs sci name, #, Higher classification
#output in file 'NameCount_qc.txt'

infile="occurrences_qc.txt"
outfile="NameCount_qc.txt"
with open(infile, "r", encoding="utf-8") as infile:
    with open(outfile, "w", encoding="utf-8") as outfile:

        taxa=[]
        number=[]
        taxafull=[]
        for line in infile:
            elem=line.split("\t")
            if elem[12] in taxa:
                number[taxa.index(elem[12])]+=1
            else:
                taxa.append(elem[12])
                number.append(1)
                taxafull.append(elem[13]+"\t"+elem[11]+"\t"+elem[14]+"\t"+elem[15])
 




        #
        for item in taxa:
            n=taxa.index(item)
            outfile.write(str(number[n]) +"\t" + item + "\t" + taxafull[n] + "\n")

