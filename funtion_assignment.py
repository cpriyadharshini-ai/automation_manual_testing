'''1.	Write a function calculate(a, b, operation) that performs addition, subtraction, multiplication, or division based on the supplied operation.'''
def calculate(a,b,operation):
  if operation=="Addition" or operation=="addition" or operation=="add":
    return a+b
  elif operation=="subtraction" or operation=="Subtraction" or operation=="sub":
    return a-b
  elif operation=="Multiplication" or operation=="multiplication" or operation=="multiply":
    return a*b
  elif operation=="Division" or operation=="division" or operation=="divide":
    if b!=0:
      return a/b
    else:
      return "'Can't divide because b is 0'"
a=eval(input("Enter a: "))
b=eval(input("Enter b: "))
operation=input("Enter operation: ")
print(f"Answer is {calculate(a,b,operation)}")

'''2.	Write a function sum_numbers(*args) that accepts any number of arguments and returns their sum.'''
def sum_numbers(*args):
    return sum(args)
list=list(map(int, input("Enter : ").split()))
print(sum_numbers(*list))  

'''3.	Write a function employee(**args) that accepts employee information such as name, ID, department and salary, then displays the information.'''
def employee_details(**kwargs):
    print("Employee Information")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
d={}
n=int(input())
for i in range(n):
  key=input("Key: ")
  value=input("Value: ")
  d[key]=value
employee_details(**d)


'''4.	Write a function remove_duplicates(lst) that returns a list containing only unique elements while preserving their original order.'''
def remove_duplicates(list):
  unique=set()
  duplicate=set()
  for num in list:
    if num not in unique:
      unique.add(num)
    else:
      duplicate.add(num)
  return unique
list=list(map(int, input().split()))
print(f"Unique elements : {remove_duplicates(list)}")

'''5.	Using a lambda function, sort a list of tuples based on the second element. Example: [(1,5), (2,3), (4,1)].'''
list=eval(input("Enter: "))
list.sort(key=lambda x:x[1])
print(list)