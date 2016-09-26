Historical Biogeographic Reconstruction of Eleodes of Arizona by Plant Communities

This represents the work behind a presentation given at the International Congress of Entomology in Orlando, FL on 26 Sept 2016.

The pipeline and scripts given here are intended to take a downloaded tab-delimited file from SCAN (Symbiota Collections of Arthropods Network) and to process those specimen data.  The filtered and sorted data are then used in the CORRELATION software to associate each species with a computed plant community.  Then historical community associations are inferred across a phylogeny using BioGeoBEARS.

The 'SCAN_data' folder contains an analysis pipeline shell script which calls each of the given python scripts to act on the downloaded occurrences.txt file from SCAN.  The output are files of lat/long coordinates for each species.

The 'CORRELATION' folder contains the results of using http://pinkava.asu.edu/Correlation/Correlate.php on each of those files.

The 'BIOGEOBEARS' folder contains the R script, phylogeny, and coded distribution file needed to infer the historical community shifts.
