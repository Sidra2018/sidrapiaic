#Marksheet
print("MARKSHEET")
name = input("Enter name of student : ")
roll_number = input ("Enter roll number : ")
sub1 = int(input("Enter chemistry marks : "))
sub2 = int(input("Enter physics marks : "))
sub3 = int(input("Enter comp marks : "))
sub4 = int(input("Enter urdu marks : "))
sub5 = int(input("Enter sindhi marks : "))
sub= [sub1,sub2,sub3,sub4,sub5]
print ("Subjects and marks")
subject= ["Chemistry","Physics","Computer","Urdu","sindhi"]
print (subject [0:])
print(sub[0:])
marks_obtained = sub1+sub2 +sub3+sub4+sub5
total_marks = 500
percent = (marks_obtained / total_marks) * 100
if percent >= 90 and percent < 100:
    print("Grade A+")
elif percent >= 80 and percent < 90:
    print("Grade A")
elif percent >= 70 and percent < 80:
    print("Grade B")
elif percent >= 60 and percent < 70:
    print("Grade C")
elif percent >= 50 and percent < 60:
    print("Grade D")
else:
    print("Fail")