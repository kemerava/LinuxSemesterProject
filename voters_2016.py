import argparse
import pyspark
import re

sc = pyspark.SparkContext()

# takes the record from the file 2016 and splits into the record as
# name, count of medicine for 2016
def getNameCount(line):
    pattern = re.compile(r'[^a-zA-Z0-9]')
    fields = re.split(pattern, line)

    return fields[2], fields[5]

# filters if the name is in the records for the 2015
# and if the record for 2015 has a count (for Republicans)
def filterReps(line):
    name = line[0]
    count = line[1]
    if name in file_reps_2015:
        return True
    return False

# filters if the name is in the records for the 2015
# and if the record for 2015 has a count (for Dems)
def filterDems(line):
    name = line[0]
    count = line[1]
    if name in file_dems_2015:
        return True
    return False

# at the end we have name, number of medicine for 2016,
# number of medicine for 2015 (for Republicans)
def getRepublicans(line):
    name = line[0]
    count = line[1]
    # we are guaranteed that the name is already in the file_reps_2015,
    # but this the additional check 
    if name in file_reps_2015:
        try: count = int(count)
        except: count = 0
        try: rep_2015  = int(file_reps_2015[name])
        except: rep_2015 = 0
        return name,  count, rep_2015

# at the end we have name, number of medicine for 2016,
# number of medicine for 2015 (for Democrats)
def getDemocrats(line):
    name = line[0]
    count = line[1]
    # we are guaranteed that the name is already in the file_dems_2015,
    # but this the additional check 
    if name in file_dems_2015:
        #  number of medicine for 2016 should be the int
        try: count = int(count)
        except: count = 0
        # number of medicine for 2015 should be the int 
        try: dem_2015  = int(file_dems_2015[name])
        except: dem_2015 = 0
        return name, count, dem_2015
    
def main( state):

    # get the raw data for 2016 ->
    # refomat all records to name, count tuples
    text_file = sc.textFile(state+ "_2016_folder/part*").map(getNameCount)

    # filter only democrats ->
    # get tupes name, count_2016, count_2015 ->
    # save to file 
    democrats = text_file.filter(filterDems)\
                         .map(getDemocrats)\
                         .saveAsTextFile(state+"_REPUBLICANS")

    # filter only republicans ->
    # get tupes name, count_2016, count_2015 ->
    # save to file 
    republicans = text_file.filter(filterReps)\
                           .map(getRepublicans)\
                           .saveAsTextFile(state+"_DEMOCRATS")  

# take in the file for Democrats in 2015 and turn it into the dictionary 
def get_file_dems_2015(file_dems_2015, state):
    pattern = re.compile(r'[^a-zA-Z0-9]')
    # open file 
    file_dems_2015 = open(file_dems_2015, "rt")
    dems_2015 = {}
    for line in file_dems_2015:
        fields = re.split(pattern, line)
        # name: count 
        dems_2015[fields[2]] = fields[6]
    # close file
    file_dems_2015.close()

    return dems_2015

# take in the file for Republicans in 2015 and turn it into the dictionary 
def get_file_reps_2015(file_reps_2015, state):
    pattern = re.compile(r'[^a-zA-Z0-9]')
    file_reps_2015 = open(file_reps_2015, "rt")
    reps_2015 = {}
    for line in file_reps_2015:
        fields = re.split(pattern, line)
        # name: count 
        reps_2015[fields[2]] = fields[6]  
    file_reps_2015.close()

    return reps_2015

# add the parsing arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--state')
    return parser.parse_args()

# parse the --state argument
args = parse_args()
if args.state == "OH":
    state = "OH"
elif args.state == "OK":
    state = "OK"


# the files to get the data from 
file_dems_2015 = state + "_Democrats"
file_reps_2015 = state + "_Republicans"

# change these data files into the dictionaies
file_dems_2015 = get_file_dems_2015(file_dems_2015, state)
file_reps_2015 = get_file_reps_2015(file_reps_2015, state)


# this calls the main process 
main(state)
