import pytest
import pandas as pd
from geopy import distance, point
import flow_solver as fs

def test_define_head_rank():
  df = pd.DataFrame({"lat":[35.765909,35.765341,35.765707],
                     "lon":[-78.724288,-78.723918,-78.72343],
                     "head":[387.5,375.2,360]})
  df = fs.__define_head_rank(df)
  assert df.loc[1.0].iloc[2] >= df.loc[2.0].iloc[2] >= df.loc[3.0].iloc[2]

def test_create_geopy_points():
  df = pd.DataFrame({"lat":[35.765909,35.765341,35.765707],
                    "lon":[-78.724288,-78.723918,-78.72343],
                    "head":[387.5,375.2,360],
                    "head_rank":[1.0,2.0,3.0]})
  df = df.set_index('head_rank')
  low_point, mid_point, high_point = fs.__create_geopy_points(df)
  assert low_point.latitude == 35.765707

def test_create_head_variables():
  df = pd.DataFrame({"lat":[35.765909,35.765341,35.765707],
                    "lon":[-78.724288,-78.723918,-78.72343],
                    "head":[387.5,375.2,360],
                    "head_rank":[1.0,2.0,3.0]})
  df = df.set_index('head_rank')
  low_head, mid_head, high_head = fs.__create_head_variables(df)
  assert low_head == 360

def test_length_low_to_high():
  df = pd.DataFrame({"lat":[35.765909,35.765341,35.765707],
                    "lon":[-78.724288,-78.723918,-78.72343],
                    "head":[387.5,375.2,360],
                    "head_rank":[1.0,2.0,3.0]})
  df = df.set_index('head_rank')
  low_point, mid_point, high_point = fs.__create_geopy_points(df)
  low_head, mid_head, high_head = fs.__create_head_variables(df)
  length = fs.__length_low_to_high(low_point, high_point)
  assert length == 264.9634085161976

def test_get_bearing():
  df = pd.DataFrame({"lat":[35.765909,35.765341,35.765707],
                    "lon":[-78.724288,-78.723918,-78.72343],
                    "head":[387.5,375.2,360],
                    "head_rank":[1.0,2.0,3.0]})
  df = df.set_index('head_rank')
  low_point, mid_point, high_point = fs.__create_geopy_points(df)
  low_head, mid_head, high_head = fs.__create_head_variables(df)
  length = fs.__length_low_to_high(low_point, high_point)
  bearing = fs.__get_bearing(low_point, high_point)
  assert round(bearing) == 286

def test_equipotential_midpoint():
  df = pd.DataFrame({"lat":[35.765909,35.765341,35.765707],
                    "lon":[-78.724288,-78.723918,-78.72343],
                    "head":[387.5,375.2,360],
                    "head_rank":[1.0,2.0,3.0]})
  df = df.set_index('head_rank')
  low_point, mid_point, high_point = fs.__create_geopy_points(df)
  low_head, mid_head, high_head = fs.__create_head_variables(df)
  length = fs.__length_low_to_high(low_point, high_point)
  bearing = fs.__get_bearing(low_point, high_point)
  equipotential_point = fs.__equipotential_midpoint(low_point, low_head, mid_head, high_head,length, bearing)
  assert round(equipotential_point.latitude, 6) == 35.765818
  assert round(equipotential_point.longitude, 6) == -78.723905

def test_get_flow_azimuth():
  df = pd.DataFrame({"lat":[35.765909,35.765341,35.765707],
                    "lon":[-78.724288,-78.723918,-78.72343],
                    "head":[387.5,375.2,360],
                    "head_rank":[1.0,2.0,3.0]})
  df = df.set_index('head_rank')
  low_point, mid_point, high_point = fs.__create_geopy_points(df)
  low_head, mid_head, high_head = fs.__create_head_variables(df)
  length = fs.__length_low_to_high(low_point, high_point)
  bearing = fs.__get_bearing(low_point, high_point)
  equipotential_point = fs.__equipotential_midpoint(low_point, low_head, mid_head, high_head, length, bearing)
  flow_azimuth = fs.__get_flow_azimuth(mid_point, equipotential_point, low_point)
  assert flow_azimuth == 91

