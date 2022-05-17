import csv

raw=[]
#opening a csv file
file1=open('bm.csv','r')

#Reading a csv file
csvFile=csv.reader(file1)

for lines in csvFile:
    raw.append(lines)
file1.close()

file2=open('bm2.csv','w')
writer= csv.writer(file2)
writer.writerows(raw)
file2.close()