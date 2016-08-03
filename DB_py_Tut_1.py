# Collection of learning programming tutorials using python with Derek Banas

###########################################################################

# Ask th user to input their name and assign it to a variable

name = input('What is your name? ')

# Print out hello followed by the name they entered

print ('Hello ', name)

#########################################################################

# Ask the user to input 2 values and store them in variables num1 num2
num1,num2 = input('Enter 2 numbers: ').split()

# Convert the strings into regular number (Integers)
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
summ = num1 + num2

# Substract values and store in difference
diff = num1 - num2

# Multiply the values and store in product
product = num1 * num2

# Divide the values and store in quotient
quotient = num1 / num2

# Use modulus on values to find the reminder
remainder = num1 % num2

# Print the results
print("{} + {} = {}".format(num1,num2,summ))
print("{} - {} = {}".format(num1,num2,diff))
print("{} * {} = {}".format(num1,num2,product))
print("{} / {} = {}".format(num1,num2,quotient))
print("{} % {} = {}".format(num1,num2,remainder))

###########################################################################

# Problem : Receive miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter Mile: 5
# 5 miles equals 8.04 kilometers

# Ask the user to input miles and assign it to the miles variable
miles = input('Enter Miles: ')

# Convert from string to integer
miles = int(miles)

# Perform calculation by multiplying 1.60934
kilometers = miles * 1.60934

# Print results using format()
print("{} miles equals {} kilometers".format(miles,kilometers))

#############################################################################

# Enter Calculation: 5 * 6
# 5 * 6 = 30

# Store user input of 2 numbers and the operator
num1, operator, num2 = input('Enter Calculation: ').split()

# Convert the strings into integers (numbers)
num1 = int(num1)
num2 = int(num2)

# if +,-,*,/ then we provide output based on operator

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":   
    print("{} * {} = {}".format(num1, num2, num1*num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1/num2))
else:
    print("use either + - * or / next time")

#############################################################################

# We'll provide different output based on age
# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# All Others -> Not Important

# Receive age and store in age
age = eval(input("Enter age: "))

# and : If both are true it returns true
# or : If either condition is true then true
# not : Convert a true condiiton into false and vice versa

# if age is both greater than or equal to 1 and less than or equal to 18 Important
if (age >= 1) and (age <= 18):
    print("Important Birthday")

# if age is either 21 or 50 Important
elif (age == 21) or (age == 50):
    print("Important Birthday")

# we check if age is less than 65 and then convert true to false and vice versa
elif not(age < 65):
    print("Important Birthday")

# Else Not Important
else:
    print("Sorry Not Important")

#########################################################################

# If age is 5 go to kindergarden
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater then 17 say go to college
# Try to complete with 10 or less lines

# Receive age and store in age
age = eval(input("Enter age: "))

# Handle if age < 5
if age < 5:
    print("Too Young to go to School")

# Special output just for age 5
elif age == 5:
    print("Go to Kindergarden")

# Since a number is the result for ages 6 - 17 we can check them all with one condition  
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to Grade {}".format(grade))

# Handle everyone else    
else:
    print("Go to College")

#########################################################################

























