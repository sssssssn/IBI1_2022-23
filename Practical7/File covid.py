import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import new libraries to work with files and directories and dataframes
os.chdir("/Users/shennuo/IBI1_2022-23")
#change the working directory to full_data.csv file 
covid_data = pd.read_csv("xid-1063743_1")
#name the data as covid_data

counter=0
while counter<=1000:
    print (covid_data.loc[counter,:])
    counter=counter+1
#showing the second column from every 100th row from the 1000 rows  
    
counter=0
for i in covid_data.loc[:,"location"]:
    if i == "Afghanistan":
     my_columns = [False, True, False, False, True, False]
     print(covid_data.loc[counter,my_columns])
     counter=counter+1
#show “total cases” for all rows corresponding to Afghanistan.

counter=0
a=[]
b=[]
for i in covid_data.loc[:,"date"]:
    if i == '2020-03-31' :
     my_columns = [False, True, True, True, False, False]
     print(covid_data.loc[counter,my_columns])
     a.append(covid_data.loc[counter,"new_cases"])
     b.append(covid_data.loc[counter,"new_deaths"])
     new_data = covid_data.loc[counter,my_columns]
     counter=counter+1
#store only the data on new cases and deaths for 31 March
print(np.mean(a))
# computed the mean number of new cases on 31 March 2020.
print(np.mean(b))
# computed the mean number of new deaths on 31 March 2020.
plt.boxplot(a)
plt.xlabel('new cases')
plt.title('new cases on 31 March')
plt.show()
plt.boxplot(b)
plt.xlabel('new deaths')
plt.title('new deaths on 31 March' )
plt.show()
#Plot the new cases and new deaths on 31 March as two separate box plots

world_dates = covid_data.loc[:,'date']
world_new_cases = covid_data.loc[:,'new_cases']
world_new_deaths = covid_data.loc[:,'new_deaths']
plt.plot(world_dates, world_new_cases,'b+')
plt.plot(world_dates,world_new_deaths,'r*')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('new cases and new deaths worldwide over time')
plt.show()
#plot both new cases and new deaths worldwide over time.

my_raws = covid_data['location'] == 'China'
china_dates = covid_data.loc[my_raws,'date']
print(covid_data.loc[my_raws,['new_cases','total_cases']])
plt.plot(china_dates,covid_data.loc[my_raws,'new_cases'],'b+')
plt.plot(china_dates,covid_data.loc[my_raws,'total_cases'],'r+')
plt.title('new cases and total cases developed over time in the China')
plt.show()
#plot new cases and total cases developed over time in the China





