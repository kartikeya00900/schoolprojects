print("Salary Program")
name=input("Enter Name Of Employee: ")
salary=float(input("Enter Basic Salary: "))
da=(25/100*salary)
hra=(15/100*salary)
pf=(12/100*salary)
ta=(7.5/100*salary)
net_pay=(salary+da+hra+ta)
gross_pay=net_pay-ta
print("\n")
print("Salary Detailed Breakup")
print("Name Of Employee: ",name)
print("Dearness Allow: ",da)
print("House Rent: ",hra)
print("Travel Allow: ",ta)
print("Net Salary Pay: ",net_pay)
print("Provident Fund: ",pf)
print("Gross Payment: ",gross_pay)

