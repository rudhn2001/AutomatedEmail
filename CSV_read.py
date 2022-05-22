import csv
import re
#opening a csv file
file=open('Book1.csv','r')
file2= open('Valid_Mail.csv','w')
#Reading a csv file
csvFile=csv.DictReader(file)
writer= csv.writer(file2)
email=[]
#display the output

for lines in csvFile: 
    print(lines)
    email.append(lines)
writer.writerow(email)
print("Written in file")
    
    # header = ['name', 'area', 'country_code2', 'country_code3']
# data = ['Afghanistan', 652090, 'AF', 'AFG']
#opening/creating a file

    
    
    # #writing the data into file
    # writer.writerow(header)
    
    
file.close()
file2.close()