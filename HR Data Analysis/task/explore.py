import pandas as pd
import requests
import os

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
            'B_office_data.xml' not in os.listdir('../Data') and
            'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here
    """
    1/5: DataFrame A
    """
    dfA = pd.read_xml('../Data/A_office_data.xml')
    dfA['employee_office_id'] = dfA['employee_office_id'].map(lambda z: 'A' + str(z))
    dfA.set_index('employee_office_id', inplace=True)
    dfA_list = list(dfA.index)

    """
    1/5: DataFrame B
    """
    dfB = pd.read_xml('../Data/B_office_data.xml')
    dfB['employee_office_id'] = dfB['employee_office_id'].map(lambda z: 'B' + str(z))
    dfB.set_index('employee_office_id', inplace=True)
    dfB_list = list(dfB.index)

    """
    1/5: reindexing DataFrame HR
    """
    dfHR = pd.read_xml('../Data/hr_data.xml')
    dfHR.set_index('employee_id', inplace=True)
    dfHR_list = list(dfHR.index)

    """
    1/5: print dataframe A,B,HR
    """
    # print(dfA_list)
    # print(dfB_list)
    # print(dfHR_list)

    """
    2/5: join dataframes A,B
    """
    dfAB = pd.concat([dfA, dfB])
    # dfAB = pd.merge(dfA, dfB, how='inner', on='employee_office_id')
    # print(dfAB.shape,dfAB.index.name, [*dfAB.columns], sep=',\t')

    """
    2/5: merge dataframes AB with HR on their indexes
    """
    dfAB_HR = dfAB.merge(dfHR, how='inner', left_index=True, right_index=True,
                         indicator=True)  # merges only rows that are in both AB and HR
    dfABhr = dfAB_HR.drop(columns=['_merge'])  # removes column created by 'indicator' attribute in merge()
    dfABhr = dfABhr.sort_index()
    # dfABhr = dfABhr.sort_index(
    #     key=lambda idx: pd.MultiIndex.from_arrays([
    #         idx.str[0],  # alphabetical part
    #         idx.str[1:].astype(int)  # numeric part
    #     ])
    # )

    # print(list(dfABhr.index))
    # print(list(dfABhr.columns))

    """
    3/5: sort by column and pick top ten
    """
    dfSelection = dfABhr.sort_values(['average_monthly_hours'], ascending=False)['Department'][0:10]
    departments = list(dfSelection)
    # print(departments)

    """
    3/5: Filter database and aggregate, sum(), from one selected column
    """
    result = dfABhr.query("Department == 'IT' & salary == 'low'").number_project.agg('sum')
    # print(result)

    """
    3/5: Find certain rows and select values from selected columns
    """
    df_rows = dfABhr.loc[['A4', 'B7064', 'A3033'], ['last_evaluation', 'satisfaction_level']].values.tolist()
    # print(df_rows)

    """
    4/5: Aggregate function, metrics
    """


    def count_bigger_5(series):
        return (series > 5).sum()


    metrics = dfAB_HR.groupby('left').agg({
        'number_project': ['median', count_bigger_5],
        'time_spend_company': ['mean', 'median'],
        'Work_accident': 'mean',
        'last_evaluation': ['mean', 'std']
    })

    metrics = metrics.round(2)

    # print(metrics.to_dict())

    """
    5/5: Pivot tables:
        1. department/left,salary/average_monthly_hours - median
        2. time_spend_company/promotion_last_5years/satisfaction_level,last_evaluation - min, max, mean
    """
    dfPivot1 = dfAB_HR.pivot_table(index='Department', columns=['left', 'salary'], values='average_monthly_hours',
                                   aggfunc='median').round(2)

    dfPivot2 = dfAB_HR.pivot_table(index='time_spend_company', columns='promotion_last_5years',
                                   values=['satisfaction_level', 'last_evaluation'],
                                   aggfunc=['min', 'max', 'mean']).round(2)

    """
    5/5: Pivot tables: selection, filtering, printing as dictionary
    """
    pivot1 = dfPivot1.loc[
        (dfPivot1[(0, 'high')] < dfPivot1[(0, 'medium')]) | (dfPivot1[(1, 'low')] < dfPivot1[(1, 'high')])]

    pivot2 = dfPivot2.loc[(dfPivot2[('mean', 'last_evaluation', 0)] > dfPivot2[('mean', 'last_evaluation', 1)])]

    print(pivot1.to_dict())
    print(pivot2.to_dict())
