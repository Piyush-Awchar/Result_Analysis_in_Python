import matplotlib.pyplot as plt
import csv
import numpy as np
min1=[]
max1=[]
fail=[]

for col in range(5,55,12):
    x=[]
    y=[]
    count=0
    count1=0
    count2=0
    count3=0
    fo=open("B.csv",'r')
    plot=csv.reader(fo)
    for row in plot:
        x.append(int(row[col]))
        count1=count1+1
        #y.append(int(row[220]))
    #print (x)
    list1=x
    list2=y
    print('TOTAL NO OF STUDENTS',count1)
    print("MAXIMUM MARKS SCORED:",max(list1))
    max1.append(int(max(list1)))
    print (max1)
    count=min(a for a in x if a > 0)
    print("MINIMUM MARKS SCORED:",count)
    min1.append(int(count))
    print (min1)
    for i in x:
                if(i<40):
                        count3=count3+1
    print('NO OF STUDENT FAILED ',count3)
    fail.append(int(count3))
    print (fail)

min1 = list(np.around(np.array(min1),2))
max1 = list(np.around(np.array(max1),2))
fail = list(np.around(np.array(fail),2))

subjects=['DM', 'DELD', 'DSA', 'COA', 'OOP']
legends=['MAXIMUM','MINIMUM','FAILED']
list3=np.arange(len(subjects))
barsticks=plt.bar(list3,max1,align='center',alpha=1,width=0.27)
for rect in barsticks:
	height=rect.get_height()
	plt.text(rect.get_x()+rect.get_width()/2,height,'%d'% int(height),ha='center')
barsticks=plt.bar(list3+0.27,min1,align='center',alpha=1,width=0.27)
for rect in barsticks:
	height=rect.get_height()
	plt.text(rect.get_x()+rect.get_width()/2,height,'%d'% int(height),ha='center')
barsticks=plt.bar(list3+0.54,fail,align='center',alpha=1,width=0.27)
for rect in barsticks:
	height=rect.get_height()
	plt.text(rect.get_x()+rect.get_width()/2,height,'%d'% int(height),ha='center')

plt.legend(legends)
plt.xticks(list3,subjects,ha='left')
plt.tight_layout()
plt.title('Max marks, Min marks and Failed Percentage of students(Div-B)')
plt.xlabel('Subjects')
plt.ylabel('Marks in percentage(APPROX)')
plt.show()


    #count1=(a for a in x if a < 20)
    #print("NO OF STUDENTS WITH NO POINTER(SGPA) :",count1)

    #count3=list2.count(50)
    #print ("NO OF STUDENTS WITH POINTER(SGPA):",count3)

