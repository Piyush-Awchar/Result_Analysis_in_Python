import matplotlib.pyplot as plt
import csv
x=[]
y=[]
count=0
count2=0
fo=open("workbook.csv",'r')
plot=csv.reader(fo)
for row in plot:
    x.append(float(row[207]))
    y.append(int(row[208]))
#print (x)
list1=x
list2=y
print("MAXIMUM SCORED POINTER(SGPA) :",max(list1))

count=min(a for a in x if a > 0)
print("MINIMUM SCORED POINTER(SGPA) :",count)


count1=list1.count(0)
print("NO OF STUDENTS WITH NO POINTER(SGPA) :",count1)

count3=list2.count(50)
print ("NO OF STUDENTS WITH POINTER(SGPA):",count3)
