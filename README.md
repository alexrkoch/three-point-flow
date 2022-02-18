# three-point-flow

Calculate groundwater flow direction given 3 hydraulic head measurements at
different wells.

## Data Input

- You can provide your own data or run the program with the sample dataset.
- To use your own data, store the data in the root directory in a file called
  `input.csv`. If you provide no `input.csv` file, the program will
  automatically use the sample dataset.
- Input data from exactly 3 well locations.
- Do not use column or row labels.
- Data from each well should be stored in a new row, and in the order:
  `latitude, longitude, hydraulic head`. For example:
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

## Calculation Method

1. Calculate the hydraulic gradient between the lowest and highest head wells.
2. Calculate the point between the lowest and highest head wells corresponding
   to the same head value of the middle head well. A line connecting the middle
   head well to this point now represents a contour line of equipotential
   hydraulic head.
3. Calculate the bearing of the equipotential line, in the line leading from the
   equipotential point to the lowest head well.
4. The flow direction is a bearning normal to the equipotential line going
   toward the lowest head well.Calculate two vectors normal to the equipotential
   line, then determine which one makes a smaller angle with the bearing leading
   towards the lowest head well.
