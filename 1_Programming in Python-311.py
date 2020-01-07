## 1. Data Science and Python ##

23 + 7
print("Hello Python")

## 2. Python Syntax ##

"""
## Instructions:
## Run the instructions below in the code editor on the right of the screen.
Remember that each instruction must be on a separate line. Also, make sure you write print(), not Print().
"""

print(30 + 10 + 40)
print(4)
print(-3)

## 3. Computer Programs ##

"""
#Instructions:
#By using the print() command, write a program that has three lines of code and:

#Displays the result of 34 + 16
#Displays the number 34
#Displays the number -34
"""

print(34 + 16)
print(34)
print(-34)

## 4. Arithmetical Operations ##

"""
#Instructions:
#Write a program with three lines of code that performs the following arithmetical #operations and
displays the results (you'll need to use the print() command to #display the results):
"""

print(16 * 10)
print(48/5)
print(5**3)

## 5. Variables ##

"""
#Instructions:
#Store the value 15 in a variable named a_value.
#Store the result of (5 + 7) - 2 to a variable named a_result.
#Using the print() command, display the following:
#The value stored in the a_value variable
#The result of adding 12 to the variable a_result
#The result of adding a_value to a_result
"""

a_value = 15
a_result = (5 + 7) - 2
print(a_value)
print(a_result + 12)
print(a_result + a_value)

## 6. Variable Names ##

"""
#Instructions:
## In the code editor on the right, we already stored 34000 in a variable named old-income, and
40000 in a variable named new income — both these variable names cause syntax errors.
## Change the variable name old-income to old_income to prevent a syntax error.
## Change the variable name new income to new_income to prevent a syntax error.
##Run the code after you changed both names.
"""
#old-income = 34000
#new income = 40000

old_income = 34000
new_income = 40000



## 7. Updating Variables ##

"""#Instructions:
#Assign a value of 20 to a variable named variable_1.
#Assign a value of 20 to a variable named variable_2.
#Update the value of variable_2 by adding 10 to its current value. You can take advantage of the += operator.
#Update the value of variable_1 by multiplying its current value by 4. You can take advantage of the *= operator.
#Display variable_1 and variable_2 using print().
"""

variable_1 = 20
variable_2 = 20
variable_2 += 10
variable_1 *= 4
print(variable_1)
print(variable_2)

## 8. Integers and Floats ##

"""
#Instructions:
#Assign the integer 10 to a variable named variable_1.
#Assign the float 2.5 to a variable named variable_2.
#Update the value of variable_1 by adding the float 6.5 to its current value. You can use the += operator.
#Update the value of variable_2 by multiplying its current value by the integer 2. You can use the *= operator.
#Display variable_1 and variable_2 using print().
"""

variable_1 = 10
variable_2 = 2.5
print(type(variable_1))
print(type(variable_2))
variable_1 += 6.5
variable_2 *= 2
print(variable_1)
print(variable_2)

## 9. Conversion Between Types ##

"""
# Instructions:
#Assign the value 13.9 to a variable named variable_a.
#Assign the value 2.8 to a variable named variable_b.
#Round variable_a using the round() command, and assign back the rounded value to variable_a.
#Convert variable_b from a float to an integer using the int() command,
and assign back the converted value to variable_b.
#Display variable_a and variable_b using the print() command.
"""

variable_a = 13.9
variable_b = 2.8
print(variable_a)
print(variable_b)
variable_a = round(variable_a)
variable_b = int(variable_b)
print(variable_a)
print(variable_b)

## 10. Strings ##

"""
#Instructions:
#Assign the string Pandora - Music & Radio to a variable named app_name.
#Assign the string 4.0 to a variable named average_rating. Make sure you don't mistake a string for a float.
#Assign the string 1724546 to a variable named total_ratings. Make sure you don't mistake a string for an integer.
#Assign the string free to a variable named price.
#Display the app_name variable using print().
"""

app_name = "Pandora - Music & Radio"
average_rating = "4.0"
total_ratings = "1724546"
price = "free"
print(type(app_name))
print(app_name)

## 11. Escaping Special Characters ##

"""
#Instructions:
#Assign the string -  Facebook's new motto is "move fast with stable infra".   to a variable named motto.
#Notice there's a . character at the end of Facebook's new motto is "move fast with stable infra". 
 you'll need to include the . character in your answer.
#Display the variable motto using print() — displaying motto is required for answer checking.
"""

motto = 'Facebook\'s new motto is "move fast with stable infra".'
print(motto)

## 12. String Operations ##

"""
#Instructions:
#Assign the string-  [Facebook's rating is]     to a variable named facebook.
#Assign the float 3.5 to a variable named fb_rating.
#Convert fb_rating from a float to a string using the str() command, and assign the converted value to a new variable
 named fb_rating_str.
#Concatenate the strings stored in facebook and fb_rating_str to form the string Facebook's rating is 3.5.
#Assign the concatenated string to a variable named fb.
#You'll need to add a space character between [Facebook's rating is] and [3.5] to avoid ending up with the string
 Facebook's rating is3.5.
#Display the fb variable using print() — this is required for answer checking.
"""

facebook = "Facebook's rating is"
fb_rating = 3.5
fb_rating_str = str(fb_rating)
fb = facebook + ' ' + fb_rating_str
print(fb)