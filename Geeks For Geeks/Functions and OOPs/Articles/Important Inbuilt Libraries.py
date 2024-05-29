Math Library
The 
𝑚
𝑎
𝑡
ℎ
 module is a standard Python module providing mathematical functions. It includes a wide range of functions for basic arithmetic, trigonometry, logarithmic, exponential, and more. Here are some commonly used functions from the 
𝑚
𝑎
𝑡
ℎ
 module:

Basic Arithmetic Functions
1. 'math.ceil(x)`:
Returns the smallest integer greater than or equal to x.

Python3

import math
result = math.ceil(4.2)
print(result)  
Output - 5

2. 
𝑚
𝑎
𝑡
ℎ
.
𝑓
𝑙
𝑜
𝑜
𝑟
(
𝑥
)
:
Returns the largest integer less than or equal to x.

Python3

 import math
 result = math.floor(4.9)
 print(result)
Output - 4

3. 
𝑚
𝑎
𝑡
ℎ
.
𝑡
𝑟
𝑢
𝑛
𝑐
(
𝑥
)
:
Returns the truncated integer value of x.

Python3

import math
result = math.trunc(4.9)
print(result) 
Output - 4

4. 
𝑚
𝑎
𝑡
ℎ
.
𝑠
𝑞
𝑟
𝑡
(
𝑥
)
:
Returns the square root of x.

Python3

import math
result = math.sqrt(16)
print(result)
Output - 4.0

Trigonometric Functions
5. 
𝑚
𝑎
𝑡
ℎ
.
𝑠
𝑖
𝑛
(
𝑥
)
, 
𝑚
𝑎
𝑡
ℎ
.
𝑐
𝑜
𝑠
(
𝑥
)
 , 
𝑚
𝑎
𝑡
ℎ
.
𝑡
𝑎
𝑛
(
𝑥
)
:
Return the sine, cosine, and tangent of x (measured in radians).

Python3

import math
angle = math.radians(45)  # Convert degrees to radians
sin_result = math.sin(angle)
cos_result = math.cos(angle)
tan_result = math.tan(angle)
print("sin_result :",sin_result, "cos_result :", cos_result, "tan_result :", tan_result)
Output - sin_result : 0.7071067811865475 cos_result : 0.7071067811865476 tan_result : 0.9999999999999999

Logarithmic and Exponential Functions
6. 
𝑚
𝑎
𝑡
ℎ
.
𝑙
𝑜
𝑔
(
𝑥
,
𝑏
𝑎
𝑠
𝑒
)
:
Returns the natural logarithm of x with the specified base.

Python3

import math
result = math.log(16, 2)
print(result)  
output - 4.0

7. 
𝑚
𝑎
𝑡
ℎ
.
𝑒
𝑥
𝑝
(
𝑥
)
:
Returns e raised to the power of x.

Python3

   import math
   result = math.exp(2)
   print(result)
Output - 7.3890560989306495

Constants
8. 
𝑚
𝑎
𝑡
ℎ
.
𝑝
𝑖
:
Mathematical constant representing the ratio of the circumference of a circle to its diameter.

9. 
𝑚
𝑎
𝑡
ℎ
.
𝑒
:
Mathematical constant representing the base of the natural logarithm.

Python3

import math
print(math.pi)
print(math.e)
Output - 3.141592653589793

2.718281828459045

You can explore more functions and constants in the official Python documentation: https://docs.python.org/3/library/math.html

Random Library
The 
𝑟
𝑎
𝑛
𝑑
𝑜
𝑚
 module in Python is a standard library module that provides functions for generating random numbers, selecting random elements, and performing various randomization tasks. It is commonly used in applications involving simulations, games, statistical sampling, cryptography, and more.

Here are some commonly used functions from the 
𝑟
𝑎
𝑛
𝑑
𝑜
𝑚
 module:

Generating Random Numbers:
1. 
𝑟
𝑎
𝑛
𝑑
𝑜
𝑚
(
)
:
Returns a random floating-point number in the range [0.0, 1.0).

Python3

import random
value = random.random()
print(value)
Output - 0.14277691938900905

2. 
𝑟
𝑎
𝑛
𝑑
𝑖
𝑛
𝑡
(
𝑎
,
𝑏
)
:
Returns a random integer between 
𝑎
 and 
𝑏
 (inclusive).

Python3

import random
value = random.randint(1, 10)
print(value)
Output - 7

3. 
𝑢
𝑛
𝑖
𝑓
𝑜
𝑟
𝑚
(
𝑎
,
𝑏
)
:
Returns a random floating-point number in the range [a, b) or [a, b] if 
𝑏
 is included.

Python3

import random
value = random.uniform(1.0, 5.0)
print(value)
Output - 1.1674375168224214

Randomizing Sequences:
4. 
𝑠
ℎ
𝑢
𝑓
𝑓
𝑙
𝑒
(
𝑠
𝑒
𝑞
𝑢
𝑒
𝑛
𝑐
𝑒
)
:
Randomly shuffles the elements of a sequence in place.

