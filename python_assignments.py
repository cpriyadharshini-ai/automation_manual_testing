'''Print all prime numbers between input range (Ex – input 20 50, prints all prime numbers between 20 and 50).'''
start=int(input("Start: "))
end=int(input("End: "))
for num in range(start, end):
    if num>1:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                break
        else:
            print(num)

'''Factorial using recursion'''
def factorial(n):
  if n==0 or n==1:
    return 1
  return n*factorial(n-1)
n=int(input("Enter: "))
print(factorial(n))

'''3.Square of numbers using lambda'''
num=int(input("Enter: "))
square=lambda num:num**2
print(f"Square value of {num} is {square(num)}")

'''4.Find the second largest element in a list'''
list=list(map(int, input("Enter list of numbers: ").split()))
first=float('-inf')
second=float('-inf')
for num in list:
  if num>first:
    second=first
    first=num
  elif num>second and num!=first:
    second=num
print(f"Second largest number in the given list is {second}")

'''5.Count frequency of characters in a string'''
string=input()
freq={}
for ch in string:
  if ch in freq:
    freq[ch]+=1
  else:
    freq[ch]=1
print(f"Frequency count of characters in a string is {freq}")

'''6.	Calculate area of a circle using math library.'''
import math
radius=int(input("Enter "))
area=math.pi*radius**2
print(area)

'''7.	Reverse a string without using built‑in reverse'''
string=input("Enter string: ")
rev=""
for ch in string:
  rev=ch+rev
print(f"Reversed string: {rev}")

'''8.Remove duplicates from a list'''
list=list(map(int, input("Enter list numbers: ").split()))
seen=set()
remove=set()
for i in list:
  if i in seen:
    remove.add(i)
  else:
    seen.add(i)
print(seen)

'''9.Merge two dictionaries'''
dict1=eval(input("Enter 1"))
dict2=eval(input("Enter 2"))
merge=dict1|dict2
print(merge)

'''Another way'''
d1={}
n=int(input("Enter 1: "))
for i in range(n):
  key=input("Key: ")
  value=input("Value: ")
  d1[key]=value
d2={}
n=int(input("Enter 2: "))
for i in range(n):
  key=input("Key: ")
  value=input("Value: ")
  d2[key]=value
merge=d1|d2
print(merge)

'''10.	Fibonacci series using recursion'''
def fib(n):
  if n==0:
    return 0
  elif n==1 or n==2:
    return 1
  return fib(n-1)+fib(n-2)
n=int(input())
for i in range(n+1):
  print(fib(i), end=" ")