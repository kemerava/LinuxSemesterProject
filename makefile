# all will build the whole project from the start or from the latest change
all:	histogram.pdf 
	echo "Everything has now been built"

# clean will clean all the files that were created in the process
# of building the project
clean: 
	rm histogram.pdf OK_Republicans OH_Republicans OK_Democrats OH_Democrats DEMOCRATS REPUBLICANS 
	rm -r OK_2016_folder OK_2015_folder OH_2016_folder OH_2015_folder OK_REP_folder OH_REP_folder OH_DEM_folder OK_DEM_folder OH_DEMOCRATS OK_DEMOCRATS OK_REPUBLICANS OH_REPUBLICANS


# the final file with the scatterplot, which reflects the results of the project
histogram.pdf: REPUBLICANS DEMOCRATS histogram.py 
	python3 histogram.py

# receiveing one file with all the Republican doctors for both states 
REPUBLICANS: OH_REPUBLICANS  OK_REPUBLICANS
	cat OH_REPUBLICANS/part* OK_REPUBLICANS/part* > REPUBLICANS

# recieving one file with all the Democratic doctors for both states 
DEMOCRATS: OH_DEMOCRATS  OK_DEMOCRATS
	cat OH_DEMOCRATS/part* OK_DEMOCRATS/part* > DEMOCRATS


# this creates a file of all the Republican (as well as Democratic) doctors from
# OH with their records as distinct name, amount of drugs for 2015,
# amount of drugs for 2016 
OH_REPUBLICANS: OH_2016_folder voters_2016.py OH_Democrats OH_Republicans
	spark-submit voters_2016.py --state OH

# depends on the above script 
OH_DEMOCRATS: OH_REPUBLICANS

# this creates a file of all the Republican (as well as Democratic) doctors from
# OK with their records as distinct name, amount of drugs for 2015,
# amount of drugs for 2016 
OK_REPUBLICANS: OK_2016_folder voters_2016.py OK_Democrats OK_Republicans
	spark-submit voters_2016.py --state OK

# depends on the above script 
OH_DEMOCRATS: OK_REPUBLICANS

# compile  all the files for the OH Democrats into one file
OH_Democrats: OH_DEM_folder 
	cat OH_DEM_folder/part-0000* > OH_Democrats

# compile  all the files for the Republicans into one file
OH_Republicans: OH_REP_folder
	cat OH_REP_folder/part-0000* > OH_Republicans

# compile  all the files for the OK Democrats into one file
OK_Democrats: OK_DEM_folder 
	cat OK_DEM_folder/part-0000* > OK_Democrats

# compile  all the files for the OK Republicans into one file
OK_Republicans: OK_REP_folder
	cat OK_REP_folder/part-0000* > OK_Republicans

# get the file for the OH Democrats and the record on the numbert of medicine
# the Democratic doctors from OH prescribed in 2015
OH_DEM_folder: OH_voter_file_1.gz OH_voter_file_2.gz OH_voter_file_3.gz OH_voter_file_4.gz voters_2015.py
	spark-submit voters_2015.py --state OH

# as a result of the script above this file is created for the OH Republicans
OH_REP_folder: OH_DEM_folder

# get the file for the OK Democrats and the record on the numbert of medicine
# the Democratic doctors from OK prescribed in 2015
OK_DEM_folder: OK_voter_file_1.csv OK_voter_file_2.csv OK_voter_file_3.csv OK_voter_file_4.csv voters_2015.py
	spark-submit voters_2015.py --state OK

# as a result of the script above this file is created for the OK Republicans
OK_REP_folder: OK_DEM_folder

# get the doctors for 2015 and 2016 and separately from OH and OK
# in 4 different folders
# (this one is the folder for OH 2015)
OH_2015_folder: prescriptions.py antidepressants PartD_Prescriber_PUF_NPI_Drug_2015.txt.gz  PartD_Prescriber_PUF_NPI_Drug_2016.txt.gz
	 spark-submit prescriptions.py

# produced by the pervious scrpt, folder for OH 2016 
OH_2016_folder: OH_2015_folder

# produced by the pervious script, folder for OK 2015
OK_2015_folder: OH_2015_folder 

# produced by the pervious script, folder for OH 2015
OK_2016_folder: OH_2015_folder


