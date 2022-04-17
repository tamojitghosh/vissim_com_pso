import pandas as pd

# with open("Simple_Network_001.mer", 'r') as fp:
#     lines = fp.readlines()
# with open("Simple_Network_001.mer", 'w') as fp:
#     for number, line in enumerate(lines):
#         if number not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#             fp.write(line)

df = pd.read_table("Simple_Network_001.mer", sep=';')

df.columns = df.columns.str.strip()
df1 = df.sort_values(by=['VehNo'])
df2 = df1.loc[:, ~df.columns.str.contains('^Unnamed')]
print(df2.to_string())
