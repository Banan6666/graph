import pandas as pd

data = pd.DataFrame({'whoAmI': ['human', 'robot', 'human', 'human', 'robot']})

one_hot = pd.get_dummies(data['whoAmI'])

unique_values = data['whoAmI'].unique()

one_hot_manual = pd.DataFrame()

for value in unique_values:
    one_hot_manual['is_' + value] = (data['whoAmI'] == value).astype(int)

one_hot_manual.head()