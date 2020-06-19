import matplotlib.pyplot as plt
import numpy as np
import csv
output=[]
x=[]
y=[]
count1=0
global  percentage
def wow(x,y,count1):
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
    print('*********************')
    return percentage

for col in range(9,60,12):
    cols=col-4
    x=[]    
    y=[]
    fo=open("B.csv",'r')
    plot=csv.reader(fo)
    count1=0
    for row in plot:
        x.append(row[col])
        y.append(row[cols])
        count1=count1+1
    #fo.close()
    #print (col)
    #print (cols)    
    output.append(wow(x,y,count1))
print(output)
    #print ('**************************************************************')





#works to display only 2 digits after decimal
output = list(np.around(np.array(output),2))

# Data to plot
labels = 'DM', 'DELD', 'DSA', 'COA', 'OOP'
sizes = np.array(output)
colors = ['orange', 'blue', 'green','r', 'm']
#explode = (0, 0, 0, 0.1,0)  # explode 1st slice
total=sum(sizes)

def absolute_value2(val):
    a  = sizes[ np.abs(sizes - val/100.*sizes.sum()).argmin() ]
    return a


# Plot
plt.pie(sizes,labels=labels, colors=colors,autopct=absolute_value2)
plt.axis('equal')
plt.title('FIRST SEMISTER RESULT(IN PERCENTAGE) OF Div-B')
plt.legend(labels,loc=1,borderpad=2, labelspacing=1.5)
plt.show()
 
