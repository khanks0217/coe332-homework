
import names

diffnames = []
i = 0 #counts the number of diff names

while i in range(5):
    tempname = names.get_full_name()
    #check if name is different
    if tempname not in diffnames:
        #print the name and its length
        print(tempname, len(tempname), sep = ', ')
        #add name to the list
        diffnames.append(tempname)
        i +=1
