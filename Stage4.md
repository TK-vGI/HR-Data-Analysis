# Stage 4/5: Aggregate the data
## Description
The HR boss wants to delve into the metrics of the two employee groups: those who left the company and those who still work for us.  
You decided to present the information in a table.

The HR boss asks for the following metrics:
* the **median** `number of projects` the employees in a group worked on, and how many employees worked on **more than** 5 projects;
* the **mean** and **median** `time spent in the company`;
* the share of employees who've had `work accidents`;
* the **mean** and **standard deviation** of the `last evaluation` score.

Remember that the guy from HR asks for those metrics for two different groups!

## Objectives
Continue using your code from Stage 2 which successfully sorts the dataset by index. On top of that, implement the following features:
1. Write the `count_bigger_5` function that counts the number of employees who worked on more than five projects. You will  
   then use it in the `agg()` method to calculate the metric from the first point in the Description section;
2. Use `groupby()` with **left** column and `agg()` to generate a table with metrics according to the boss's needs (refer to example for the metrics);
3. Round all the numbers to two decimals. To round numbers to the second decimal place, you can apply the `round(2)` method to a `DataFrame`;
4. Print the resulting table as a Python dictionary. To do so, use the `to_dict()` method.

## Example
_Input: a merged DataFrame_

_Output (the answer is for reference only; the actual values may differ):_

_DataFrame:_

```

    number_project           time_spend_company   Work_accident   last_evaluation
     median count_bigger_5        mean   median        mean          mean   std
left
0.0      3.0            120       2.40    3.0          0.24          0.64  0.25
1.0      5.0            85        4.85    4.0          0.11          0.77  0.13

```

_Resulting dictionary:_

```

{('number_project', 'median'): {0: 3, 1: 5},
 ('number_project', 'count_bigger_5'): {0: 120, 1: 85},
 ('time_spend_company', 'mean'): {0: 2.40, 1: 4.85},
 ('time_spend_company', 'median'): {0: 3.0, 1: 4.0},
 ('Work_accident', 'mean'): {0: 0.24, 1: 0.11},
 ('last_evaluation', 'mean'): {0: 0.64, 1: 0.77},
 ('last_evaluation', 'std'): {0: 0.25, 1: 0.13}}

```
