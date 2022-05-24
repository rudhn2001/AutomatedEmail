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

    # for line in csvFile:
    #     Email_list.append(line)
    # print("Emails are: ")
    # print(Email_list)
    # #for validating the email and storing in another file
    # for email in Email_list:
    #     type(email)     
    #     if (Email_Validate(email)==1):
    #         writer.writerows(email)
    #     else:
    #         continue
    # print("A file named Valid_Mail.csv has been created to store valid emails")