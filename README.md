# LinuxSemesterProject
Hypothesis: Doctors, whose political affiliation is Democratic party were more likely to proscribe more antidepressants in 2016 than in 2015, compared to their Republican colleagues, because of the election outcome of 2016 presidential elections. 




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
