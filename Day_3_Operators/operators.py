#Day 3: 30 Days of python programming

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

