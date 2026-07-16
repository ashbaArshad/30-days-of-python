#Day 2: 30 Days of python programming
import math

first_name = "Maria"
last_name = "Scott"
full_name = "Maria Scott"
country = "Germany"
city = "Berlin"
age = 22
year = 2026
is_married = False
is_true = True
is_light_on = True
var1, var2, var3 = 1, 2, 3

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(var1))
print(type(var2))
print(type(var3))

print("Length of first name :", len(first_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
print("Num1 : ", num_one)
print("Num2 : ", num_two)
total = num_one + num_two
print("Total : ", total)
diff = num_one - num_two
print("Difference : ", diff)
product = num_one * num_two
print("Product : ", product)
division = num_one / num_two
print("Division : ", division)
reminder = num_two % num_one
print("Reminder : ", reminder)
exp = num_one ** num_two
print("Exponent : ", exp)
floor_division = math.floor(division)
print("Floor Division : ", floor_division)

radius = 30 
print("Radius Of Circle : ", radius)

area_of_circle = 3.15 * radius ** 2
print("Area Of Circle : ", area_of_circle)

circum_of_circle = 2 * 3.15 * radius
print("Circumference Of Circle : ", area_of_circle)

radius = int(input("Enter radius of circle : "))
print("Radius Of Circle : ", radius)

area_of_circle = 3.15 * radius ** 2
print("Area Of Circle : ", area_of_circle)

circum_of_circle = 2 * 3.15 * radius
print("Circumference Of Circle : ", area_of_circle)

first_name, last_name, country, age = input("Enter firstname, lastname, " \
    "country and age separated by space : ").split()

print("First Name : ", first_name)
print("Last Name : ", last_name)
print("Country : ", country)
print("Age : ", age)

help('keywords')
