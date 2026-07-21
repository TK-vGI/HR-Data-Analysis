# Stage 3/5: Get the insights
## Description
The HR boss needs to know some important details about the employees. Find out the answers to the following questions:
1. What are the departments of the top ten employees in terms of working hours?
2. What is the total number of projects on which IT department employees with low salaries have worked?
3. What are the last evaluation scores and the satisfaction levels of the employees `A4`, `B7064`, and `A3033`?

## Objectives
After successfully sorting in the previous stage, continue expanding your program by adding the functionalities listed below.  
Answer the questions from the description using the pandas built-in methods. Here is a little explanation for each question:
1. Use `average_monthly_hours` column to sort the dataset in descending order, select top 10 employees based on this sorted data  
   and output a Python list of **corresponding departments' names**;
2. Filter the database based on `IT` for `Department` column and `low` for `salary` column. Then, sum up the values from  
   the `number_project` column and output the **total number of projects** for this filtered database;
3. Finally find `last_evaluation` and `satisfaction_level` values for the employees `A4`, `B7064`, and `A3033`.  
   Output a Python list where each entry is a list of values of the last evaluation score and the satisfaction level of an employee.  
   The data for each employee should be specified in the same order as the employees' IDs in the question above.  
   Apply the .loc method of pandas to answer the question!

_We advise using Google before implementing a logic-intensive approach. The chances are there is a ready-to-use method  
in `pandas` that will solve the problem in one line._

Print answers to all three questions — each on a separate line.

## Example
_Input data:_  
    
_The merged DataFrame from the previous stage._  

_Output (the answer is for reference only; the actual values may differ):_
```
['hr', 'support', 'management', 'management', 'IT', 'sales', 'product_mng', 'product_mng', 'IT', 'technical']
653
[[0.65, 0.89], [0.72, 0.83], [0.55, 0.34]]
```