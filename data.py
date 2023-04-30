import pandas as pd

data = {'Name': ['Tony', 'Robert', 'John', 'Alice'],
        'Age': ['18', '19', '20', '21']
        }

df = pd.DataFrame(data, columns=['Name', 'Age'])

print(df)
df.to_csv('test.csv', index=False)
