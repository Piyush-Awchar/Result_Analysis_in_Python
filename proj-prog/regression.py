import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
d = pd.read_csv('workbook.csv')
sb.regplot(x="Experience",y="salary",data=d)
plt.show()
