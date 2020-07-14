import pandas as pd

df = pd.read_csv('resources/adult.resources', header=None)

# basic
print(df.size)
print(df.shape)

print(df.columns)
df.columns = ['age','workplace','fnlwgt','education','education-num','material-status','occupation',
              'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','wage']
print(df.columns)

print(df.dtypes)
print(df.head())
print(df.tail())

# summary
print(df.describe())
print(df.mean())
print(df.mode())

# details
print(df.education.unique())
print(df.education.value_counts())
print(df['wage'].value_counts())
print(df.groupby(['wage'])['age'].mean())
print(df.groupby(['wage'])['age'].std())
print(df['capital-gain'].corr(df['age']))
