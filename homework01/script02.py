
import names

i = 0 #i counts names of length 8

while i in range(5):
    #Generate a name and store in in tempname
    tempname = names.get_full_name()
    #Check if tempname is 9 characters, including the space
    if len(tempname) == 9:
        print(tempname)
        #increase name count
        i +=1
