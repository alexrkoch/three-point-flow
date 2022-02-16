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

df = load_data()

def define_head_rank(df):
  # highest head 'head_rank'= 1.0, lowest = 3.0
  df['head_rank'] = df.iloc[:, 2].rank(ascending = 0)
  df = df.set_index('head_rank')
  return df

df = define_head_rank(df)
print(df.head())



# Verify numbers are acceptable (all are numbers, coordinates are positive), leaving this to the end

# Identify which wells have the highest lowest and middle head 

# Calculate distance between highest and lowest using geopy
  # geopy.distance.distance example:
    # newport_ri = (41.49008, -71.312796)
    # cleveland_oh = (41.499498, -81.695391)
    # print(distance.distance(newport_ri, cleveland_oh).feet)

# Calculate point on that line of equipotential with middle head

# Calculate azimuthal direction of flow normal to the equipotential line
