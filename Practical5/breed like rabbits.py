n = 1
j = 0
#Limit range to stop the loop at greater than 100
while j <= 100:
    n = n+1
#adding gernerations
    j = 2**n
#Calculating the number of next generations
    print(j)
print(str(n))
#the 7 generations exceed 100 rabbits