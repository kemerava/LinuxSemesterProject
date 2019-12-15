all:	histogram.pdf 
	echo "Everything has now been built"

clean: histogram.pdf OH_2015 OH_2016 VH_2015 VH_2016
	rm histogram.pdf OH_2015 OH_2016 VH_2015 VH_2016

histogram.pdf:	taggedRecords buildHisto.awk 
	gawk -f buildHisto.awk <taggedRecords >tagHistogram
	rm temp.text

OH_2015: prescriptions.py antidepressants PartD_Prescriber_PUF_NPI_Drug_2015.txt.gz
	python3 prescriptions.py
OH_2016: prescriptions.py antidepressants PartD_Prescriber_PUF_NPI_Drug_2016.txt.gz  
	python3 prescriptions.py
VH_2015: prescriptions.py antidepressants PartD_Prescriber_PUF_NPI_Drug_2015.txt.gz 
	python3 prescriptions.py
VH_2016: prescriptions.py antidepressants PartD_Prescriber_PUF_NPI_Drug_2016.txt.gz  
	python3 prescriptions.py

