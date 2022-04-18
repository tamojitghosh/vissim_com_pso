import pandas as pd
filename = "Simple_Network_001.mer"

with open(filename, 'r') as fp:
    lines = fp.readlines()  # reading the output file from vissim
with open(filename, 'w') as fp:
    for number, line in enumerate(lines):
        if number not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            fp.write(line)  # deleting the initial unwanted lines

df = pd.read_table(filename, sep=';')  # delimiting the dataframe by semicolon
df.columns = df.columns.str.strip()  # removing the space between the columns
df1 = df.sort_values(by=['VehNo'])  # sorting the dataframe by vehicle number
df2 = df1.loc[:, ~df.columns.str.contains('^Unnamed')]  # removing columns with no data 'unnamed'
df3 = df2[df2['t(Exit)'] != -1.00]  # removing the rows with -1 value in t(Exit)

print(df3.to_string())
