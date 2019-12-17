#This program finds the keyword 'From' and then strips out email addresses from a textfile.

file_name=input("Enter File Name/Full Path: ")
try:
    file_handle=open(file_name)
except:
    print("Please enter a valid file name!")
    exit(1)
count=0
email_list=list()
for line in file_handle:
    words=line.split()
    if 'From' in words:#look for "the string 'From' in the list words
        email=words[1:2]
        #if email in email_list: continue #optional redundant value elimination
        email_list.append(email)
        count=count+1
#email_list.sort()#optional alphabetical ordering of emails
for i in range(len(email_list)):
    print(str(email_list[i]).strip('[\']'))#we convert the list elements into
    #strings and strip [] and '' from both sides
print("There were",count,"lines in the file with From as the first word")
