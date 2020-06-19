import matplotlib.pyplot as plt
import numpy as np
import csv
ol=[]
th=[]
count1=0
count2=0
#count3=0
#count4=0
output1=[]
output2=[]
per1=[]
per2=[]
global  percentage1
global  percentage2

def wow(count1,count3,count4):
        percentage1=(count3/count1)*100
        print("TOTAL PERCENTAGE OL",percentage1,"%")
        per1.append(percentage1)
        percentage2=(count4/count1)*100
        print("TOTAL PERCENTAGE TH",percentage2,"%")
        per2.append(percentage2)
        return percentage1,percentage2
for col in range(3,60,12):
        cols=col+1
        ol=[]
        th=[]
        fo=open("B.csv",'r')
        plot=csv.reader(fo)
        count1=0
        count3=0
        count4=0
        
        for row in plot:
                ol.append(int(row[col]))
                th.append(int(row[cols]))
                count1=count1+1     
        for i in ol:
                if(i<20):
                        count3=count3+1
        print(count3)
        for j in th:
                if(j<20):
                        count4=count4+1
        print(count4)
        output1.append(wow(count1,count3,count4))
        #output2.append(wow(count1,count3,count4))        
print(per1)
print(per2)
#print(output1)
#print(output2)


#works to display only 2 digits after decimal
per1 = list(np.around(np.array(per1),2))
per2 = list(np.around(np.array(per2),2))


subjects=['DM', 'DELD', 'DSA', 'COA', 'OOP']
legends=['ONLINE','THEORY']
list3=np.arange(len(subjects))
barsticks=plt.bar(list3,per1,align='center',alpha=1,width=0.27)
for rect in barsticks:
	height=rect.get_height()
	plt.text(rect.get_x()+rect.get_width()/2,height,'%d'% int(height),ha='center')
barsticks=plt.bar(list3+0.27,per2,align='center',alpha=1,width=0.27)
for rect in barsticks:
	height=rect.get_height()
	plt.text(rect.get_x()+rect.get_width()/2,height,'%d'% int(height),ha='center')


plt.legend(legends)
plt.xticks(list3,subjects,ha='left')
plt.tight_layout()
plt.title('Visualization of Failed Percentage(Div-B)')
plt.xlabel('Subjects(ONLINE VS THEORY EXAM)')
plt.ylabel('Marks in percentage(APPROX)')
plt.show()
