# Programmers: [Your Name]
# Course: CS151 [Instructor name]
# Due Date: [Due Date]
# Lab Assignment: Lab 04
# Description: This program calculates the customer's monthly phone bill based on their package and data usage.
# Data in: data used, package type
# Data out: monthly bill
# Credits: class notes

# Define constants for package prices, data limits, extra costs, and discount
GREEN_BASE_PRICE = 49.99
BLUE_BASE_PRICE = 70.00
PURPLE_BASE_PRICE = 99.95

GREEN_DATA_LIMIT = 2  # in GB
BLUE_DATA_LIMIT = 4  # in GB
PURPLE_DATA_LIMIT = float('inf')  # Unlimited data for Purple package

GREEN_EXTRA_COST = 15.00  # per extra GB
BLUE_EXTRA_COST = 10.00  # per extra GB
PURPLE_EXTRA_COST = 0  # per extra GB

DISCOUNT_THRESHOLD = 75.00  # Discount applicable if bill exceeds this amount
DISCOUNT_AMOUNT = 20.00  # Discount amount for Green package

# Greet the user and get input
print('='*75)
print(" This program will calculate your monthly phone \n bill based on your package and data usage.")
print('='*75)
# Get data usage from the user
data = float(input("\tHow much data did you use this month? "))

# Get package type from the user with validation
package_type = input("\tWhat phone package do you have? (Green, Blue, or Purple) ").strip().lower()

# Validate package type input using a while loop
while package_type != "green" and package_type != "blue" and package_type != "purple":
    print("\tSorry, this is not a valid package type.")
    package_type = input("\tPlease enter a valid package type (Green, Blue, or Purple): ").strip().lower()

# Set base price, data limit, and extra data cost based on the valid package type
if package_type == "green":
    base_price = GREEN_BASE_PRICE
    data_limit = GREEN_DATA_LIMIT
    extra_data_cost = GREEN_EXTRA_COST
elif package_type == "blue":
    base_price = BLUE_BASE_PRICE
    data_limit = BLUE_DATA_LIMIT
    extra_data_cost = BLUE_EXTRA_COST
elif package_type == "purple":
    base_price = PURPLE_BASE_PRICE
    data_limit = PURPLE_DATA_LIMIT
    extra_data_cost = PURPLE_EXTRA_COST

# Calculate the monthly bill
if data > data_limit:
    bill = base_price + extra_data_cost * (data - data_limit)
else:
    bill = base_price

# Apply coupon discount for Green package if applicable
if package_type == "green":
    has_coupon = input("\tDo you have a coupon? (yes or no) ").strip().lower()
    if has_coupon == "yes" and bill >= DISCOUNT_THRESHOLD:
        bill -= DISCOUNT_AMOUNT

# Output the bill amount to the user
print(f"\tYour monthly phone bill is: ${bill:.2f}")

# Thank the user
print("\tThank you for using this program!")
print('='*75)