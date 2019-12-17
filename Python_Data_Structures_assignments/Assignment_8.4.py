file_name=input('Enter file name:') #ask user for file name

file_path=open(file_name)#open the file name input given by the user
list=list()#create a empty list

for lines in file_path:#iterate over the lines in the file
    words=lines.split()#split the line using spaces and store them in list
    for i in words:#iterate the list created for each element
        if i in list:continue#continue to loop if current element is in the list
        list.append(i)#else add the unique element to the list

list.sort()#sort the list alphabetically
print(list)
