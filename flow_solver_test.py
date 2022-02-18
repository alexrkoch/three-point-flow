import pytest
import pandas as pd
from geopy import distance, point
import flow_solver as fs


def test_load_data():
  df = fs.load_data()
  assert type(df.iloc[0]) == int or float

def test_define_head_rank():
  df = fs.load_data()
  df = fs.define_head_rank(df)
  assert df.loc[1.0].iloc[2] >= df.loc[2.0].iloc[2] >= df.loc[3.0].iloc[2]

def test_create_geopy_points():
  df = fs.load_data()
  df = fs.define_head_rank(df)
  low_point, mid_point, high_point = fs.create_geopy_points(df)
  assert low_point.latitude == 35.765707

def test_create_head_variables():
  df = fs.load_data()
  df = fs.define_head_rank(df)
  low_head, mid_head, high_head = fs.create_head_variables(df)
  assert low_head == 360

def test_length_low_to_high():
  df = fs.load_data()
  df = fs.define_head_rank(df)
  low_point, mid_point, high_point = fs.create_geopy_points(df)
  length = fs.length_low_to_high(low_point, high_point)
  assert length == 264.9634085161976

def test_get_bearing():
  df = fs.load_data()
  df = fs.define_head_rank(df)
  low_point, mid_point, high_point = fs.create_geopy_points(df)
  length = fs.length_low_to_high(low_point, high_point)
  bearing = fs.get_bearing(low_point, high_point)
  assert round(bearing) == 286

def test_equipotential_midpoint():
  df = fs.load_data()
  df = fs.define_head_rank(df)
  low_point, mid_point, high_point = fs.create_geopy_points(df)
  length = fs.length_low_to_high(low_point, high_point)
  bearing = fs.get_bearing(low_point, high_point)
  equipotential_point = fs.equipotential_midpoint(length, bearing)
  assert round(equipotential_point.latitude, 6) == 35.765818
  assert round(equipotential_point.longitude, 6) == -78.723905

def test_get_flow_azimuth():
  df = fs.load_data()
  df = fs.define_head_rank(df)
  low_point, mid_point, high_point = fs.create_geopy_points(df)
  length = fs.length_low_to_high(low_point, high_point)
  bearing = fs.get_bearing(low_point, high_point)
  equipotential_point = fs.equipotential_midpoint(length, bearing)
  flow_azimuth = fs.get_flow_azimuth(mid_point, equipotential_point, low_point)
  assert flow_azimuth == 91