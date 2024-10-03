# Programmers: Cody and Korede
# Course: CS151, Professor Zee
# Due Date: October 10th, 2024
# Lab Assignment: Lab 04
# Problem Statement: Write a program to determine how much a customer owes
#                    their mobile phone provider based on their subscription
#                    package and amount of data used.
# Data In: Data type (data_type), Data used (data_used), If user has coupon (coupon)
# Data Out: How much data was used (data_used), Bill for the month (total_cost),
# Credits: None other than class :)


# Creation of various necessary variables
# total_cost -> value of the monthly bill
# data_used -> the data that the user has used in total for this month
# additional_data -> the amount of data the user has used that exceeds
#                    their plan's given amount
#                    (only used if data is Green or Blue)
# coupon -> a string that's used for determining if the user has a coupon
#           that can lower the price by $20
#           (only used if data is Green)
total_cost = 0
data_used = 0
additional_data = 0
coupon = ""


# Ask the user to input their current data plan
# After that, take the input and lower it so that the program works
# as long as the user inputs the word (not case-sensitive)
data_type = str(input("Enter the data plan you're currently using (please input Green, Blue, Purple): "))
data_type = data_type.lower()


# Check if data_type is actually green, blue, or purple
# If it isn't, prompt the user to input code again
while data_type != "green" and data_type != "blue" and data_type != "purple":
    data_type = str(input("Invalid input. Please enter the data plan you're currently using (please input Green, Blue, Purple): "))
    data_type = data_type.lower()


# The three different routes depending on what the data type is

# In Green:
# Ask for data -> accommodate for extra data -> check for coupon
# check if coupon input is valid -> loop if not -> calculate total cost
# depending on if user's bill exceeds 70 and user has coupon

# In Blue:
# Ask for data -> accommodate for extra data -> calculate total cost

# In Purple:
# Set cost equal to 99.95
if data_type == "green":
    data_used = int(input("How much data in total did you use this month?: "))
    if data_used > 2:
        additional_data = data_used - 2
    else:
        additional_data = 0
    coupon = str(input("Do you have a coupon that could be used to aid in your payment? (please input yes or no): "))
    coupon = coupon.lower()
    while coupon != "yes" and coupon != "no":
        coupon = str(input("Invalid input. Do you have a coupon that could be used to aid in your payment? (please enter yes or no): "))
        coupon = coupon.lower()
    total_cost = 49.99 + (additional_data * 15)
    if total_cost >= 75 and coupon == "yes":
        total_cost = total_cost - 20
elif data_type == "blue":
    data_used = int(input("How much data in total did you use this month?: "))
    if data_used > 4:
        additional_data = data_used - 4
    else:
        additional_data = 0
    total_cost = 70 + (additional_data * 10)
else:
    total_cost = 99.95


# Determines what to print depending on data type
# All print statements must be one line
# Include total cost, data used (if necessary), and if a coupon will be used (if necessary)
if data_type == "purple":
    print(f"This month, your monthly bill has come to ${total_cost:.2f}")
elif data_type == "green":
    if coupon == "yes":
        phrase = (f"This month, you have used {data_used}GB of data. "
                  f"Since you have a coupon, your bill has been reduced by $20.00. Your monthly bill has come to ${total_cost:.2f}")
        print(phrase)
    else:
        phrase = f"This month, you have used {data_used}GB of data. Your monthly bill has come to ${total_cost:.2f}"
        print(phrase)
else:
    phrase = f"This month, you have used {data_used}GB of data. Your monthly bill has come to ${total_cost:.2f}"
    print(phrase)

