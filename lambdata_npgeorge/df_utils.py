"""
utility functions for working with DataFrames
"""

import pandas as pd
import numpy as np

#from example in class
#TEST_DF = pandas.DataFrame([1,2,3,np.nan,4])

#made up data
df = pd.DataFrame({
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'DoB': ['12/20/1991', '05/04/1988', '06/18/1974', '08/29/1980', '11/03/1965'],
    'siblings': [2,3,1,np.nan,3]
})

#checking data frames for nulls
missing = raw_data.isnull().values.any()
print(missing)

#function to split dates into month, day, and year
def wrangle(X):
  
    #breaking out month
    X['month'] = X.DoB.astype(str).str[:2].astype(int)
    #days
    X['day'] = X.DoB.astype(str).str[3:5].astype(int)
    #years
    X['year'] = X.DoB.astype(str).str[6:].astype(int)

    # return the wrangled dataframe
    return X

df = wrangle(df)
