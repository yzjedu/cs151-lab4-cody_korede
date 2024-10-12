# LAB-4 Feedback

| Test Case | in: package | in: GB used | in: coupon? | output: Total                    |
|-----------|-------------|-------------|-------------|----------------------------------|
| 1         | green       | 1           | yes         | 49.99                            |
| 2         | blue        | 4           | N/A         | 70                               |
| 3         | purple      | 10          | N/A         | 99.95                            |
| 4         | BLUE        | 0           | N/A         | 70                               |
| 5         | Green       | 8           | yes         | 119.99                           |
| 6         | Blue        | 8           | N/A         | 110                              |
| 7         | Green       | 7           | no          | 124.99                           |
| 8         | aqua        | N/A         | N/A         | loops until correct input is provided |

### Blind Test
|Result |Description|
|--------------|-----------------------------------------|
| **YES-** | Test case 1 is correct (below limit green) |  
| **YES-** | Test case 2 is correct (below limit blue) |   
| **YES-** | Test case 3 is correct (purple) |   
| **YES-** | Test case 4 is correct (Blue capitalized) |    
| **YES-** | Test case 5 correct (Green over limit with coupon) |   
| **YES-** | Test case 6 correct (Blue over limit) |   
| **YES-** | Test case 7 correct (Green over limit without coupon) |   
| **YES-** | Test case 8 is correct (incorrect package) |   
| **YES-** | Program clearly states the purpose in the output |   
| **YES-** | Input prompts are clear |   
| **YES-** | Price output is formatted to 2 decimal places |  

### Open Test
|Result |Description|
|--------------|-----------------------------------------|
|**-NO**| The algorithm matches the code   |
|**YES-**| There is a block of introductory comments at the top |  
|**YES-**| Purpose of the program is clearly stated |  
|**YES-**| There are comments in the code|
|**YES-**| Code uses round function or an f-string for formatting total|
|**YES-**| Code uses .lower or .upper on the package name|   
|**YES-**| Total price is output in only one place|


### Documents for Participation Grade

|Result         |Type            |
|---------------|----------------|
|**YES-** | Reflection 1   |
|**YES-** | Reflection 2   |
|**YES-** | Algorithm      |
|**YES-** | Test case   |

### Comments on the grading
- Number 7 in your algorithm and the code doesn't actually. match You could have, if else, a statement and other things 
- 
- 
### Lab Grade: E

#### Participation Grade: S
 - If participation grade is unsatisfactory check the `NO` in the documents sections
