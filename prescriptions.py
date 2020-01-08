import gzip 
import pyspark

# set up the spark context
sc = pyspark.SparkContext()

# returns the data for every record, leaving only
# last name, first name, city, state, medicine, total day supply
# from the total record 
def getNameStateAntidepressant(line):
   # separate record 
   fields = line.split("\t")
   # if the record has the right formatting in the number of the fields,
   # get the needed fields, strip and use only the lower case
   if len(fields)>12:
      last_name = fields[1].lower().strip()
      first_name =  fields[2].lower().strip()
      city = fields[3].lower().strip()
      state = fields[4].lower().strip()
      medicine = fields[8].lower().strip()
      total_day_supply = fields[12].lower().strip()
   return last_name, first_name, city, state, medicine, total_day_supply

# if the record in the medicine name field of the record is not the antidepressant, then filter it out
def onlyAntidepressants(line):
   if line[4] in list_anti_depr:
      return True
   return False

# for every record get the distinct name
# and the count (which is the total supply of the medicine for the day)
def getNameAndCount(line):
   last_name, first_name, city, state, medicine, total_day_supply = line
   # make sure that the total day is an int, otherwise just assign a 0
   try: total_day_supply = int(total_day_supply)
   except: total_day_supply = 0
   # the distinc name is the cancatnation of the last, fist names and the city
   return (last_name + first_name + city), total_day_supply


# this is the main function with all the main transformations 
def get_doctors_from_OH_and_OK(file_name_in, file_OH, file_OK):

   # get the raw medicare data ->
   # get tupes (last_name, first_name, city, state, medicine, total_day_supply) ->
   # filter out only the records with the antidepressants 
   file_in = sc.textFile(file_name_in).map(getNameStateAntidepressant)\
                                      .filter(onlyAntidepressants)

   # get only the records that are from OH state ->
   # return tuples (distinct name, total day supply) ->
   # reduce by getting the sum of all the total day supplies for the distinct names ->
   # save in the OH foler 
   get_doctors_OH = file_in.filter(lambda x: x[3] == "oh").map(getNameAndCount)\
                    .reduceByKey(lambda x, y: int(x)+int(y)).saveAsTextFile(file_OH)

   # get only the records that are from OK state ->
   # return tuples (distinct name, total day supply) ->
   # reduce by getting the sum of all the total day supplies for the distinct names ->
   # save in the OK foler 
   get_doctors_OK = file_in.filter(lambda x: x[3] == "ok").map(getNameAndCount)\
                    .reduceByKey(lambda x, y: int(x)+int(y)).saveAsTextFile(file_OK)


# usning the file with all the antidepressants (taken from https://www.fda.gov/media/76700/download),
# fomat the lines and insert into the array that would be used to find out of the type of medicine
# from the medicare data is an antidepressant
def get_list_antidepressants():
   # open the file with antidepressant name
   antidep_file = open("antidepressants", "rt")
   antidepressants = []
   
   for antid in antidep_file:
      # if the file has 2 spaces at the end, strip them
      if (antid[-2]==" ") or (antid[-2:]=="\n"):
         antid = antid[:len(antid)-2]
      # if it has only one, strip only one character (other cases, just leave as is)
      else:
         antid = antid[:len(antid)-1]
      # remove any capital letters 
      antidepressants.append(antid.lower())
   # close file
   antidep_file.close()
   return antidepressants

# this is the resulting list of all the antidepressants 
list_anti_depr = get_list_antidepressants()

def main():
   # medicare data for 2015
   file_name_2015 = "PartD_Prescriber_PUF_NPI_Drug_2015.txt.gz"

   # pack the answens for the 2015 in these folders 
   file_2015_OH = "OH_2015_folder"
   file_2015_OK = "OK_2015_folder"

   # medicare date for 2016 
   file_name_2016 = "PartD_Prescriber_PUF_NPI_Drug_2016.txt.gz"

   # pack the answers for the 2016 in these folders 
   file_2016_OH = "OH_2016_folder"
   file_2016_OK = "OK_2016_folder"


   # call the fuunction for the 2015 data
   get_doctors_from_OH_and_OK(file_name_2015, file_2015_OH, file_2015_OK)

   # call the function for the 2016 data
   get_doctors_from_OH_and_OK(file_name_2016, file_2016_OH, file_2016_OK)

  
main()

