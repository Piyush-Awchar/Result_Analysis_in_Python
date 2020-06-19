import matplotlib.pyplot as plt
import csv
import numpy as np
x=[]
fo=open("B.csv",'r')
plot=csv.reader(fo)
for row in plot:
        x.append(row[167])
list1=x
list2=[]
count=list1.count('O')
count1=list1.count('A+')
count2=list1.count('A')
count3=list1.count('B+')                 
count4=list1.count('B')                 
count5=list1.count('C')
count6=list1.count('P')                 
count7=list1.count('F')
print(count,count1,count2,count3,count4,count5,count6,count7)
list2=[count,count1,count2,count3,count4,count5,count6,count7]
grades=['O','A+','A','B+','B','C','P','F']
list3=np.arange(len(grades))
barsticks=plt.bar(list3,list2,align='center',alpha=1,color='g''b''y''m''c''r''k''b')

for rect in barsticks:
	height=rect.get_height()
	plt.text(rect.get_x()+rect.get_width()/2,height,'%d'% int(height),ha='center')
	

plt.legend(barsticks[:8],grades)
plt.xticks(list3,grades)
plt.tight_layout()
plt.title('Visualization Of Grades Obtained in Principles of Programming Language(Div-B)')
plt.xlabel('GRADES')
plt.ylabel('NO OF STUDENTS')
plt.show()
