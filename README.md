# LinuxSemesterProject

Summary

Hypothesis: Doctors, whose political affiliation is Democratic party were more likely to proscribe more antidepressants in 2016 than in 2015, compared to their Republican colleagues, because of the election outcome of 2016 presidential elections. 


Sources: 
* Medicare prescriptions 2015 (in /data/raw/) -- to find out the number of prescriptions for the antidepressants for each doctor in Ohio and Oklahoma in 2015 (around 24 million records)
*	Medicare prescriptions 2016 (in /data/raw) -- to find out the number of prescriptions for the antidepressants for each doctor in Ohio and Oklahoma in 2016 (around 24 million records)
*	Ohio State Voter Files (in /data/raw/) -- to find out the political affiliation of the doctors who are prescribing the antidepressants (a few thousand records)
* Oklahoma State Voter Files (from http://oklavoters.com/download.html --  Data as of 5 December 2016) -- to find out the political affiliation of the doctors  who are prescribing the antidepressants (a few thousand records)
* List of all the antidepressants (from https://www.fda.gov/media/76700/download)


Outline of the project:
Using the script in prescriptions.py and the medicare data for 2015 and 2016 obtained 4 files with the doctors for Ohio and Oklahoma state for 2015 and 2016, who were prescribing the antidepressants, each of files containing the records with the distinct name of the doctor and the count of the medical prescriptions. Here distinct name is the concatenation of the last name, first name and the city and the  the count of the medical prescriptions is defined as the sum of all total day supply prescriptions prescribed by that doctor. Using the script voters_2015.py, the 2015 files that we obtained from the previous script and the data about the party affiliation for both states, we obtain files for both states and for both parties that have separately Republican and Democratic doctors distinct names and the number of prescribed medicine for 2015. Using script voters_2016.py, the 2016 files that we obtained in the first script were combined with the data that we got from the second script, obtaining the file for each state, that had the distinct name, number of medicine for 2016, number of medicine for 2015. Later this data was used to plot 2 scatter plots for Democratic (blue) and Republican party (red) with x-axis being 2015 and y-axis bring 2016. The bigger the angle was from x-axis the more medicine was prescribed in 2016 over  2015.

Conclusion and future research: 
The scatter plot that was obtained as a result of this study shows that the Democratic party doctors did prescribe more medicine in 2016 then 2015 compared to Republican doctors. Future research will involve investigation of the  data for 2017, that will give the more detailed information about weather or not the trend will continue.  



