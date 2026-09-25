'''1. Student Attendance Analysis
A college maintains the daily attendance details of its students in the form of a list containing student IDs. 
Some students may have attended multiple sessions on the same day. The administration wants to identify the longest continuous 
sequence of sessions in which no student ID is repeated. Develop a solution that determines the maximum length of such a sequence.
'''
def attendance_analysis(arr):
  left=0
  maximum_length=0
  unique=set()
  for i in range(len(arr)):
    if arr[i] in unique:
      unique.remove(arr[left])
      left+=1
    unique.add(arr[i])
    current_length=i-left+1
    maximum_length=max(maximum_length, current_length)
  return maximum_length
arr=list(map(int, input().split()))
print(attendance_analysis(arr))

'''2. Online Shopping Price Analysis
An online shopping application stores the prices of products viewed by a customer during a browsing session. 
The customer wants to identify a continuous range of products that provides the maximum possible total discount value. 
Given the discount values, determine the maximum value that can be obtained from any continuous range.
'''
def shopping_price(arr):
    current=arr[0]
    maximum=arr[0]
    for i in range(1,len(arr)):
        current=max(arr[i],current+arr[i])
        maximum=max(maximum,current)
    return maximum
arr=list(map(int,input().split()))
print(shopping_price(arr))

'''3. Rainwater Collection System
A city installs buildings of different heights along a straight road. During rainfall, water gets collected between taller buildings. 
The engineering team needs to calculate the total amount of water that can remain trapped after heavy rainfall based on 
the heights of the buildings.
'''
def trap_water(height):
    n=len(height)
    left=[0]*n
    right=[0]*n
    left[0]=height[0]
    for i in range(1,n):
        left[i]=max(left[i-1],height[i])
    right[n-1]=height[n-1]
    for i in range(n - 2,-1,-1):
        right[i]=max(right[i+1],height[i])
    water=0
    for i in range(n):
        water+=min(left[i],right[i])-height[i]
    return water
height=list(map(int,input().split()))
print(trap_water(height))

'''4. Employee Performance Analysis
A company stores the monthly performance scores of an employee for several months. The scores may contain both positive and negative 
values depending on the employee's performance. Management wants to identify the continuous period during which the employee achieved 
the highest overall performance.
'''
def employee_performance(scores):
    current=scores[0]
    maximum=scores[0]
    for i in range(1,len(scores)):
        current=max(scores[i],current+scores[i])
        maximum=max(maximum,current)
    return maximum
scores = list(map(int, input().split()))
print(employee_performance(scores))

'''5. Product Sales Analysis
A retail company stores the daily sales quantity of a product for several consecutive days. 
Due to seasonal changes, some days may have negative adjustments. The company wants to identify the period that produced the highest 
multiplication of sales-related values. Develop a solution to determine this maximum product.
'''
def sales_analysis(arr):
  current_max=arr[0]
  current_min=arr[0]
  answer=arr[0]
  for i in range(1,len(arr)):
    if arr[i]<0:
      current_max,current_min=current_min,current_max
    current_max=max(arr[i],current_max*arr[i])
    current_min=min(arr[i],current_min*arr[i])
    answer=max(answer,current_max)
  return answer
arr=list(map(int,input().split()))
print(sales_analysis(arr))

'''6. Customer Purchase History
An e-commerce application stores the product IDs purchased by a customer in chronological order. 
The same product may appear multiple times. The system needs to determine the longest sequence of consecutive purchases in 
which every product ID is unique.
'''
def purchase_history(arr):
  left=0
  maximum_length=0
  unique_product_id=set()
  for i in range(len(arr)):
    if arr[i] in unique_product_id:
      unique_product_id.remove(arr[left])
      left+=1
    unique_product_id.add(arr[i])
    current_length=i-left+1
    maximum_length=max(maximum_length, current_length)
  return maximum_length
arr=list(map(int, input().split()))
print(purchase_history(arr))

'''7. Bank Transaction Analysis
A bank stores transaction amounts for a customer's account. A continuous group of transactions may add up to a specific target amount. 
The auditing system needs to determine how many different continuous transaction groups produce exactly the specified amount.
'''
def bank_transaction(arr,target):
    prefix=0
    count=0
    freq={0:1}
    for x in arr:
        prefix+=x
        if prefix-target in freq:
            count+=freq[prefix-target]
        freq[prefix]=freq.get(prefix,0)+1
    return count
arr=list(map(int,input().split()))
target=int(input())
print(bank_transaction(arr,target))

'''8. Employee Skill Grouping
A company receives a list of employee skill codes represented as strings. Employees having the same set of characters in their 
skill codes belong to the same skill category, even if the characters appear in a different order. The HR system needs to organize 
employees into appropriate skill groups.
'''
def group_skills(words):
    groups={}
    for word in words:
        key=''.join(sorted(word))
        if key not in groups:
            groups[key]=[]
        groups[key].append(word)
    return list(groups.values())
words=input().split()
print(group_skills(words))

'''9. Network Packet Analysis
A network monitoring system receives packet identifiers in chronological order. The system must determine the longest sequence of 
consecutive packets whose identifiers form a continuous numerical sequence, regardless of their original order in the incoming data.
'''
def network_packet(arr):
    nums=set(arr)
    maximum=0
    for x in nums:
        if x-1 not in nums:
            current=x
            length=1
            while current+1 in nums:
                current+=1
                length+=1
            maximum=max(maximum,length)
    return maximum
arr=list(map(int,input().split()))
print(network_packet(arr))c

'''10. Hospital Appointment Scheduling
A hospital receives appointment requests represented by starting and ending times. Some appointments overlap with each other. 
The scheduling system needs to combine overlapping appointment periods so that the final schedule contains only non-overlapping time ranges.
'''
def appoinment_scheduling(appointments):
    appointments.sort()
    merged=[appointments[0]]
    for start,end in appointments[1:]:
        last_end=merged[-1][1]
        if start<=last_end:
            merged[-1][1]=max(last_end,end)
        else:
            merged.append([start,end])
    return merged
appointments=[[1,3],[2,6],[8,10],[9,12]]
print(appoinment_scheduling(appointments))