n = 1
j = 0
#Limit range to stop the loop at greater than 100
while j <= 100:
    n = n+1
#adding gernerations
    j = 2**n
    newborn=2**n - 2**(n-1)
#Calculating the number of new born rabbits
    print("new born",newborn)
print("generations needed",str(n))
#the 7 generations exceed 100 rabbits