import matplotlib.pyplot as plt
import csv
x=[]
y=[]
count1=0
fo=open("workbook.csv",'r')
plot=csv.reader(fo)
for row in plot:
        x.append(row[9])
        count1=count1+1
        
        y.append(row[5])
list0=x
list1=y
count=list0.count('FF')
count2=list1.count('0')
count3=count1-count2 
failed=count
total_student=count1
total_student_attemped=count3
absent_student=count2


calculation=count3-(count-count2)

percentage=(calculation/count3)*100



print("Total no of Students")
print (count1)
print("Total no of ABSENT student")
print(count2)
print("No of students ATTEMPED subject")
print(count3)
#print (x)
print("Total no of Students FAILED")
print (count-count2)
print("Total RESULT")
print(percentage,"%")
