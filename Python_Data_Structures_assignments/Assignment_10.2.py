#program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
keyword='From'
c_hour=dict()
for lin in handle:
    words=lin.split()
    #print(words)#debugging
    if keyword in words:
        #print(words[5])
        date=words[5].split(':')
        hour=date[0]
        c_hour[hour]=c_hour.get(hour,0)+1
#print(c_hour)#debugging
#print(c_hour.items())#debugging
temp=list()
for k,v in c_hour.items():#iterate the tuples inside list
    temp.append((k,v))#append the values of k and v to temp list

temp=sorted(temp)#sort the temp list (of tuples)
for i,j in temp:#iterate through the temp list and print the value pairs
    print(i,j)
