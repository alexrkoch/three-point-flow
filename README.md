# three-point-flow

Calculate groundwater flow direction given 3 hydraulic head measurements at
different wells.

## Data Input

- Store data in the root directory in file called `input.csv`
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
