import sys
f=open(sys.argv[1],"r")
list1=f.read().splitlines()
f.close()
dict1={}
for i in list1:
    person,school = i.split(":")
    dict1[person]=str(school)
    
for student in sys.argv[2].split(","):
    try:
        print("Name : {} , University : {}".format(student,dict1[student]))
    except:
        print("No record of {} was found!".format(student))
    