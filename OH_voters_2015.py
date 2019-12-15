# this will take in a voter file at a time as a parameter and check it agains the doctors 
def main():

    ''' 1. this is the script for the third step  that processes the voter files. 
    It looks up the political affiliation of the doctors who prescribed antidepressants in 2015 
    (this is the one for OH. There will be the similar one for the VH)
    and  maps the political affiliation with the doctor and number of prescriptions
    2. prably will make sense to put the doctors into a dict 
    (doctor's name (last name concat. with first name): number of prescriptions), because there 
    will be relativelly small compared to the number of the people who voted 
    3. needs another step before this script to get all the names like uniq -c 
    4. next script after this one is donna go through the records for the 2016 and if the doc
    is mentioned here and in 2016 record put his name and the ratio in the other file 
    with all dems (same thing add there VH)'''
    
    file_doctors = open(file_doctors, "rt")
    file_political_affiliation = open(file_political_affiliation, "rt")
    file_dem = open("OH_DEM", "wt")
    file_rep = open("OH_REP", "wt")

    ## TODO: change this into the dictionary,
    ## for now just to see if this reads all the data properly use list
    doctor_records = file_doctors.readlines()
    voter = file_political_affiliation.readline()
    while voter:
        fields = voter.split(",")
        last_name = fields[3].lower()
        first_name = fields[4].lower()
        polit_aff = fields[10].lower()
        name = last_name+first_name
        if name in doctor_records:
            if polit_aff == "r":
                print ("Republican:", last_name, first_name) # this will have the number of prescriptions and the name of the doctor and will go to the appropriate file
            else:
                print ("Democrat:", last_name, first_name)
        voter = file_political_affiliation.readline()
        
    file_doctors.close()
    file_political_affiliation.close()
    file_dem.close()
    file_rep.close()
