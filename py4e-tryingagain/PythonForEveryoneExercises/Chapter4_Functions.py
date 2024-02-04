'''
Created on Jan 27, 2024

@author: rob.fenoglio
'''
'''
Exercise 6: Rewrite your pay computation with time-and-a-half for over-
time and create a function called computepay which takes two parameters
(hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''
hoursworked=input("Please enter your hours worked: ")
hoursworked=float(hoursworked)
payrate=input("Please enter your hourly pay rate: ")
payrate=float(payrate)
def computepay(a,b):
    if a > 40:
        overtimehoursworked=a-40
        a=40
    totalpaid=a*b+overtimehoursworked*b*1.5
    print("Your total pay is",totalpaid)
computepay(hoursworked,payrate)

