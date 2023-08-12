# Programmer Name: Gilbert Negrillo
# Date: 8/11/23

print("Welcome to the Largest of Three Program")

# Variables
first_num = 0
second_num = 0
third_num = 0
largest_num = 0

user_name = ""

result_of_division = 0.0

play_again = False

# Output the types of variables
print("\n firstNumber is of type: " + str(type(first_num)))
print("\n user_name is of type: " + str(type(user_name)))
print("\n result_of_division is of type: " + str(type(result_of_division))) # output result_of_division type
print("\n play_again is of type: " + str(type(play_again))) # output play_again type


# Get three integers from the user
first_num = int(input("\n Please enter the first whole (integer) number: "))
print("\n firstNum = " + str(first_num))
print("\n firstNumber is of type: " + str(type(int(first_num)))) # Data type back to int
second_num = int(input("\n Please enter the second whole (integer) number: "))
print("\n secondNum = " + str(second_num))
print("\n secondNumber is of type: " + str(type(int(second_num)))) # Data type back to int
third_num = int(input("\n Please enter the third whole (integer) number: "))
print("\n thirdNum = " + str(third_num))
print("\n thirdNumber is of type: " + str(type(int(third_num)))) # Data type back to int

user_name = (input("\n Please enter your name: ")) # get user's name
print("\n\n user_name = " + user_name) # print() user's name

quotient = first_num / second_num # find the quotient of the first input number by the second input number
print("\n\n Quotient of the first input number by the second input number = " + str(quotient)) # output the quotient of the first input number by the second input number
print("\n Quotient is of type: " + str(type(float(quotient))))


# Nested if statement proper data types (int) with arithmetic operators
if (first_num > second_num):
    if(first_num > third_num):
        largest_num = first_num
    else:
        largest_num = third_num
else:
    if(second_num > third_num):
         largest_num = second_num
    else:
        largest_num = third_num


print("\n\n" + user_name + "," + "the largest number of three the numbers you entered is: " + str(largest_num))
print("\n largest_num is of type: " + str(type(int(largest_num))))

# Compound if statement using and operator
if (first_num < second_num) and (first_num < third_num):
    print("\n\n" + str(first_num) + " is smallest")
else:
    if(second_num < first_num) and (second_num < third_num):
        print("\n\n" + str(second_num) + " is smallest")
    else:
        print("\n\n" + str(third_num) + " is smallest")


# ChatGPT largest of three solution
print("\n\n ChatGPT largest of three solution")
def largest_of_three(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif(b >= a) and (b >= c):
        return b
    else:
        return c

num1 = float(input("Enter the first number: "))
print("\n\n num1 is of type: " + str(type(num1)))
num2 = float(input("Enter the second number: "))
print("\n\n num2 is of type: " + str(type(num2)))
num3 = float(input("Enter the third number: "))
print("\n\n num3 is of type: " + str(type(num3)))

largest = largest_of_three(num1, num2, num3)
print("The largest number among", num1, ",", num2, "and", num3, "is", largest)
print("\n largest is of type: " + str(type(largest)))