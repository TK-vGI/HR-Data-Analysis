import pandas as pd
import requests
import os


# scroll down to the bottom to implement your solution

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
    DataFrame A
    """
    dfA = pd.read_xml('../Data/A_office_data.xml')
    dfA['employee_office_id'] = dfA['employee_office_id'].map(lambda z: 'A' + str(z))
    dfA.set_index('employee_office_id', inplace=True)
    dfA_list = list(dfA.index)

    """
    DataFrame B
    """
    dfB = pd.read_xml('../Data/B_office_data.xml')
    dfB['employee_office_id'] = dfB['employee_office_id'].map(lambda z: 'B' + str(z))
    dfB.set_index('employee_office_id', inplace=True)
    dfB_list = list(dfB.index)

    """
    reindexing DataFrame HR
    """
    dfHR = pd.read_xml('../Data/hr_data.xml')
    dfHR.set_index('employee_id', inplace=True)
    dfHR_list = list(dfHR.index)

    """
    print dataframe A,B,HR
    """
    # print(dfA_list)
    # print(dfB_list)
    # print(dfHR_list)

    """
    join dataframes A,B
    """
    dfAB = pd.concat([dfA, dfB])
    # dfAB = pd.merge(dfA, dfB, how='inner', on='employee_office_id')
    # print(dfAB.shape,dfAB.index.name, [*dfAB.columns], sep=',\t')

    """
    merge dataframes AB with HR on their indexes
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

    print(list(dfABhr.index))
    print(list(dfABhr.columns))