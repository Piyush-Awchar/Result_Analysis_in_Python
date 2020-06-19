import matplotlib.pyplot as plt
import csv
ol=[]
th=[]
x=[0,10,20,30,40,50]
fo=open("B.csv",'r')
plot=csv.reader(fo)
for row in plot:
    ol.append(int(row[15]))
    th.append(int(row[16]))
legends=['Online','Theory']  
ranges=['0-10','10-20','20-30','30-40','40-50']
plt.hist([ol,th],x,rwidth=0.7,alpha=1)
plt.title('Online vs Theory marks of Computer Digital Electronics and Logic Design[Div-B]')
plt.xlabel("RANGE OF MARKS SCORED")
plt.ylabel("NUMBER OF STUDENTS")
plt.legend(legends)

plt.show()
