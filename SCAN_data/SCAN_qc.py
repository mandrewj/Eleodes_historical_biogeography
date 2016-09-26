#This script does basic quality control pruning on SCAN occurrence data.
#Filters out records with Basis of Record NOT 'PreservedSpecimen'
#Filters out records without decimal lat/long data
#Filters out records with uncertainty >= 1000 meters
#Filters out records with no entry in the 'Locality' field
#output is placed in the file 'occurrences_qc.txt'


infile="occurrences.txt"
outfile="occurrences_qc.txt"

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

    
with open(infile, "r", encoding="utf-8") as infile:
    with open(outfile, "w", encoding="utf-8") as outfile:
        #
        outfile.write(infile.readline())
        #
        for line in infile:
            elem=line.split("\t")
            if (elem[3]=="PreservedSpecimen") and (elem[62] != "") and (elem[63] != "") and (elem[58] != ""):
                if isfloat(elem[65]):
                    if eval(elem[65]) < 1000:
                            outfile.write(line)
                else:
                    outfile.write(line)
        #

