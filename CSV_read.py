import csv

#opening a csv file
file=open('BULKEMAIL.csv','r')

#Reading a csv file
csvFile=csv.reader(file)

#display the output
for lines in csvFile: 
    print(lines)