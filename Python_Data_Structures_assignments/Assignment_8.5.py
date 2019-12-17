#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#You will parse the From line using split() and print out the second word in the line
#(i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

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
    if 'From' in words:
        email=words[1:2]
        #if email in email_list: continue #optional redundant value elimination
        email_list.append(email)
        count=count+1
#email_list.sort()#optional alphabetical ordering of emails
for i in range(len(email_list)):
    print(str(email_list[i]).strip('[\']'))#we convert the list elements into
    #strings and strip [] and '' from both sides
print("There were",count,"lines in the file with From as the first word")
