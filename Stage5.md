# Stage 5/5: Draw up pivot tables
## Description
The HR boss desperately needs your pivot tables for their report.
1. The first pivot table displays `Department` as rows. For columns, it displays employees' current status(`left`), and their `salary`.  
   The values should be the median number of monthly hours(`average_monthly_hours`) employees have worked. In the table,  
   the HR boss wants to see only those departments where either one is true:  

   - For the currently employed: the median value of the working hours of high-salary employees is smaller than medium-salary employees, OR:
   - For the employees who left: the median value of working hours of low-salary employees is smaller than high-salary employees.

2. The second pivot table is where each row is an employee's time in the company(`time_spend_company`); the columns indicate  
   whether an employee has had any promotion(`promotion_last_5years`). The values are the `minimum`, `maximum`, and `mean` of `last_evaluation`  
   and `satisfaction_level`. Filter the table by the following rule: select only those rows where the mean value of `last_evaluation`  
   is higher for those without promotion than those who had promotion.

## Objectives
Continue using your code from Stage 2 which successfully sorts the dataset by index. On top of that, implement the following features:
1. Use `df.pivot_table()` to generate the **first pivot table**: `Department` as **index**, `left` and `salary` as **columns**,
`average_monthly_hours` as **values**. Store **median** values in the table.
2. Use `df.pivot_table()` to generate the **second pivot table**: `time_spend_company` as **index**, `promotion_last_5years` as **column**,
`satisfaction_level` and `last_evaluation` as **values**. Store the **min**, **max**, and **mean** values in the table.
3. Use the search methods to subset the data as requested in the Description section. Round all the numbers to two
decimals;
4. Print two resulting DataFrames as Python dictionaries. To do so, use the `to_dict()` method.

## Example
_Input: a merged DataFrame_

_Output (the answer is for reference only; the actual values may differ):_

_Resulting DataFrames:_

```

left 0.0 1.0
salary high low medium high low medium
Department
IT 185.0 177.5 196.0 155.0 235.0 197.0
management 203.0 199.0 201.0 231.0 155.5 235.0

```

```

              max                                           mean        \

last_evaluation satisfaction_level last_evaluation
0 1 0 1 0 1
2 1.0 0.99 1.0 0.94 0.72 0.69
7 1.0 0.90 1.0 0.94 0.77 0.75

                                       min

satisfaction_level last_evaluation satisfaction_level
0 1 0 1 0 1
2 0.70 0.65 0.37 0.52 0.09 0.29
7 0.48 0.60 0.36 0.42 0.09 0.15

```

_Resulting dictionaries:_

```

{(0.0, 'high'): {'IT': 185.0,
'management': 203.0},
(0.0, 'low'): {'IT': 177.0,
'management': 199.0},
(0.0, 'medium'): {'IT': 196.0,
'management': 201.0},
(1.0, 'high'): {'IT': 155.0,
'management': 231.0},
(1.0, 'low'): {'IT': 235.0,
'management': 155.0},
(1.0, 'medium'): {'IT': 197.0,
'management': 235.0}}

```

```

{('max', 'last_evaluation', 0): {2: 1.0, 7: 1.0},
('max', 'last_evaluation', 1): {2: 0.99, 7: 0.9},
('max', 'satisfaction_level', 0): {2: 1.0, 7: 1.0},
('max', 'satisfaction_level', 1): {2: 0.94, 7: 0.94},
('mean', 'last_evaluation', 0): {2: 0.72, 7: 0.77},
('mean', 'last_evaluation', 1): {2: 0.69, 7: 0.75},
('mean', 'satisfaction_level', 0): {2: 0.7, 7: 0.48},
('mean', 'satisfaction_level', 1): {2: 0.65, 7: 0.6},
('min', 'last_evaluation', 0): {2: 0.37, 7: 0.36},
('min', 'last_evaluation', 1): {2: 0.52, 7: 0.42},
('min', 'satisfaction_level', 0): {2: 0.09, 7: 0.09},
('min', 'satisfaction_level', 1): {2: 0.29, 7: 0.15}}

```