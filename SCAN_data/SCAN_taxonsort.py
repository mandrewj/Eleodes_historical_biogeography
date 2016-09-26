#!/usr/bin/python3

#This script parses a list of occurences into individual species data files
#This script requires the file taxonsort.txt to be in the same directory
#Each line on taxonsort.txt is formatted as:
#outputname|name1|name2|name3|etc...
#Files are placed in the data_output/ subfolder
#outputname_records.txt contains the full record entries for manual verification
#outputname_LatLong.txt contains only lat/long data for input to PROXIMITY

import os, sys

taxonsort="taxonsort.txt"
#infile="occurrences_qc.txt"


if not os.path.exists('data_output'):
    os.mkdir('data_output')

taxa=[]

with open(taxonsort,"r", encoding="utf-8") as taxonsort:
    for line in taxonsort:
        elem=line.strip().split("|")
        taxa.append(elem)

for taxon in taxa:
    outfile="data_output/"+taxon[0]+"_records.txt"
    gps=[]
    with open("occurrences_qc.txt","r",encoding="utf-8") as infile:
        with open(outfile, "w", encoding="utf-8") as outfile:
            outfile.write(infile.readline())
            for line in infile:
                elem=line.split("\t")
                if elem[12] in taxon:
                    outfile.write(line)
                    gps.append(str(elem[62])+","+str(elem[63]))
    outfile2="data_output/"+taxon[0]+"_LatLong.txt"
    infile.close()
    with open(outfile2, "w",encoding="utf-8") as outfile2:
        for record in gps:
            outfile2.write(record+"\n")
                    
            



