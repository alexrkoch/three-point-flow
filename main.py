import flow_solver

def load_data():
  try:
    df = pd.read_csv('input.csv', header=None)
    print("Input data loaded successfully!")
  except:
    df = pd.read_csv('sample-data.csv', header=None)
    print("No input data found, using sample data.")
  return df

if __name__ == '__main__':
  df = load_data()
  flow_azimuth = get_flow_direction_frome_three_wells(df)
  print(f"Groundwater in the area is flowing towards an azimuth of {flow_azimuth}\N{DEGREE SIGN}")