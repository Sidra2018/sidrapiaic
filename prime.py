num = int(input("Enter number : "))
if num == 1 or num == 0:
    print(num,"is not prime")
elif num == 2:
    print(num,"is prime")
else:
    is_prime = True #flags boleancheck means prime 
    for i in range(2,num): # number divideid by 0 ininfinite  from 1 is alawsya divisible and 0 caanoot as 0 infinite,thats y starts from2
        print(i)
        if num % i  == 0:# ifnum is 7 23456
            is_prime = False # means not prime
            break
        
    if is_prime:
        print(num,"is prime")
    else:
        iter = 1
        for i in range(2,num):
iter +=1
if num % i ==0:
    break
if iter == (num -1):
    print("num")        
    #print(num,"is not prime")


