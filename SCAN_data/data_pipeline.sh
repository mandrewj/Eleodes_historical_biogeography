#!/bin/bash

printf "\n\n\n### SCAN to PROXIMITY Data Pipeline, September 2016, Andrew Johnston ###\n\n\n\n"
printf "This script assumes 'python3' is installed\n"
printf "assuming tab-delimited symbiota 'occurrences.txt' exists in this folder.\n"
printf "Note: Line counts include the single header line of each file\n\n"


printf "Lines in occurrences.txt:\n"
wc -l occurrences.txt

printf "\n\nCalling SCAN_qc.py for basic quality control...\n"
python3 SCAN_qc.py

printf "Lines in occurrences_qc.txt:\n"
wc -l occurrences_qc.txt

printf "\n\nCounting names and collections in QCd data....\n"
python3 SCAN_collcount.py
printf "Collections printed to CollCount_qc.txt\n"
wc -l CollCount_qc.txt

python3 SCAN_NameCount.py
printf "Names printed to NameCount_qc.txt\n"
wc -l NameCount_qc.txt


printf "\n\nSorting taxa defined in taxonsort.txt ...\n"
python3 SCAN_taxonsort.py

printf "Data files from data_output/ :\n"
wc -l data_output/*_records.txt


printf "\n\nData files taxon_LatLong.txt can be copied straight into PROXIMITY at:\n"
printf "http://pinkava.asu.edu/Correlation/ \n"
printf "Records for each taxon can be reviewed in the taxon_records.txt file\n\nEmail: ajohnston@asu.edu if this doesn't work!\nOr better yet if it does!\n\n\n"

