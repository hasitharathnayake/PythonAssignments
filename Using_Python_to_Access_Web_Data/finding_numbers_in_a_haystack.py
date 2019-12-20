#The basic outline of this problem is to read the file, look for integers using
#the re.findall(), looking for a regular expression of '[0-9]+' and then
#converting the extracted strings to integers and summing up the integers.
import re
intl=list()

fname=input("Please enter the file name: ")
if len(fname)<1:#for ease of testing
    fname="regex_sum_42.txt"

#using a regex [0-9]+ isolates numbers in a line
fhandle=open(fname)
for lines in fhandle:
    if re.search('[0-9]+',lines):
        nums=re.findall('[0-9]+',lines)
        for num in nums:
            i=int(num)
            intl.append(num)

print(intl)
print(sum(intl))
