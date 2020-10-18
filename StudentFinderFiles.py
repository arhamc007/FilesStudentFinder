#Creates a file and prompts the user to input their details
fh = open("student.txt", "w+")
totstu=int(input("Please enter the total no. of students "))
for c in range (totstu):
    formatc = False
    while not (formatc):
        StudentID=input("Please enter the ID in the format of 2 letters followed by 4 numbers ")
        if StudentID[:2].isalpha() and StudentID[2:].isdigit():
            formatc = True
        else:
            print("Format is incorrect. Please re-enter ")
    Email=input("Please enter the email ")
    details= StudentID + "#" + Email
    fh.write(details + "\n")
fh.close()
#Searches for a given Student ID
fh = open("student.txt", "r")
search = input("Please enter your StudentID ")
b=fh.readline()
found = 0 
while b != "":
    details= b.split("#")
    if details[0]==search:
        print("Email Address is " + details[1])
        found=1
    b=fh.readline()
    if found==0:
        print("ID not found")
fh.close()
#Searches for Student IDs starting with a particular letter(s) 
fh = open("student.txt", "r")
search = input("Please enter your StudentID letters ")
b=fh.readline()
while b != "":
    details=b.split("#")
    if details[0].startswith(search):
        print(details[0]+" "+details[1])
    else:
        print("Not found ")
    b=fh.readline()
fh.close()
#to add additional students 
fh = open("student.txt", "a")
totstu=int(input("Please enter the total no. of students "))
for c in range (totstu):
    formatc = False
    while not (formatc):
        StudentID=input("Please enter the ID in the format of 2 letters followed by 4 numbers ")
        if StudentID[:2].isalpha() and StudentID[2:].isdigit():
            formatc = True
        else:
            print("Format is incorrect. Please re-enter ")
    Email=input("Please enter the email ")
    details= StudentID + "#" + Email
    fh.write(details + "\n")
fh.close()
#storing different information on different lines and modifying the above code
fh = open("student.txt", "w+")
totstu=int(input("Please enter the total no. of students "))
for c in range (totstu):
    formatc = False
    while not (formatc):
        StudentID=input("Please enter the ID in the format of 2 letters followed by 4 numbers ")
        if StudentID[:2].isalpha() and StudentID[2:].isdigit():
            formatc = True
        else:
            print("Format is incorrect. Please re-enter ")
    fh.write(StudentID)
    fh.write("\n")
    Email=input("Please enter the email ")
    fh.write(Email)
    fh.write("\n")
    Address=input("Please enter the address ")
    fh.write(Address)
    fh.write("\n")
    Tutor=input("Please enter the tutor's name ")
    fh.write(Tutor)
    fh.write("\n")
fh.close()

fh = open("student.txt", "r")
search = input("Please enter your StudentID ")
b=fh.readline()
found = 0 
while b != "":
    stid=b
    if stid.strip()==search:
        ed=fh.readline()
        print("Email Address is " ,ed)
        found=1
    b=fh.readline()
if found==0:
    print("ID not found")
fh.close()

fh = open("student.txt", "r")
search = input("Please enter your StudentID letters ")
b=fh.readline()
flag=0
while b != "":
    stid=b
    st=stid.strip()
    if st.startswith(search):
        flag=1
        ed=fh.readline()
        print("email:",ed)
        ed=fh.readline()
        print("add:",ed)
        ed=fh.readline()
        print("tutor:",ed)
    b=fh.readline()
if flag==0:
     print("Not found ")
fh.close()


    

        


    
