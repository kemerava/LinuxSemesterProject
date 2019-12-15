def main():

    ''' here if the doctor is in the 2016 record, check if they are in the 
    previously created list of doctors with political affiliation and count 
    and if they are, then add them to the total list of Democrats or Republicans
    with the count ''' 
    file_doctors_2016 = open(file_doctors_2016, "rt")
    file_dems_2015 = open(file_dems_2015, "rt")
    file_reps_2015 = open(file_reps_2015, "rt")
    file_dem = open("DEMOCRATS", "wt")
    file_rep = open("REPUBLICANS", "wt")

    # this will be the the dictionary of all the docs from 2015 key:data == doctor_name: number of medicine
    2015_dems = file_dems_2015.readlines()
    2015_reps = file_reps_2015.readlines()
    doctor = file_doctors_2016.readline()
    while doctor:
        fields = doctor.split(" ")
        name = files[0]
        num_antidep = fields[1]
        if name in 2015_dems:
           print(name, 2015_dems[name]/num_antidep) # this will go into combined DEMOCRATS file  
        elif name in 2015_reps:
           print(name, 2015_reps[name]/num_antidep) # this will go into combined REPUBLICANS file  
        
    file_doctors_2016.close()
    file_dems_2015.close()
    file_reps_2015.close()
    file_dem.close()
    file_rep.close()


