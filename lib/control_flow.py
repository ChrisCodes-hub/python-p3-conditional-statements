#!/usr/bin/env python3

def admin_login(username, password):
    if (username =="admin" or username=="ADMIN") and password =="12345":
     return"Access granted"
    else:
     return"Access denied"
admin_login("admin",12345)
    

def hows_the_weather(temperature):
    if temperature < 40:
       return "It's brisk out there!"
    elif temperature >=40 and temperature <=60:
       return "It's a little chilly out there!"
    elif temperature >85:
       return "It's too dang hot out there!"
    else:
       return "It's perfect out there!"
hows_the_weather(55)

def fizzbuzz(num):
    if num%3==0 and num %5 ==0:
       return "FizzBuzz"
    elif num % 3==0:
       return "Fizz"
    elif num % 5==0:
       return "Buzz"
    else:
       return num
fizzbuzz(3)


def calculator(operation, num1, num2):
    if operation=="+":
       return num1+num2
    elif operation=="-":
       return num1-num2
    elif operation=="*":
       return num1*num2
    elif operation=="/":
       return num1/num2
    else:
       print("Invalid operation!")
       return None
calculator("a",1,2)
    
