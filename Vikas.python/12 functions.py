# function is a block of caode, we use function in program according to our need.
# def key word use to define/declear a function
#user-define function - created by user 
#in- built function - already available in pythone

#print () - in-built function
#def - keyword 
#.index() - method

#def myfunction(): # creating a function
#print("i an a function")
#myfuction()   # calling a fuction

#def calc():
#    a = 12
#    b = 23
#    print(a+b) 
#    calc()
#def calc():
#    a=12
#    b=23
#    return a+b
#print(calc())

#function with default parameater/agrument
#def calc(a,b):
#    print(a+b)
#calc(6,6)
#calc(9,6)
#calc(5,6)
#calc(1,6)
    
    
# function with default parameter/argument
#def location(city = "noida"):
#    print("my city is:",city)
#location()
#location("delhi")
#location("patna")
#location("agra")

#items = ["apple","mango","banana"]
#def printlist(fruits):
#    print(fruits)
#printlist(items)

num = int(input("enter a number:"))
def factorial(num):
    fact = 1
    for i in range (1,num+1):
        fact = fact * i
    print("Factorial is: ",fact)
factorial(num)
import calculator
calculator.factorial(5)

from calculator import oddeven
oddeven(7)
def addition(a,b):
    print("Addition is:",a+b)

def oddeven(num):
    if num%2==0:
        print(f"{num} is a Even Number")
    else:
        print(f"{num} is a Odd Number")

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print("Factorial is: ",fact)


                        