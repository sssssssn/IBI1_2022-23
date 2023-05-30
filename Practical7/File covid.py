import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import new libraries to work with files and directories and dataframes
os.chdir("/Users/shennuo/IBI1_2022-23")
#change the working directory to full_data.csv file 
covid_data = pd.read_csv("xid-1063743_1")
#name the data as covid_data

print(covid_data.iloc[0:1001:100,1])
#showing the second column from every 100th row from the 1000 rows  
    
location_column = [False, True, False, False, False, False]
location_data = covid_data.iloc[:,location_column]
Afghanistan_row = [] #create a list to store Boolean values
for i in location_data.location: 
    Boolean = i=="Afghanistan"
    Afghanistan_row.append(Boolean) 

print(covid_data.loc[Afghanistan_row,"total_cases"]) 
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

print("mean_new_cases=", np.mean(a))
# computed the mean number of new cases on 31 March 2020.
print("mean_new_deaths=", np.mean(b))
# computed the mean number of new deaths on 31 March 2020.

plt.boxplot(a, vert = True, whis = 1.5, patch_artist = True, meanline = False, showbox = True, showcaps = True, showfliers = True, notch = False) 
plt.title('New cases on 31 March 2020')
plt.ylabel('number')
plt.xlabel('new cases')
plt.show()

plt.boxplot(b, vert = True, whis = 1.5, patch_artist = True, meanline = False, showbox = True, showcaps = True, showfliers = True, notch = False) 
plt.title('New deaths on 31 March 2020')
plt.ylabel('number')
plt.xlabel('new deaths' )
plt.show()
#Plot the new cases and new deaths on 31 March as two separate box plots

#set all the data
world_new_date = []
for i in covid_data.date:
    if not i in world_new_date:
       world_new_date.append(i)
world_new_date = sorted(world_new_date)

new_cases = []      
for i in world_new_date:
    new_cases.append(np.sum(covid_data.loc[covid_data.loc[:,"date"] == i, "new_cases"]))

new_deaths = []
for i in world_new_date:
    new_deaths.append(np.sum(covid_data.loc[covid_data.loc[:,"date"] == i, "new_deaths"]))

plt.plot(world_new_date, new_cases,'b+')
plt.plot(world_new_date, new_deaths,'r*')
plt.xticks(world_new_date[0:len(world_new_date):4],rotation=-90)
plt.title('new cases and new deaths worldwide over time')
plt.show()
#plot both new cases and new deaths worldwide over time.

china_date = []
for i in covid_data.date:
    if not i in china_date:
       china_date.append(i)
china_date = sorted(china_date) 

china_new_cases = []
china_data_rows=covid_data.loc[:,"location"]=="China"
#these command is to find out which lines are used to record the data in china
china_covid_data=covid_data.loc[china_data_rows,:]
#this will generate a new form in which china data are recorded

for i in china_date:
    china_new_cases.append(np.sum(china_covid_data.loc[china_covid_data.loc[:,"date"] == i, "new_cases"]))
    #use a list to store the data of new cases in china
    my_raws = covid_data['location'] == 'China'
china_dates = covid_data.loc[my_raws,'date']
print(covid_data.loc[my_raws,['new_cases','total_cases']])
total_china_cases=0
total_china_cases_list=[]
for i in china_new_cases:
    total_china_cases+=i
    total_china_cases_list.append(total_china_cases)
    
plt.plot(china_dates,china_new_cases,'b+')
plt.plot(china_dates,total_china_cases_list,'r+')
plt.xticks(world_new_date[0:len(china_date):4],rotation=-90)
#Adjust the x label to make it easer to read
plt.title('new cases and total cases developed over time in the China')
plt.show()
#plot new cases and total cases developed over time in the China