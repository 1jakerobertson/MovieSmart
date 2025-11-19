import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'col1': ['A', 'B', 'C'],
    'col2': ['1', '2', '3'],
    'col3': ['X', 'Y', 'Z']
})

# Join the columns using a separator (e.g., '-')
df['new_col'] = df['col1'].str.cat(df['col2'], sep='-').str.cat(df['col3'], sep='-')

print(df)
