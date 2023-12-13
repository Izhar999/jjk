# class Vehicle:
#     def __init__(self,name,max_speed,mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#     def seat_capacity(self,capacity):
#         return (f"the seating capacity of a{self.name} is {capacity}")

# class Bus(Vehicle):
#     def seat_capacity(self, capacity=50):
#         return super().seat_capacity(capacity=50)

# school_bus=Bus("School Volvo",180,10)
# print(school_bus.seat_capacity())
 

# print("Hello World")

# a=input("My name is ")


# a=int(input("a:"))
# # b=int(input("b:"))
# for i in range(2,a):
#     if a%i==0:
#         print("not prime number")
#         break
# else:
#     print("prime number")


# a=float(input("a:"))
# b=float(input("b:"))
# print("product:",a*b)


# a=input("a:")
# print("ASCII value of",a,"is",ord(a))

# a=int(input("a: "))
# b=int(input("b: "))
# a=a+b
# b=a-b
# a=a-b
# print("after swapping: a=",a,"and b=",b)


# a=int(input("a:"))
# b=int(input("b:"))
# temp=a
# a=b
# b=temp
# print("after swapping: a=",a,"and b=",b)


# F=int(input("a:"))
# print("Temperature in Degree Celsius:",(F-32)*5/9)


# a=complex(input("a:"))
# b=complex(input("b:"))
# print("complex:",a+b)


'''Program to Print Prime Numbers From 1 to N'''
# a=int(input("a:"))
# b=int(input("b:"))
# for i in range(a,b+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
        

'''program to Check Whether a Number is Positive or Negative or Zero'''
# a=int(input('a: '))
# if a>1:
#     print(("Positive"))
# elif a==0:
#     print("zero")
# else:
#     print("Negative")

'''Program to Check Vowel or Consonant'''
# a=input("a: ")
# b=("aeiouAEIOU")
# if a in b:
#     print("vowel")
# else:
#     print("Consonant")
'''program to Find the Largest Number Among Three Numbers'''
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# print("max is:",max(a,b,c))
# print("min is:",min(a,b,c))
''' Program to Calculate Sum of Natural Numbers'''
# a=int(input("a: "))
# b=int(input("b: "))
# c=0
# for i in range(a,b+1):
#     c=c+i
#     print("sum of natural num:",c)
'''Program to Print Alphabets From A to Z Using Loop'''
# a=int(input("a: "))
# b=int(input("b: "))
# print("Alphabets From A to Z:")
# for i in range(a,b+1):
#     print(chr(i),end=",")
'''Leap Year Program in python'''
# a=int(input("a: "))
# if a%4==0 and a%100!=0:
#     print("leap year")
# elif a%100==0:
#     print("non-leap year")
# elif a%400==0:
#     print("leap year")
# else:
#     print("non-leap year")
'''Factorial Program in in python'''
# a=int(input("a: "))
# x=1
# for i in range(1,a+1):
#     x=x*i
# print("Factorial num:",x)
'''Fibonacci Series Program'''
# x=int(input("a: "))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(0,x-3):    
#     print(a+b)
#     temp=a
#     a=b
#     b=temp+b
# print(b)
'''gcd of Two Numbers'''
# import math
# x=int(input("a: "))
# y=int(input("b: "))
# print("gcd:",math.gcd(x,y))
'''LCM of Two Numbers'''
# import math
# x=int(input("a: "))
# y=int(input("b: "))
# print("gcd:",math.lcm(x,y))
'''Program to Print Armstrong Numbers Between 1 to 1000'''
# x=int(input("x: "))
# y=int(input("y: "))
# v=0
# for i in range(x,y+1):
    # for j in str(i):
    #     u=int (j)**len(str(i))
    #     v=v+u
    # if v==int(i):
    #     print(v)
    # else:
    #     continue
"""d=0
    l=i
    while l>0:
        d=l%10
        v=v+(d*d*d)
        l//=10
    if v==i:
        print(i)
    v=0 """


'''Reverse Number Program'''  
# a=int(input("a: "))
# print(str(a)[::-1])  
'''Palindrome Number Program'''
# a=int(input("a: "))
# x=str(a)[::-1]
# if int(x)==(a):
#     print("palindrome num:")
# else:
#     print("Not")
'''Program To Check Neon Number'''
# a=int(input("a: "))
# d=a*a
# s=0
# f=0
# print(s)
# f=tuple(map(int, s))
# print(f)
# if sum(f)==a:
#     print("Neon number")

# a=int(input("a: "))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# a=int(input("a: "))
# for i in range(1,a+1):
#     for j in range(1,(a-i)+1):
#         print("*",end=" ")
#     print()


# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,(a-i)+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


'''Print Pascal's Triangle in Python'''
# from math import factorial
 
# input n
# n = 5
# for i in range(n):
#     for j in range(n-i+1):
 
#         # for left spacing
#         print(end=" ")
 
#     for j in range(i+1):
 
#         # nCr = n!/((n-r)!*r!)
#         print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
#     # for new line
#     print()
# from math import factorial 
# n=9
# for i in range(n):
#     for j in range(n-i+1):
#         print(end=" ")
#     for j in range(i+1):
#         print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
#     print()

# a=('kk','dd','4','gg')
# u=list(a)
# print(','.join(u))


# u='kk','ll','mm','nn'
# a,b,c,d=u
# print(c)


# from math import factorial
# n=5
# for i in range(n+1):
#     for j in range(n-i+1):
#         print(end=' ')
#     for j in range(i+1):
#         print(factorial(i)//(factorial(j)*factorial(i-j)),end=' ')
#     print()








































































































































