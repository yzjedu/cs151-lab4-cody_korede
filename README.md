[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5ZuHqJtk)

# Lab4 Mobile Subscription Fees

### 🔴🔴 *DO NOT* Start to code before the instructor Approve your algorithm, and test cases 🔴🔴
- ### Grade: EMRN
- ### Due: Before Next Lab
- ### [Markdown Tutorial-1](https://www.youtube.com/shorts/-aSSrmAXHDg)
- ### [Markdown Tutorial-2](https://www.youtube.com/shorts/0YLTInrkaHg)
- ### Use [markdown_basics file](markdown_cheatsheet.md) to write readable algorithm

## Problem: 
Write a program to determine how much a customer owes their mobile phone provider based on their subscription package and amount of data used.

## Purpose: 
This lab gives you practice with:
* String methods and formating
* Decision making
* Input validation with loops
* Write your own algorithm, flowchart and control paths before coding

## Details:
The mobile phone provider has three different subscription packages for its customers:  

* **Package Green:** 
  * For $49.99/month, 2GB of data is provided. 
  * Additional GB are $15/GB.  
  * Check if the customer has a coupon. 
  * The coupon takes \$20 off a bill of \$75 or more.  
* **Package Blue:** 
  * For \$70/month, 4GB of data is provided. 
  * Additional GB are $10/GB.
* **Package Purple:** 
  * For \$99.95/month, unlimited data is provided.

Your goal is to tell the customer how much they owe for their monthly bill based on their package, and how much data they used.  Be sure to include the monthly special that only applies to users with a Green package, if they have a coupon. There is no rollover of unused data from month to month in any package.

If the user inputs an invalid package name, **tell them that it was invalid and continue to prompt for a package name until a valid name is entered.** 

## Program Requirements:
When you plan your solution, you must take the following into account:  

1. You may only have one print statement concerning cost
2. You must use at least one logical boolean operator (and/or/not)
3. Use the `f string` formatting approach so that the final amount due only goes to 2 decimal places. 
   1. Look up how this works if you aren't sure (Zybook section 2.9).
4. Your program MUST work no matter what case the user types the package as 
   1. (i.e. `gREEn` should count as the green package). 
   2. How did we learn to do this in Notes 9?

## Steps:
1. Understand the problem
2. Write an algorithm showing the steps the program will go through to solve this problem (`algorithm.md`)
3. Test that your algorithm works by walking through it with example input, and double checking that you've covered all requirements above. **You must show your algorithm to the instructor before you can start coding.**
4. Write your code following your algorithm and using good usability principles in `main.py`. 
5. Properly comment your code with intro comments and line comments
6. Draw a flowchart of your program using `draw.io`
7. Label the control paths on your flowchart. 
   1. Create a list of test cases in `test_cases.xlsx` by listing the input boundary values that will allow you to test each path. 
   2. You must write an equation in excel using the input values in your test cases to calculate what the correct cost should be for each test case's cost output.  
8. Test your code to make sure it works correctly on each control path; fix it if it doesn't work right, and test again.


# Check list Before you submit 

- [ ] Passes your test cases
- [ ] Output price always has 2 values after the decimal.
- [ ] The algorithm matches the code  
- [ ] There is a block of introductory comments at the top
- [ ] There are comments in the code (do not need to determine if they are good)
- [ ] Code uses rounding function or formating
- [ ] Code works for lower, upper or any case combination of user input

## What to Submit in GitHub:

1. Completed `main.py` file  
2. `algorithm.md`
   1. Must contain image of your flow chart
3. An Excel file with your test cases.  
    - Edit the `test_cases.xlsx` file with Excel software 
    - If it can open then ok. Otherwise
      - Right click on `test_cases.xlsx` -> Open In -> Associated Application
4. `RD1.md` -> Reflection for Drive 1
5. `RD2.md` -> Reflection for Drive 2

**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get? 
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working with your partner?