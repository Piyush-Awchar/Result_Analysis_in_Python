import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
x=[181,159,162,123,142,189,173,126]
y=[65,53,56,49,50,67,59,55,50]
sb.regplot(y,x)
plt.show()
