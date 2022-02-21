import flow_solver as fs
import pandas as pd

def __load_data():
  try:
    df = pd.read_csv('/app/input.csv', header=None)
    print("Input data loaded successfully!")
  except:
    df = pd.read_csv('/app/sample-data.csv', header=None)
    print("No input data found, using sample data.")
  return df

if __name__ == '__main__':
  df = __load_data()
  flow_azimuth = fs.get_flow_direction_from_three_wells(df)
  print(f"Groundwater in the area is flowing towards an azimuth of {flow_azimuth}\N{DEGREE SIGN}")