
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
    
import sys
def main(file_doctors): #file_political_affiliation, file_doctors


    
    file_doctors = open(file_doctors, "rt")
    file_political_affiliation = sys.stdin
    file_dem = open("OH_DEM", "wt")
    file_rep = open("OH_REP", "wt")

    doctor_records = {}
    for line in file_doctors:
        feilds = line.split()
        doctor_records[feilds[0]+feilds[1]] = feilds[2]
        
    voter = file_political_affiliation.readline()
    while voter:
        fields = voter.split(",")
        last_name = fields[3][1:len(fields[3])-1].lower()
        first_name = fields[4][1:len(fields[4])-1].lower()
        polit_aff = fields[10][1:len(fields[10])-1].lower()
        name = last_name+first_name

        if name in doctor_records:
           
            if polit_aff == "r":
                print (last_name, first_name, file=  file_rep )
            elif polit_aff == "d":
                print (last_name, first_name,  file = file_dem)
        voter = file_political_affiliation.readline()
        
    file_doctors.close()
    file_political_affiliation.close()
    file_dem.close()
    file_rep.close()
    
doctor_file = "OH_2015"
main(doctor_file)
