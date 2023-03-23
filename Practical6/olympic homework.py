
import numpy as np
import matplotlib.pyplot as plt
costs=[]
#create an empty list to store the cost per game.
Game=[]
#create an empty list yo store the game name in the history
olympic_Games = {'los angeles 1984':1, 'Seoul 1988':8, 'Barcelona 1992':15, 'Atlanta 1996':7, 'Sydney 2000':5, 'Athens 2003':14, 'Beijing 2008':43, 'London 2012':40}
#store the data into the 'olympic games' dectionary
for Gamename in olympic_Games:
    costs.append(olympic_Games[Gamename])
    Game.append(Gamename)
#returns sorted list, does not mutate cost.
cost = sorted(costs)
cost.sort()
#mutate cost
print(cost)
#Print a list of sorted values for the cost

N = len(costs)
#set the bar numbers as the length of costs

ind  = np.arange(N)
width = 0.5
#set the spacing of the bars
pl = plt.bar(ind, costs, width)
plt.ylabel('costs')
#naming the y axis
plt.title('eight Olympic costs')
plt.xticks(ind, Game )
#naming the x axis
plt.yticks(np.arange(0,45,5))
#Set vertical coordinate values and spacing

plt.show()
