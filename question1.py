# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
import math
x1=int(input('enter the x1 coordinate: '))
x2=int(input('enter the x2 coordinate: '))
y1=int(input('enter the y1 coordinate: '))
y2=int(input('enter the y2 coordinate: '))
distance=math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(f'The distance between two coordinate points {x1}, {x2}, {y1} and {y2} is {int(distance)}')

# Question 1(ii)
# Write a Python program to find maximum between three numbers.

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
number3 = int(input('Enter the third number: '))
# maximum number
maximum = max(number1, number2, number3)
print(f'The maximum between three numbers {number1},{number2} and {number3} is {maximum}  ')



