#1 ─── Exercise: Declare a variable  ───────────────────────
num = 3.14

print(f'num = {num}')

#2 ─── Exercise: store a variable  ───────────────────────
favorite_language = ("Python is awesome!")

print(f'favorite_language = "{favorite_language}"')

#3 ─── Exercise: False  ───────────────────────
flag = False

print(f'flag = {flag}')

#4 ─── Exercise: variable operations  ───────────────────────
x = 12.5
y = 3.5
z = (x * y)

print(f"x = {x}, y = {y}, z = {z}")

#5 ─── Exercise: variable operations  ───────────────────────
x = 15
y = 4
z = 23

w = int(x % y)
v = int(z % x)
u = int(z % y)

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print(f"w = {w}")
print(f"v = {v}")
print(f"u = {u}")

#6 ─── Exercise: variable operations  ───────────────────────
score = 100

score /= 2
score += 10
score *= 3

print(f"score = {score}")
#7 ─── Exercise: variable operations  ───────────────────────
x = 15
y = 10
z = x == y

print(f"x = {x}, y = {y}, z = {z}")
#8 ─── Exercise: Boolean expresions  ───────────────────────
x1 = True
x2 = False

x3 = x1 and x2
print(f"x3 = {x3}")
#9 ─── Exercise: Boolean expresions  ───────────────────────
a = True
b = True
c = False

result = (a or b) and not c

print(f"result = {result}")
#10 ─── Exercise: wheater map  ───────────────────────
is_sunny = True
temperature = 25
wind_speed = 10
water_temperature = 22

can_go_hiking = bool(is_sunny and temperature and wind_speed)
can_go_swimming = bool(is_sunny and temperature and water_temperature)
cannot_go_outside = bool(not is_sunny) 

print("Can go hiking:", can_go_hiking)
print("Can go swimming:", can_go_swimming)
print("Cannot go outside:", cannot_go_outside)
#11 ─── Exercise: license exercise  ───────────────────────
has_license = True
has_experience = False
has_clean_record = True

can_drive_car = has_license and has_clean_record
can_drive_truck = has_license and has_experience and has_clean_record
cannot_drive_any = not has_license or not has_clean_record

print("Can drive car:", can_drive_car)
print("Can drive truck:", can_drive_truck)
print("Cannot drive any:", cannot_drive_any)
#12 ─── Exercise: review of numbers in variables  ───────────────────────
a = 3
b = 6

c = 0
if a < b or b >= 10:
    c = 2

c += 1
print(f"c = {c}")
#13 ─── Exercise: temperature  ───────────────────────
temperature = int(input())
weather = "unset"

if temperature < 0:
    weather = ("Freezing")
elif temperature >= 0 and temperature <=15:
    weather = ("Cold")
elif temperature >= 16 and temperature <=25:
    weather = ("Mild")
else:
    weather = ("Hot")

print(f"weather = {weather}")
#14 ─── Exercise: dividing floats  ───────────────────────
level = int(input())
has_training = input() == "True"
level_message = "None"

if level >= 1 and level <= 5:
    level_message = "Basic weapons only"

elif level >= 6 and level <= 10 and not has_training:
    level_message = "Need weapon training first"

elif level >= 6 and level <= 10 and has_training:
    level_message = "Access to advanced weapons granted"

elif level >= 11:
    level_message = "Access to all weapons granted"

else:
    level_message = "Invalid level"

print(level_message)
#15 ─── Exercise: Age in ten years  ───────────────────────
name = input()
age = int(input())

age += 10

print(f"In 10 years, {name} will be {age} years old.")
#16 ─── Exercise: dividing floats  ───────────────────────
num1 = float(input())
num2 = float(input())

result = num1 / num2
print(result)

#17 ─── Exercise: divisions  ───────────────────────
# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
# Your code here
for i in range(30, 81):
    if i % 4 == 0:
        print(i, end=", ")
print()  # Creates a new line for better readability

# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
# Your code here
count_impar = 0
for i in range(15, 80):
    if i % 2 == 1:
        count_impar += 1
        print(i, end=", ")
        if count_impar == 8:
            break

print()  # Creates a new line for better readability

# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
# Your code here
for i in range(50, 9, -1):
    if i % 5 == 0:
        print(i, end=", ")
print()  # Creates a new line for better readability

# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
# Your code here
product = 1

for i in range(1, 31):
    if i % 3 == 0:
        product *= i
print(product, end=" ")
# Remember: print only the number, not "Product = number"

#18 ─── Exercise: function of def  ───────────────────────
# Declare the function print_large_number below
def print_large_number():
    print(50005000)

n = int(input())                
for i in range(n):
    print_large_number()
