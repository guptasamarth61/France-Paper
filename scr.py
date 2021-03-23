import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns
ls = [1.9907992,  2.22148731, 2.3639862, 1.88652862, 2.75121603, 2.53209383, 4.32684969, 2.83955137, 1.90366743, 1.94629013]
df1 = pd.DataFrame(ls, columns = ['A'])
print(df1.describe().transpose()) 
# df = pd.read_excel("Bank 2\Data.xlsx")
# # sns.pairplot(df[['sin_time', 'cos_time']], diag_kind='kde')
# # sns.histplot(df['Day'], kde = True)
# # plt.title("Day")
# plt.show()
# # df2 = df[['sin_time', 'cos_time', 'QL', 'HOL', 'Day', 'Week', 'X1']].describe().transpose()
# # df2.to_excel("Data Describe.xlsx")

