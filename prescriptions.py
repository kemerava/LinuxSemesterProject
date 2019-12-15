import gzip 

def main(file_name_in, file_name_out_OH, file_name_out_VH):

   file_in = gzip.open(file_name_in, "rt")

   file_out_OH = open(file_name_out_OH, "wt")
   file_out_VH = open(file_name_out_VH, "wt")

   antidep_file = open("antidepressants", "rt")
   antidepressants = []
   for antid in antidep_file:
      if antid[-2]==" ":
         antid = antid[:len(antid)-2]
      else:
         antid = antid[:len(antid)-1]
      antidepressants.append(antid.lower())
   
   line = file_in.readline()
   fields = line.split("\t")
   prev_name = fields[2].lower()+fields[3].lower()
   count = 0
   while line:

      fields = line.split("\t")
      if len(fields)>8:
         last_name = fields[2].lower()
         first_name =  fields[3].lower()
         state = fields[4].lower()
         antidepressant = fields[8].lower()
         name = last_name+first_name

         if name == prev_name:
            count += 1
         else:
            
            if antidepressant in antidepressants:
               if state == "oh":
                  print(last_name, first_name, count) #, file = file_out_OH 
               elif state == "vh":
                  print("VH:",last_name, first_name, count)#,  file = file_out_VH
            count = 0
            prev_name = name 
         line = file_in.readline()
   file_in.close()
   file_out_OH.close()
   file_out_VH.close()
   antidep_file.close()

         
    

file_name_2015 = "PartD_Prescriber_PUF_NPI_Drug_2015.txt.gz"
file_2015_OH = "OH_2015"
file_2015_VH = "VH_2015"
file_name_2016 = "PartD_Prescriber_PUF_NPI_Drug_2016.txt.gz"
file_2016_OH = "OH_2015"
file_2016_VH = "VH_2015"

main(file_name_2015, file_2015_OH, file_2015_VH)


