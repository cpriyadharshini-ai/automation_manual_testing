'''Write a Python program which accepts a sequence of comma separated 4 digit
binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated
sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010'''

binary=input()
binary_group=binary.split(",")
for bin in binary_group:
  decimal=int(bin, 2)
  if decimal%5==0:
    print(bin)


'''Write a Python program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

a="hello world! 123"
letter_count=0
digit_count=0
for i in a:
    if i.isalpha():
        letter_count=letter_count+1
    elif i.isnumeric():
        digit_count=digit_count+1
print("Letter",letter_count)
print("Digit",digit_count)


'''Write a program which can compute the factorial of a given numbers.The
results should be printed in a comma-separated sequence on a single
line.Suppose the following input is supplied to the program:8
Then, the output should be:40320'''

num=int(input())
fact=1
for i in range(1,num+1):
  fact=fact*i
print(fact)