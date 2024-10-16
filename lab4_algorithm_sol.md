### Algorithm for Mobile Subscription Fees Calculation

1. Output the purpose and a brief description of the program to the user.

2. Initialize Constants for Subscription Packages:
- `GREEN_BASE_PRICE = 49.99`
- `BLUE_BASE_PRICE = 70.00`
- `PURPLE_BASE_PRICE = 99.95`
- `GREEN_DATA_LIMIT = 2` (GB)
- `BLUE_DATA_LIMIT = 4` (GB)
- `PURPLE_DATA_LIMIT = unlimited` (Unlimited data for Purple package)
- `GREEN_EXTRA_COST = 15.00` (per extra GB)
- `BLUE_EXTRA_COST = 10.00` (per extra GB)
- `PURPLE_EXTRA_COST = 0` (Unlimited data)
- `DISCOUNT_THRESHOLD = 75.00`
- `DISCOUNT_AMOUNT = 20.00`

4. Ask the user to input the amount of data used (in GB).

5. Ask the user to input their subscription package type (`green`, `blue`, or `purple`), and convert the input to lowercase and remove extra spaces.

1. While the input is not `"green"`, `"blue"`, or `"purple"`:
   1. Output an error message indicating an invalid package type.
   1. Re-prompt the user to input a valid package type (accepting any capitalization).

7. Set the `base_price`, `data_limit`, and `extra_data_cost` based on the selected `package_type`:
    1. If the package type is `green`:
       1. Set `base_price = GREEN_BASE_PRICE`
       1. Set `data_limit = GREEN_DATA_LIMIT`
       1. Set `extra_data_cost = GREEN_EXTRA_COST`
    2. Else if the package type is `blue`:
       1. Set `base_price = BLUE_BASE_PRICE`
       1. Set `data_limit = BLUE_DATA_LIMIT`
       1. Set `extra_data_cost = BLUE_EXTRA_COST`
    3. Else if the package type is `purple`:
       1. Set `base_price = PURPLE_BASE_PRICE`
       1. Set `data_limit = PURPLE_DATA_LIMIT` (unlimited)
       1. Set `extra_data_cost = PURPLE_EXTRA_COST` (no extra cost)

8. Calculate the monthly bill:
    1. If the `data` used exceeds the `data_limit`:
       1. Calculate `bill = base_price + extra_data_cost * (data - data_limit)`
    2. Otherwise:
       1. Set `bill = base_price`

9. If the package type is `green`, check for discount eligibility:
    1. Ask the user if they have a coupon (`yes` or `no`), then convert to lowercase and strip spaces.
    2. If the user has a coupon and `bill >= DISCOUNT_THRESHOLD`:
       1. Apply the discount: `bill = bill - DISCOUNT_AMOUNT`

10. Output the calculated `bill` to the user, formatted to two decimal places.

11. Output a message thanking the user and indicating that the program has ended.