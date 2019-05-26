import random
arr = [] #empty array
for i in range(10): #counting
    print(random.randint(5,500)) # to print any randomnumber in between 5 to 500
    arr.append(random.randint(10,1000))
for num in arr: # to iterate it
    print(arr)
