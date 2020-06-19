import matplotlib.pyplot as plt
import csv
x=[]
y=[]
count=0
count1=0
count2=0
count3=0
fo=open("workbook.csv",'r')
plot=csv.reader(fo)
for row in plot:
    x.append(int(row[5]))
    count1=count1+1
    #y.append(int(row[220]))
#print (x)
list1=x
list2=y
print('TOTAL NO OF STUDENTS',count1)
print("MAXIMUM MARKS SCORED:",max(list1))

count=min(a for a in x if a > 0)
print("MINIMUM MARKS SCORED:",count)
for i in x:
            if(i<40):
                    count3=count3+1
print('NO OF STUDENT FAILED ',count3)

#count1=(a for a in x if a < 20)
#print("NO OF STUDENTS WITH NO POINTER(SGPA) :",count1)

#count3=list2.count(50)
#print ("NO OF STUDENTS WITH POINTER(SGPA):",count3)
