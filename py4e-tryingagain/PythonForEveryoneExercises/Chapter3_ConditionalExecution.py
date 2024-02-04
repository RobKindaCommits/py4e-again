'''
Created on Jan 24, 2024

@author: rob.fenoglio
'''
'''
Exercise 3.1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
'''
'''
hoursworked=input("Enter your hours worked\n")
hoursworked=float(hoursworked)
overtimehoursworked=0
if hoursworked > 40:
    overtimehoursworked=hoursworked-40
    hoursworked=40
payrate=input("Enter your pay rate per hour\n")
payrate=float(payrate)
totalpaid=hoursworked*payrate+overtimehoursworked*payrate*1.5
print("Your total pay is",totalpaid)
'''


'''
#Exercise 3.2: Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. 
'''
'''
hoursworked=input("Enter your hours worked\n")
try:
    hoursworked=float(hoursworked)
except:
    print("Please enter a numeric value.")
    quit()
overtimehoursworked=0
if hoursworked > 40:
    overtimehoursworked=hoursworked-40
    hoursworked=40
payrate=input("Enter your pay rate per hour\n")
payrate=float(payrate)
totalpaid=hoursworked*payrate+overtimehoursworked*payrate*1.5
print("Your total pay is",totalpaid)
'''


'''
Exercise 3.3: Write a program to prompt for a score between 0.0 and
1.0. If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:
3.11. EXERCISES 41
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
'''
'''
score=input("Please enter a score between 0.0 and 1.0: ")
try:
    score=float(score)
except:
    print("Please enter a numeric value.")
    score=input("Please enter a score between 0.0 and 1.0: ")
    try:
        score=float(score)
    except:
        print("You're hopeless")
        quit()
if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
 '''
 
 '''
    
    