import math
import pandas as pd
from geopy import distance, point

def get_flow_direction_from_three_wells(df):
  df = __define_head_rank(df)
  low_point, mid_point, high_point = __create_geopy_points(df)
  length = __length_low_to_high(high_point, low_point)
  bearing = __get_bearing(low_point, high_point)
  low_head, mid_head, high_head = __create_head_variables(df)
  equipotential_point = __equipotential_midpoint(length, bearing)
  flow_azimuth = __get_flow_azimuth(mid_point, equipotential_point, low_point)
  return flow_azimuth

def __load_data():
  try:
    df = pd.read_csv('input.csv', header=None)
    print("Input data loaded successfully!")
  except:
    df = pd.read_csv('sample-data.csv', header=None)
    print("No input data found, using sample data.")
  return df

def __define_head_rank(df):
  # highest head 'head_rank'= 1.0, lowest = 3.0
  df['head_rank'] = df.iloc[:, 2].rank(ascending = 0)
  df = df.set_index('head_rank')
  return df

def __create_geopy_points(df):
  low_point = point.Point(df.loc[3.0].iloc[0], df.loc[3.0].iloc[1])
  mid_point = point.Point(df.loc[2.0].iloc[0], df.loc[2.0].iloc[1])
  high_point = point.Point(df.loc[1.0].iloc[0], df.loc[1.0].iloc[1])
  return low_point, mid_point, high_point

def __create_head_variables(df):
  high_head = df.loc[1.0].iloc[2]
  mid_head = df.loc[2.0].iloc[2]
  low_head = df.loc[3.0].iloc[2]
  return low_head, mid_head, high_head

def __length_low_to_high(low_point, high_point):
  return distance.distance(low_point, high_point).feet

def __get_bearing(start_point, end_point):
    # Function copied from YAFS (https://www.programcreek.com/python/?project_name=acsicuib%2FYAFS)
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
            # math.tau instead of 2.0 * math.pi
            d_lng = -(2.0 * math.pi - d_lng)
        else:
            d_lng = (2.0 * math.pi + d_lng)

    tan_start = math.tan(start_lat / 2.0 + math.pi / 4.0)
    tan_end = math.tan(end_lat / 2.0 + math.pi / 4.0)
    d_phi = math.log(tan_end / tan_start)
    bearing = (math.degrees(math.atan2(d_lng, d_phi)) + 360.0) % 360.0
    bearing = round(bearing)
    return bearing

def __equipotential_midpoint(length, bearing):
  sub_distance = ((mid_head - low_head) / (high_head - low_head)) * length
  return distance.distance(feet=sub_distance).destination((low_point), bearing=bearing)

def __get_flow_azimuth(mid_point, equipotential_point, low_point):
  equipotential_bearing = get_bearing(equipotential_point, mid_point)
  equipotential_to_low_bearing = get_bearing(equipotential_point, low_point)

  # create the two possible flow direction scenarios, both normal to the equipotential head line.
  eb_plus = equipotential_bearing + 90
  eb_minus = equipotential_bearing - 90

  # correct for values outside of azimuth range
  # consider replacing with mod 360.
  # eb_plus = eb_plus % 360
  # eb_minus = eb_minus % 360
  # eb_plus %= 360
  if eb_plus >= 360:
    eb_plus -= 360
  if eb_minus < 0:
    eb_minus += 360
  
  # determine which makes an acute angle with equipotential_to_low_bearing.
  if equipotential_to_low_bearing < eb_plus:
    angle_plus = equipotential_to_low_bearing - eb_plus
  else: 
    angle_plus = eb_plus - equipotential_to_low_bearing
  angle_plus = abs(angle_plus)
  if angle_plus > 180:
    angle_plus = abs(angle_plus - 360)
  if angle_plus < 90:
    return eb_plus
  elif angle_plus == 90:
    return equipotential_to_low_bearing
  else:
    return eb_minus