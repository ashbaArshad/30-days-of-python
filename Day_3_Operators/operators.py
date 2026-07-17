#Day 3: 30 Days of python programming
import math

#1. Declare your age as integer variable
age = 25

#2. Declare your height as a float variable
height = 5.2

#3. Declare a variable that store a complex number
complex_num = 2 + 1j

#4. Write a script that prompts the user to enter base 
# and height of the triangle and calculate an area of 
# this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
height = int(input("Enter height: "))
print("The area of the triangle is ", 0.5 * base * height)

#5. Write a script that prompts the user to enter side a, 
# side b, and side c of the triangle. Calculate the 
# perimeter of the triangle (perimeter = a + b + c).
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
print("The perimeter of the triangle is ", side_a + side_b + side_c)

#6. Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter 
# (perimeter = 2 x (length + width))
length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
area = length * width
print("Area of rectangle is ", area)
perimeter = 2 * area
print("Perimeter of rectangle is ", perimeter)

#7. Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and 
# circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("Enter radius of circle: "))
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius
print("Area of circle is: ", area)
print("Circumference of circle is: ", circumference)

#12. Find the length of 'python' and 'dragon' and make a 
#falsy comparison statement
print(len("python") != len("dragon")) 

#13. Use and operator to check if 'on' is found in both 
# 'python' and 'dragon'
on_in_both = "on" in "python" and "on" in "dragon"
print(f"on in both python and dragon : {on_in_both}")

#14. I hope this course is not full of jargon. 
# Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
print(f"jargon is in the sentence : {"jargon" in sentence}")

#15. There is no 'on' in both dragon and python
print(f"no 'on' in both dragon and python : {not on_in_both}")

#16. Find the length of the text python and convert the 
# value to float and convert it to string
length = len("python")
print(f"Length of python : {length}")
to_float = float(length)
print(f"Converted to float : {to_float}")
to_string = str(to_float)
print(f"Converted to string : {to_string}")

#17. Even numbers are divisible by 2 and the remainder is 
# zero. How do you check if a number is even or not using 
# python?
num = int(input("Enter num : "))
is_even = (num % 2) == 0
print("Is Even : ", is_even)

#18. Check if the floor division of 7 by 3 is equal to the 
# int converted value of 2.7.
floor_val = math.floor(7/3)
to_int = int(2.7)
print(f"Floor(7/3) is equal to int(2.7) : {floor_val == to_int}")

#19. Check if type of '10' is equal to type of 10
print(f"Type of '10' is equal to type of 10 : {type("10") == type(10)}")

#20. Check if int('9.8') is equal to 10
print(f"int('9.8') is equal to 10 : {int(9.8) == 10}")


#21. Write a script that prompts the user to enter hours and 
# rate per hour. Calculate pay of the person?
hours = int(input("Enter hours : "))
rate_per_hr = int(input("Enter rate per hour : "))
weekly_earning = hours * rate_per_hr
print(f"Your weekly earning is {weekly_earning}")

#22. Write a script that prompts the user to enter number 
# of years. Calculate the number of seconds a person can 
# live. Assume a person can live hundred years
secs_in_a_year = 365 * 24 * 60 * 60
years = int(input("Enter number of years you have lived: ")) 
print(f"You have lived for {secs_in_a_year * years} seconds.")

#23. Write a Python script that displays the following table
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125

print(f"{1} {1} {1*1} {1**2} {1**3}")
print(f"{2} {1} {2*1} {2**2} {2**3}")
print(f"{3} {1} {3*1} {3**2} {3**3}")
print(f"{4} {1} {4*1} {4**2} {4**3}")
print(f"{5} {1} {5*1} {5**2} {5**3}")




