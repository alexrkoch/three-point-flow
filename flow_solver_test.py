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