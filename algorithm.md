# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...


1. Prompt user to enter what package they bought, "green", "purple" or "blue" and set the input to data_type

2. Convert data_type to lowercase 
    
3. While data_type does not equal "green", "blue" or "purple"
   1. prompt user to input the package again
    2. Convert data_type to lowercase 
4. If user inputs "green"
    1. Prompt user to input the amount of data they used, store under data_used
       1. if data used > 2
           additional_data = data_used - 2
       2. otherwise 
          additional_data = 0
   2. Prompt user to input if they have a coupon, input "yes" or "no", store under coupon
       1. if input is "yes"
    total_cost = 49.99 + 15(additional_data)
    if total_cost >= 75
        total_cost = total_cost - 20
    otherwise
        total_cost = total_cost

5. Otherwise, if user inputs "blue"
    1. Prompt user to input how much data they used, store under data_used
        1. if data_used > 4
            additional_data = data_used - 4
        2. otherwise
            additional_data = 0
    2. total_cost = 70.00 + 10(additional_data)

6. Otherwise, if user inputs "purple"
    1. total_cost = 99.95

7. Output to the user the amount they owe for their monthly bill

    
    
