import sys
import argparse
import pyspark
import re

sc = pyspark.SparkContext()

# this creates the dictionaly of the doctors    
def get_doctors(file_doctors):
    # open the file 
    file_doctors = open(file_doctors, "rt")
    # pattern is only numbers and letters
    pattern = re.compile(r'[^a-zA-Z0-9]')
    doctor_records = {}
    for line in file_doctors:
        # leave only the words or the numbers for every record 
        feilds = re.split(pattern, line)
        # set it up as name: medicine count
        doctor_records[feilds[2]] = feilds[5] 
    file_doctors.close()
    return doctor_records 
    

# returns the right formatting for the OH doctors
# as last, firt names, city and political affiliation
def nameAndPolitAffiliationOH(voter):
    fields = voter.split(",")
    last_name = fields[3][1:len(fields[3])-1].lower()
    first_name = fields[4][1:len(fields[4])-1].lower()
    polit_aff = fields[10][1:len(fields[10])-1].lower()
    city = fields[13][1:len(fields[13])-1].lower()
    return last_name, first_name, city, polit_aff

# returns the right formatting for the OK doctors
# as last, firt names, city and political affiliation
def nameAndPolitAffiliationOK(voter):   
    fields = voter.split(",")
    last_name = fields[1][1:len(fields[1])-1].lower()
    first_name = fields[2][1:len(fields[2])-1].lower()
    polit_aff = fields[6][1:len(fields[6])-1].lower()
    city = fields[13][1:len(fields[13])-1].lower()
    return last_name, first_name, city, polit_aff

# this returns a false if the distinct name is found in the list of doctors
def get_non_doctors(person):
    name = person[0]+person[1]+person[2]
    if  name in doctors_dict:
        return False
    else:
        return True

# this returns name, medicine count, political affiliation (as 1 letter)
def get_only_doctors(person):
    # name is the concatenation of the last, first names and the city 
    name = person[0]+person[1]+person[2]
    try:
        # doctors_dict[name] the count of the medicine for this person
        # person[3][0] is the first letter of the political affilation
        return name, doctors_dict[name], person[3][0]
    except:
        return "", 0, ""

def main_process(file_polit_aff,  state):

    # get the raw data 
    political_aff_file = sc.textFile(file_polit_aff)
    # choose the mapping function based on the state
    if state == "OH":
        mapping_function = nameAndPolitAffiliationOH
    elif state == "OK":
        mapping_function = nameAndPolitAffiliationOK
    
    # returns the tuples with last and first name,
    # city and political affiliation
    name_polit_affil = political_aff_file.map(mapping_function)

    # filters out the records of the doctors 
    non_doctors = name_polit_affil.filter(get_non_doctors)

    # get the doctors by substracting the nondoctors from all records ->
    # fomat the doctors records as name, medicine count, political affiliation
    only_doctors =  name_polit_affil.subtract(non_doctors)\
                        .map(get_only_doctors)

    # filer only Republican doctors ->
    # get distinct names just in case some records are repeated ->
    # save as the file for republican 
    rep_doctors = only_doctors.filter(lambda x: x[2] == 'r').distinct()\
                .map(lambda x: (x[0], x[1]))\
                .saveAsTextFile(state+"_REP_folder")

    # filer only Democratic doctors ->
    # get distinct names just in case some records are repeated ->
    # save as the file for Democrat 
    dem_doctors = only_doctors.filter(lambda x: x[2] == 'd').distinct()\
                .map(lambda x: (x[0], x[1]))\
                .saveAsTextFile(state+"_DEM_folder")  


# argument parser
parser = argparse.ArgumentParser(description='Choosing a state.')

# setting up the arguments 
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--state')
    return parser.parse_args()

# parse the arguments of the command
# if --state OH: then prosess the OH file and get the data about OH
# else if --state OK: then do the same for OK
args = parse_args()
if args.state == "OH":
    state = "OH"
elif args.state == "OK":
    state = "OK"
doctor_file = state + "_2015_folder/part-00000"


# if we are processing info about OH, OH_voter_file_*.gz are the files
# with the info on the voters in the state
if state == "OH":
    file_in = "OH_voter_file_*.gz"

elif state == "OK":
    file_in = "OK_voter_file_*.csv"
# returns the list of all the doctors for the given state for 2015 year
doctors_dict = get_doctors(doctor_file)

main_process(file_in, state)
