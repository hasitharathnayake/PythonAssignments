#program to read through the mbox-short.txt and figure out who has
#sent the greatest number of mail messages.
senders=dict()
#file_name = input("Enter file name:")
file_name="mbox-short.txt"
handle = open(file_name)
for lines in handle:
    phrase_list=lines.split()
    if 'From' in phrase_list:
        key=phrase_list[1]
        senders[key]=senders.get(key,0)+1
v_max=0
email_of_max=''
for k,v in senders.items():
    #print(k,v)#debug line
    if v>=v_max:
        v_max=v
        email_of_max=k

print(email_of_max,v_max)
