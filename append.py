employ = ["sidra", 30, "karachi"]
print(employ[0])
employ.append("Pakistan")
print (employ)
employ[2]="Lahore"
print(employ)
employ.insert(1,"Ehsan")
print (employ)
employ.pop() # it will pop last value index means to remove it thelast value
print (employ)
employ.pop(1) # for particular value
# if to remove index wise then use del
del employ[2]
print (employ)
employ.remove("sidra") #if  to remove valuewise
print (employ)