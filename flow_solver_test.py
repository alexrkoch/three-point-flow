import pytest
import numpy as np
import pandas as pd
from geopy import distance
import flow_solver as fs

# def test_add():
#   assert add(1,2) == 3

def test_data_has_numbers():
  df = fs.load_data()
  assert type(df.iloc[0]) == int or float