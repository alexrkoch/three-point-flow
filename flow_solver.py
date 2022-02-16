import numpy as np
import pandas as pd
from geopy import distance

def load_data():
  try:
    df = pd.read_csv('input.csv', header=None)
    print("Input data loaded successfully!")
  except:
    df = pd.read_csv('sample-data.csv', header=None)
    print("No input data found, using sample data.")
  return df

def define_head_rank(df):
  # highest head 'head_rank'= 1.0, lowest = 3.0
  df['head_rank'] = df.iloc[:, 2].rank(ascending = 0)
  df = df.set_index('head_rank')
  return df

def length_highest_to_lowest(df):
  highest = (df.loc[1.0].iloc[0], df.loc[1.0].iloc[1])
  lowest = (df.loc[3.0].iloc[0], df.loc[3.0].iloc[1])
  length = distance.distance(highest, lowest).feet
  return length



df = load_data()
df = define_head_rank(df)
print(length_highest_to_lowest(df))


# Calculate point on that line of equipotential with middle head

# Calculate azimuthal direction of flow normal to the equipotential line

# Verify numbers are acceptable (all are numbers, coordinates are positive), leaving this to the end