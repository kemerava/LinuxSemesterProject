import matplotlib.pyplot as plt
import numpy as np
import re

#f = plt.figure()
file_dems = open("DEMOCRATS", "rt")
file_reps = open("REPUBLICANS", "rt")
#ax1 = plt.axes([0.1, 0.1, 0.5, 1])
#ax2 = plt.axes([0.1, 0.5, 0.5, 1])
f, (ax1, ax2) = plt.subplots(1, 2, sharey = True, sharex = True)
f.suptitle("Comparing the Democratic and Republican parties")
x1 = []
y1 = []
x2 = []
y2 = []
for line in file_dems:
    pattern = re.compile(r'[^a-zA-Z0-9]')
    fields = re.split(pattern, line)
    x1.append(int(fields[5]))
    y1.append(int(fields[7]))

    

for line in file_reps:
    pattern = re.compile(r'[^a-zA-Z0-9]')
    fields = re.split(pattern, line)
    
    x2.append(int(fields[5]))
    y2.append(int(fields[7]))
    
#plt.scatter(x1, y1, color = "blue", alpha = 0.2,label = "Democratic Party")

ax1.scatter(x1, y1, color = "blue", alpha = 0.5,label = "Democratic Party")
ax2.scatter(x2, y2, color = "red", alpha = 0.5, label = "Republican Party")

plt.ylabel("2016")
plt.xlabel("2015")
plt.title('Prescribed antidepressants in 2016 and 2015 by Republican and Democratic doctors') 
ax1.set_title("Democratic Party")
ax2.set_title("Republican Party")
#plt.show()
#print (democrats)
#print(republicans)

f.savefig("histogram.pdf")
