import pandas as pd
import os
import statistics

csv_file = 'us-500.csv'
csv_path = f'{os.getcwd()}\{csv_file}'
df = pd.read_csv(csv_path, header=None)
n_rows, n_col = df.shape
n_rows -= 1
n_col -= 1


def function1():
    print(f'Filter file by Rows (0-{n_rows}) and Columns (0-{n_col}).\n')
    
    start_r, end_r, start_c, end_c = int, int, int, int
    while True:
        start_r = int(input(f'Please choose start row: '))
        end_r = int(input(f'Please choose end row: '))
        if start_r < 0 or end_r > n_rows:
            print("\nRow(s) out of range, please try again.\n")
        else:
            break

    while True:
        start_c = int(input(f'Please choose start column: '))
        end_c = int(input(f'Please choose end column: '))
        if start_c < 0 or end_c > n_col:
            print("\Column(s) out of range, please try again.\n")
        else:
            break

    r = [start_r, end_r]
    c = [start_c, end_c]

    return (r, c)

def checkType(val):
    options = ['Data', 'Address', 'Phone No.']
    addr_signs = ['st', 'dr', 'ave' ,'blvd']

    val_split = val.split()
    for x in val_split:
        
        # Address check
        # Check if string contains signs of address.
        if x.lower() in addr_signs:
            return options[1]

        # Phone No. check
        # US phone No. format xxx-xxx-xxxx
        # Check if string contains dash.
        if '-' in x:
            return options[2]
    
    # Data (Others)
    return options[0]


# function2 checks the column type.
# Input arguement, DataFrame.
# Return, list of column types. 
def function2(data):
    to_return = []
    temp = [[] for i in range(n_col + 1)]
    for idx, row in data.iterrows():
        for i in range(len(row)):
            temp[i].append(checkType(row[i]))
 
    for x in temp:
        most_common = statistics.mode(x) 
        to_return.append(most_common)
    return to_return


def main():
    print(f"\n\n\n\n\n\n{' CSV Exercise ':*^40}")

    print(f"\n\n{' Columns ':-^40}")
    print(function2(df))
    
    print(f"\n\n{' Filter ':-^40}")
    r, c = function1()
    print(df.iloc[r[0]:r[1]+1, c[0]:c[1]+1])

    
    

main()