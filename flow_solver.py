import math
import pandas as pd
from geopy import distance, point

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

def length_low_to_high(df):
  highest = (df.loc[1.0].iloc[0], df.loc[1.0].iloc[1])
  lowest = (df.loc[3.0].iloc[0], df.loc[3.0].iloc[1])
  length = distance.distance(highest, lowest).feet
  return length

def create_geopy_points(df):
  low_point = point.Point(df.loc[3.0].iloc[0], df.loc[3.0].iloc[1])
  mid_point = point.Point(df.loc[2.0].iloc[0], df.loc[2.0].iloc[1])
  high_point = point.Point(df.loc[1.0].iloc[0], df.loc[1.0].iloc[1])
  return low_point, mid_point, high_point

def get_bearing(start_point, end_point):
    # Function from YAFS (https://www.programcreek.com/python/?project_name=acsicuib%2FYAFS)
    """
    Calculates the bearing between two points.

    Parameters
    ----------
    start_point: geopy.Point
    end_point: geopy.Point

    Returns
    -------
    point: int
        Bearing in degrees between the start and end points.
    """
    start_lat = math.radians(start_point.latitude)
    start_lng = math.radians(start_point.longitude)
    end_lat = math.radians(end_point.latitude)
    end_lng = math.radians(end_point.longitude)

    d_lng = end_lng - start_lng
    if abs(d_lng) > math.pi:
        if d_lng > 0.0:
            d_lng = -(2.0 * math.pi - d_lng)
        else:
            d_lng = (2.0 * math.pi + d_lng)

    tan_start = math.tan(start_lat / 2.0 + math.pi / 4.0)
    tan_end = math.tan(end_lat / 2.0 + math.pi / 4.0)
    d_phi = math.log(tan_end / tan_start)
    bearing = (math.degrees(math.atan2(d_lng, d_phi)) + 360.0) % 360.0

    return bearing

def find_equipotential_midpoint(df, length, bearing):
  # find sub distance
  high_lat = df.loc[1.0].iloc[0]
  high_lon = df.loc[1.0].iloc[1]
  high_head = df.loc[1.0].iloc[2]

  mid_lat = df.loc[2.0].iloc[0]
  mid_lon = df.loc[2.0].iloc[1]
  mid_head = df.loc[2.0].iloc[2]

  low_lat = df.loc[3.0].iloc[0]
  low_lon = df.loc[3.0].iloc[1]
  low_head = df.loc[3.0].iloc[2]
  sub_distance = ((mid_head - low_head) / 
                  (high_head - low_head)) * length


  equipotentialPoint = geopy.distance.distance(feet=sub_distance).destination((low_lon, low_lat), bearing=bearing)


# def get_flow_azimuth(df, equipotentialPoint)
  # find bearing from equipotentialPoint to middle head point

  # determine what direction the low point is in

  # add or subtract 90 from the equipotential bearing

df = load_data()
df = define_head_rank(df)
length = length_low_to_high(df)
low_point, mid_point, high_point = create_geopy_points(df)
bearing = get_bearing(low_point, high_point)

 
