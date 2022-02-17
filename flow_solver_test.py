import pytest
import numpy as np
import pandas as pd
from geopy import distance
import flow_solver as fs


def test_data_has_numbers():
  df = fs.load_data()
  assert type(df.iloc[0]) == int or float

def test_define_head_rank():
  df = fs.load_data()
  df = fs.define_head_rank(df)
  assert df.loc[1.0].iloc[2] >= df.loc[2.0].iloc[2] >= df.loc[3.0].iloc[2]

def test_length_low_to_high():
  df = fs.load_data()
  df = fs.define_head_rank(df)
  length = fs.length_low_to_high(df)
  assert length == 264.9634085161976

def test_get_bearing():
  df = fs.load_data()
  df = fs.define_head_rank(df)
  length = fs.length_low_to_high(df)
  low_point, mid_point, high_point = fs.create_geopy_points(df)
  bearing = fs.get_bearing(low_point, high_point)
  assert bearing == 286.1800749096567

def test_equipotential_midpoint():
  df = fs.load_data()
  df = fs.define_head_rank(df)
  length = fs.length_low_to_high(df)
  low_point, mid_point, high_point = fs.create_geopy_points(df)
  bearing = fs.get_bearing(low_point, high_point)
  equipotential_point = fs.equipotential_midpoint(df, length, bearing)
  assert round(equipotential_point.latitude, 6) == 35.765819
  assert round(equipotential_point.longitude, 6) == -78.723904

