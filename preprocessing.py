import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import math

#to adjust the week day from releavnt excel sheet
wk = 4
sht = 5
xls = pd.ExcelFile('SECOND  BANK (WEEK {0}).xlsx'.format(wk))
df5 = pd.read_excel(xls, 'Sheet{0}'.format(sht))
len = df5.count()
qlt = []


#finding the queue leaving time
for i in range(0, len[0]):
    tme = timedelta(minutes = df5['Arrival time'][i].minute, hours = df5['Arrival time'][i].hour)
    delta = timedelta(minutes = df5['X1'][i])
    qlt.append(datetime.strptime(str(tme + delta).split(".")[0], '%H:%M:%S').time())
df5['QLT'] = qlt


#finding the length of the queue
no = []
hol = []
for j in range(0, len[0]):
    cnt = 0
    minn = datetime(12,12, 12, 23, 59, 59).time()
    wt = 0
    for i in range(0, j):
        if(df5['Arrival time'][j] < df5['QLT'][i]):
            cnt = cnt + 1
            if(minn > df5['QLT'][i]):
                minn = df5['QLT'][i]
                wt = math.modf(df5['X1'][i])[1]*60 + math.modf(df5['X1'][i])[0]
    no.append(cnt)
    hol.append(wt)
# Queue Length
df5['QL'] = no

# How Long the person at the beginning of the queue has waited
df5['HOL'] = hol

#hour and minute of arrival
seconds_in_day = 86400
sin_sec = []
cos_sec = []
day = []
for i in range(0, len[0]):
    sec = df5['Arrival time'][i].hour*3600 + df5['Arrival time'][i].minute*60
    sin_sec.append(np.sin(2*np.pi*sec/seconds_in_day))
    cos_sec.append(np.cos(2*np.pi*sec/seconds_in_day))
    day.append(sht)
df5['sin_time'] = sin_sec
df5['cos_time'] = cos_sec
df5['Day'] = sht

# to show the cyclical nature of time
df5.sample(50).plot.scatter('sin_time','cos_time').set_aspect('equal')
df5.X1.plot()
plt.show()

# print(df5)
#convert to excel
df5.to_excel("B2 W{0} D{1}.xlsx".format(wk, sht))