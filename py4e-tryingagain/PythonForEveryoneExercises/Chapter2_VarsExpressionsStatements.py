'''
Created on Jan 23, 2024

@author: rob.fenoglio
'''
#2.2 Write a program that uses input to prompt a user for their
#name and then welcomes them.

#usersname=input("What is your name?\n")
#print("Hello",usersname)



#2.3 Write a program to prompt the user for hours and rate per
#hour to compute gross pay.

#hoursworked=input("Enter your hours worked\n")
#hoursworked=float(hoursworked)
#payrate=input("Enter your pay rate per hour\n")
#payrate=float(payrate)
#totalpaid=hoursworked*payrate
#print("Your total pay is",totalpaid)



#2.5 Write a program which prompts the user for a Celsius tem-
#perature, convert the temperature to Fahrenheit, and print out the
#converted temperature.

centigradetemp=input("Enter the temperature in centigrade degrees: ")
centigradetemp=int(centigradetemp)
fahrenheittemp=round(centigradetemp*9/5+32,None)
print("The Fahrenheit teamperature is",fahrenheittemp,"degrees.")
