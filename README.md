# Three Point Flow

Calculate groundwater flow direction given 3 hydraulic head measurements at
different wells.

## Docker Image

The docker image for this project can be found in my Docker Hub Repository:
https://hub.docker.com/repository/docker/alexrkoch/three-point-flow

The dockerized version of the program only runs the sample data. To run the
Docker image make sure Docker is running, then simply enter into the command
line:

```
docker run alexrkoch/three-point-flow
```

To use your own input data:

1. Clone this repo to your local machine.
2. Follow the steps below in **Data Input** to make sure your data format is
   correct.
3. Install the dependencies in `requirements.txt`.
4. Run `main.py`.

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
