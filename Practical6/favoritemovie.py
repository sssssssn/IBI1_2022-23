
import numpy as np
import matplotlib.pyplot as plt
my_dict = {}
#creat an empty dictionary to store data
moviegenre = {'Comedy':73, 'Action':42, 'Romance':38, 'Fantasy':28, 'Science-fiction':22, 'Horror':19, 'Crime':18, 'Documentary':12, 'History':8, 'War':7 }
#store the data into the 'moviegenre' dictionary
my_dict = moviegenre
sizes=[]
#create a new list to store the number
for movie in moviegenre:
    print(movie,my_dict[movie])
#print the dictionary
    sizes.append(my_dict[movie])
#store the number of the students who like a particular type of movie in to a list
labels = 'Comedy', 'Action', 'Romance', 'Fantasy', 'Science-fiction', 'Horror', 'Crime', 'Documentary', 'History', 'War'
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%', 
        shadow=False, startangle=90)
plt.axis('equal')
# equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
movietype=input('which  kind of movie do you want to search?')
#get the movie type that the user want to search
print(my_dict[movietype])


    