#19 ─── Exercise: FizzBuzz ───────────────────────
def fizzbuzz(num):

    if num % 3 == 0 and num % 7 == 0:
        return("FizzBuzz")
    elif num % 3 == 0:
        return("Fizz")
    elif num % 7 == 0:
        return("Buzz")
    else:
        return(num)
#20 ─── Exercise: FizzBuzz continue ───────────────────────
string_num = int(input())
result = fizzbuzz(string_num)
print(f"Welcome to FizzBuzz!\n{result}")

def fizzbuzz(num):
    
    if num % 3 == 0 and num % 7 == 0:
        return("FizzBuzz")
    elif num % 3 == 0:
        return("Fizz")
    elif num % 7 == 0:
        return("Buzz")
    else:
        return(num)

string_num = int(input())
result = fizzbuzz(string_num)
print(f"Welcome to FizzBuzz!")

for n in range(1, string_num + 1):
    print(fizzbuzz(n))
#20 ─── Exercise: FizzBuzz finally ───────────────────────
def fizzbuzz(num):
    
    if num % 3 == 0 and num % 7 == 0:
        return("FizzBuzz")
    elif num % 3 == 0:
        return("Fizz")
    elif num % 7 == 0:
        return("Buzz")
    elif "3" in str(num) and num % 3 != 0 and num % 7 != 0:
               return("Almost Fizz")
    else:
        return(num)

string_num = int(input())
result = fizzbuzz(string_num)
print(f"Welcome to FizzBuzz!")

for n in range(1, string_num + 1):
    print(fizzbuzz(n))
#21 ─── Exercise: Exercise of list changes ───────────────────────
def change_element(lst, index, new_element):    
    # Write code here
    lst[index] = new_element
    return(lst)
#22 ─── Exercise: Exercise of list changes ───────────────────────
def sum_elements(lst):
    # Write code here
    total_sum = 0
    for i in range(len(lst)):
        total_sum += lst[i]
    print(total_sum)
#23 ─── Exercise: Exercise of list changes ───────────────────────
def change_element(list1, index, list2):
    # Write your code below
    list1[index] = list2[0]
    print(list1)
#24 ─── Exercise: pairs of numbers that multiply to give n using numbers from 1 to n (inclusive). ───────────────────────
n = int(input())
# Write your code below
for i in range (1, n + 1):
    if n % i == 0:
       print(f"{i} {n//i}")
#24 ─── Exercise: Lists ───────────────────────
# exercise 1
shopping_list = ["bread", "eggs", "milk", "butter"]
# exercise 2
def values(lst):
    # Write code here
    for i in range (len(lst)):
        print(lst[i])
# exercise 3
def sum_elements(lst):
    # Write code here
    total_sum = 0
    for i in range(len(lst)):
        total_sum += lst[i]
    print(total_sum)
# exercise 4
def change_element(lst, index, new_element):
    # Write code here
    lst[index] = new_element
    return(lst)
# exercise 5
def change_element(list1, index, list2):
    # Write your code below
    list1[index] = list2[0]
    print(list1)
# exercise 6
def merge(lst1, lst2):
    # Write code here
    lst3 = lst1 + lst2
    lst3.sort()
    return(lst3)
# exercise 7
def combine_and_filter(lst, threshold):
    # Write code here

    result = []
    for x in lst:
        if x > threshold:
            result.append(x)
    result.sort()
    return(result)
# exercise 8
def prod(lst):
    # Write code here
    total_sum = 1
    for i in range(len(lst)):
        total_sum *= lst[i]
    return(total_sum)
# exercise 9
def reverse(lst):
    # Write code here
    new_lst = []
    for i in range(len(lst) -1, -1, -1):
        new_lst.append(lst[i])
    return(new_lst)
#24 ─── Exercise: The enumerate function ───────────────────────
lst = list(map(int, input().split(",")))
# Write your code below
new_lst = []
for index, n in enumerate(lst):
    if n < 50 or n % 5 == 0:
        new_lst.append(index)
print(new_lst)
#25 ─── Exercise: Another exercise of enumerate function ───────────────────────
new_lst = []
for index, letter in enumerate(lst):
    if (len(letter)) > 3 or (letter.startswith("a")):
        new_lst.append(index)
print(new_lst)
#25 ─── Exercise: Iterating Over Strings ───────────────────────
text = input()
# Write your code below
count = 0
for i in text:
      if i.lower() == ("p"):
          count = count + 1
print(count)
#26 ─── Exercise: List Slicing ───────────────────────
lst = input().split(",")
# Write your code below
n = len(lst)

if len(lst) %  2 == 0:
     print(lst[n//2 - 1 : n//2 + 1])
else:
     print(lst[n//2 - 1 : n//2 + 2])
