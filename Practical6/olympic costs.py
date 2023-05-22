import numpy as np
import matplotlib.pyplot as plt
costs=[]
#create an empty list to store the cost per game.
Game=[]
#create an empty list yo store the game name in the history
olympic_Games = {'1984':1, '1988':8, '1992':15, '1996':7, '2000':5, '2003':14, '2008':43, '2012':40}
#store the data into the 'olympic games' dectionary
for Gamename in olympic_Games:
    costs.append(olympic_Games[Gamename])
    Game.append(Gamename)
#returns sorted list, does not mutate cost.
cost = sorted(costs)
#mutate cost
print(cost)
#Print a list of sorted values for the cost
sortedyear=[]
olympic_Games_value=list(olympic_Games.values())
olympic_Games_keys=list(olympic_Games.keys())
for i in cost:
    for j in range(0,len(olympic_Games)):
        if i == olympic_Games_value[j]:
            sortedyear.append(olympic_Games_keys[j])
#Sort the years by how much they cost

N = len(cost)
#set the bar numbers as the length of costs
ind  = np.arange(N)
width = 0.5
#set the spacing of the bars
pl = plt.bar(ind, cost, width)
plt.ylabel('costs(billions)')
#naming the y axis
plt.title('Eight Olympic costs')
plt.xticks(ind, sortedyear)
#naming the x axis
plt.yticks(np.arange(0,45,5))
#Set vertical coordinate values and spacing 
plt.show()


            

        
        

