# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 22:08:18 2023

@author: 100840150
"""
import pandas as pd

hr=67
coffe=2
ed=2
alcohol=1
ce=10
import random

#print(random.randint(0, 3))
day=['7','8','12','13','18','22']
days=[str(i) for i in range(1,31)]
res=[]
da=[]
for i in range(len(days)):
    res.append(hr)
    da.append(days[i]+'7')
    res.append((hr+random.randint(0, 3)+random.randint(0, 1)))
    da.append(days[i]+'8')
    res.append(hr)
    da.append(days[i]+'12')
    res.append((hr+random.randint(0, 3)+random.randint(0, 3)))
    da.append(days[i]+'13')
    res.append((hr+random.randint(0, 3)))
    da.append(days[i]+'18')
    res.append((hr+random.randint(0,4)+random.randint(0, 7)+random.randint(0, 3)+random.randint(0, 2)))
    da.append(days[i]+'22')
    
    hr=hr+random.randint(-2*alcohol,2*alcohol)

dic={'time':da,'hr':res}
dic=pd.DataFrame(dic)
dic.to_csv('data.csv',index=False)

import datetime 
import numpy as np
import matplotlib.pyplot as plt
data=[]
for i in range(1,31):
    data.append(datetime.date(2023, 1, i))
    data.append(datetime.date(2023, 1, i))
    data.append(datetime.date(2023, 1, i))
    data.append(datetime.date(2023, 1, i))
    data.append(datetime.date(2023, 1, i))
    data.append(datetime.date(2023, 1, i))


fig, axs = plt.subplots()
axs.plot(data, res)
axs.set_xlabel('Time')
axs.set_ylabel('HR')
axs.grid(True)
plt.xticks(rotation=45)



fig.tight_layout()
plt.show()


