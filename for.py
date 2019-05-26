#for range print
for i in range(10): # 0 to 9 and i is  variable # range 
    print (i)
    print("hello")
for i in range(2,10): #starts from 2 means 1 till 9print("hello")
    print(i)
import random
arr = [] #empty array
for i in range(2,10): #counting
    print(random.randint(5,500)) # to print any randomnumber in between 5 to 500
    arr.append(random.randint(10,1000))
for num in arr: # to iterate it
    print(num)
