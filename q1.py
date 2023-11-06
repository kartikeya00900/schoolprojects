num=int(input("Enter Number Of Students: "))
l={}
for i in range(num):
    roll_n=int(input("Enter Your Roll Number: "))
    name=input("Enter Your Name: ")
    marks=float(input("Enter Your Marks: "))
    l[roll_n]=[name,marks]
for i in l:
    if l[i][1]>75:
      print("Name:",l[i][0],"Marks:",l[i][1])
    else:
       print("No Name")