import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    #sorted_salaries = unique_salaries
    if 2 > len(sorted_salaries):
        return pd.DataFrame({'SecondHighestSalary': [None]})
    second_highest = sorted_salaries.iloc[1]
    return pd.DataFrame({'SecondHighestSalary' : [second_highest]})
