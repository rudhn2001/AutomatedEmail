import csv

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']
#opening/creating a file
with open('BULKMAIL.csv','w') as file:
    writer= csv.writer(file)
    
    #writing the data into file
    writer.writerow(header)
    writer.writerow(data)
    
    file.close()