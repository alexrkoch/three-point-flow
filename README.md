# three-point-flow

Calculate groundwater flow direction given 3 hydraulic head measurements at
different wells.

## Data Input

- You can provide your own data or run the program with the sample dataset.
- To use your own data, store the data in the root directory in file called
  `input.csv`. If you provide no `input.csv` file, the program will
  automatically use the sample dataset.
- Input data from exactly 3 well locations.
- Data from each well should be stored in a new row, with no row labels, and in
  the order: `latitude, longitude, hydraulic head`. For example:
  ```
  lat, lon, head
  lat, lon, head
  lat, lon, head
  ```
- Latitude and longitude should use the WGS-84 datum, and be in decimal format.
  This is what you get from Google Maps, which is the source of all sample data
  for this project.
- Hydraulic head must have units of `feet`. For fractions of a foot use decimals
  (e.g., for 10' 6" use 10.5 feet)