Python3

import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
Output - [5, 3, 2, 4, 1]

5. 
𝑐
ℎ
𝑜
𝑖
𝑐
𝑒
(
𝑠
𝑒
𝑞
𝑢
𝑒
𝑛
𝑐
𝑒
)
:
Returns a random element from a sequence.

Python3

import random
my_list = [1, 2, 3, 4, 5]
value = random.choice(my_list)
print(value)
Output - 4

6. 
𝑠
𝑎
𝑚
𝑝
𝑙
𝑒
(
𝑠
𝑒
𝑞
𝑢
𝑒
𝑛
𝑐
𝑒
,
𝑘
)
:
Returns a new list with 
𝑘
 unique random elements sampled from the sequence without replacement.

Python3

import random
my_list = [1, 2, 3, 4, 5]
sampled = random.sample(my_list, 3)
print(sampled)
Output - [2, 5, 4]

DateTime Library
In Python, the 
𝑑
𝑎
𝑡
𝑒
𝑡
𝑖
𝑚
𝑒
 module provides classes for working with dates and times. It allows you to represent dates, times, and intervals, and perform operations on them. Here are some key components of the 
𝑑
𝑎
𝑡
𝑒
𝑡
𝑖
𝑚
𝑒
 module:

1. 
𝑑
𝑎
𝑡
𝑒
𝑡
𝑖
𝑚
𝑒
 Class:
The 
𝑑
𝑎
𝑡
𝑒
𝑡
𝑖
𝑚
𝑒
 class represents a date and a time. It has attributes like year, month, day, hour, minute, second, and microsecond.

Python3

from datetime import datetime
current_datetime = datetime.now()
print(current_datetime)
Output - 2023-11-30 08:17:47.597082

2. 
𝑑
𝑎
𝑡
𝑒
 Class:
The 
𝑑
𝑎
𝑡
𝑒
 class represents a date (year, month, and day) without a time component.

Python3

from datetime import date
current_date = date.today()
print(current_date)
Output - 2023-11-30

3. 
𝑡
𝑖
𝑚
𝑒
 Class:
The 
𝑡
𝑖
𝑚
𝑒
 class represents a time (hour, minute, second, and microsecond) without a date component.

Formatting and Parsing:
You can format 
𝑑
𝑎
𝑡
𝑒
𝑡
𝑖
𝑚
𝑒
 objects as strings and parse strings into 
𝑑
𝑎
𝑡
𝑒
𝑡
𝑖
𝑚
𝑒
 objects using the 
𝑠
𝑡
𝑟
𝑓
𝑡
𝑖
𝑚
𝑒
 and 
𝑠
𝑡
𝑟
𝑝
𝑡
𝑖
𝑚
𝑒
 methods.

Python3

from datetime import datetime
current_datetime=datetime.now()
# Format a datetime object as a string
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# Parse a string into a datetime object
parsed_date = datetime.strptime("2023-01-01 12:30:00", "%Y-%m-%d %H:%M:%S")
print(parsed_date)
Output - 2023-11-30 08:29:10

2023-01-01 12:30:00

Date Arithmetic:
Performing arithmetic operations with dates is possible using the 
𝑡
𝑖
𝑚
𝑒
𝑑
𝑒
𝑙
𝑡
𝑎
 class.

Python3

from datetime import datetime, timedelta
current_datetime=datetime.now()
future_date = current_datetime + timedelta(days=7)
print(future_date)
Output - 2023-12-07 08:29:56.154919

For more details and examples, refer to the official Python documentation on the 
𝑑
𝑎
𝑡
𝑒
𝑡
𝑖
𝑚
𝑒
 module https://docs.python.org/3/library/datetime.html

Challenge Galore
Problem Statement - Write a Python program that calculates the remaining days, hours, and minutes until the event. Additionally, provide the percentage completion of the event based on the current time compared to the event's start time.
Python3

from datetime import datetime, timedelta
import math

event_date = datetime(2023, 12, 31, 18, 30)  # December 31, 2023, 6:30 PM

current_datetime = datetime.now()

time_difference = event_date - current_datetime
remaining_days = time_difference.days
remaining_hours, remaining_seconds = divmod(time_difference.seconds, 3600)
remaining_minutes = remaining_seconds // 60

# Calculate percentage completion
total_seconds_in_event = (event_date - event_date.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
elapsed_seconds = (current_datetime - event_date.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
percentage_completion = (elapsed_seconds / total_seconds_in_event) * 100


print(f"Remaining time until the event: {remaining_days} days, {remaining_hours} hours, {remaining_minutes} minutes.")
print(f"Percentage completion of the event: {math.floor(percentage_completion)}%")
Output - Remaining time until the event: 31 days, 9 hours, 0 minutes.

Percentage completion of the event: -3971%

