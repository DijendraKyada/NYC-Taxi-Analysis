# IA626_ParkingViolation

### Question:
Â
__In this project we will analyze a dataset which contains information about taxi rides in NYC.  The data set is quite large so getting a basic idea of what the data contains is important.  Each student should use one of the CSV files.  Answer the following questions:__

1. What time range does your data cover?  How many rows are there total?
2. What are the field names?  Give descriptions for each field.
3. Give some sample data for each field.
4. What MySQL data types would you need to store each of the fields? [int(xx), varchar(xx),date, datetime, bool, decimal(m, d)]
5. What is the geographic range of your data (min/max - X/Y)? Plot this (approximately on a map)
6. What are the distinct values for each field? (If applicable)
7. For other numeric types besides lat and lon, what are the min and max values?
8. Create a chart which shows the average number of passengers each hour of the day.
9. Create a new CSV file which has only one out of every thousand rows.
10. Repeat step 8 with the reduced dataset and compare the two charts.

## Introduction

__The dataset is from the file `taxi_data_7.csv` which is not linked in this repository due to its size. Following are the analysis as asked form the above section. Every section would have description, code, output and screenshots of the output as needed.__

Important imports:
```python
import csv
import time
from datetime import datetime
import matplotlib.pyplot as plt
```

Due to its large size we can load data as simple as shown below

```python
fn = 'Sources/trip_data_7.csv'
f = open(fn, "r")
reader = csv.reader(f)
```

### 1.a. Range of data cover

___Logic:___ Taxi trip has initial pickup time and then final dropoff time. Since this dataset has pickup time and dropoff time so we can say that this dataset ranges from minimum value of pickup time(the pickup time of the first ever trip in this dataset) till maximum value of dropoff time(dropoff time of the last trip ever made in this dataset).

Logical Code:

```python
pickuptime = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
dropofftime = datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S')

    if min_pickup_time is None:
        min_pickup_time = pickuptime
    elif pickuptime < min_pickup_time:
        min_pickup_time = pickuptime

    if max_dropoff_time is None:
        max_dropoff_time = dropofftime
    elif dropofftime > max_dropoff_time:
        max_dropoff_time = dropofftime
```
Output:
>![Fields Names in the DataSet](/Images/DataRange.png)

>___`Data Ranges from 2013-07-01 00:00:00 (this time is highly unlikely but it could be possible that a taxi picked up some one at that particular time) and till 2013-08-03 13:14:30`___


### 1.b. Number of Rows in this data set

___Logic:___ Since I am running a single loop for most of the stuff I could just have a counter variable to count the number of rows in that loop.

In a standalone loop it could be as following:

```python
number_of_rows = 0
for row in reader:
    number_of_rows += 1

# subtracting number_of_rows by 1 as first row was header
print("# of rows:", number_of_rows-1)
```

>___`This Dataset has 13,823,840 rows`___

### 2. Field names and Description

___Logic:___ We can show the field names by showing the data of the 1st row (0th Index)

>![Fields Names in the DataSet](/Images/FieldNames.png)

__Field Names__ | __Description__
-------------|------------
Medallion |Permit number to operate the taxi
Hack License|A New York City Taxi Drivers License number
Vendor ID|Code of the provider associated with the trip
Rate Code|
Store and Fwd Flag|
Pickup Datetime|Pickup date and time when the meter was engaged
Dropoff Datatime|Drop off date and time when the meter was disengaged
Passenger Count|Number of passenger in a particular trip
Trip time in secs| Time in seconds taken to complete the trip
Trip Distance|Distance covered to complete the trip
Pickup Longitude|Pickup geographic Longitude
Pickup Latitude|Pickup geographic Latitude
Dropff Longitude|Drop off geographic Longitude
Dropoff Latitude|Drop off geographic Latitude

### 3. Some Sample DataSet

___Logic:___ We can iterated the loop till 5 rows to show some sample data

Logical Code:
```python
n=0
for row in reader:
  n=+1
  #first row would be header
  print(row)
  if n > 6
    break:
```
Output:

>![Sample Data from Dataset](/Images/SampleData.png)


### 4. MySQL data used to store each of the fields

Following is the table showcasing what datatypes and their range could be use to store each fields

__Field Names__ | __MySQL DataType__
-------------|------------
medallion |
hack_license|
vendor_id|
rate_code|
store_and_fwd_flag|
pickup_datetime|
dropoff_datatime|
passenger_count|
trip_time_in_secs|
trip_distance|
pickup_longitude|
pickup_latitude|
dropff_longitude|
dropoff_latitude|

### 5. Geographic Ranges

___Logic:___ Finding minimum and maximum of latitude and longitude for pickup and dropoff is fairly simple as we just have to provide limit - `Latitude goes from -90 to 90` and `Longitude goes from -180 to 180`. But since this dataset is of New York city we can bound the conditions of latidude and longitude accordingly. The boundary of NYC is `min_lat = 40.5774, max_lat = 40.9176, min_long = -74.15, max_long = -73.7004`. We have to do some addition check as some data had N/A or null values.

Logical Code:
```python
if row[10] != '' and row[11] != '' and row[12] != '' and row[13] != '':
        pickup_lon = float(row[10])
        pickup_lat = float(row[11])
        dropoff_lon = float(row[12])
        dropoff_lat = float(row[13])

        # min and max dropoff
        if pickup_min_lon is None and pickup_min_lat is None and pickup_max_lon is None and pickup_max_lat is None:
            pickup_min_lon = pickup_lon
            pickup_min_lat = pickup_lat
            pickup_max_lon = pickup_lon
            pickup_max_lat = pickup_lat
        elif pickup_lat <= 40.9176 and pickup_lat >= 40.5774 and pickup_lon <= -73.7004 and pickup_lon >= -74.15:
            if pickup_min_lon > pickup_lon and pickup_min_lat > pickup_lat:
                pickup_min_lon = pickup_lon
                pickup_min_lat = pickup_lat
            if pickup_max_lon < pickup_lon and pickup_max_lat < pickup_lat:
                pickup_max_lon = pickup_lon
                pickup_max_lat = pickup_lat

        # min and max dropoff
        if dropoff_min_lon is None and dropoff_min_lat is None and dropoff_max_lon is None and dropoff_max_lat is None:
            dropoff_min_lon = dropoff_lon
            dropoff_min_lat = dropoff_lat
            dropoff_max_lon = dropoff_lon
            dropoff_max_lat = dropoff_lat
        elif dropoff_lat <= 40.9176 and dropoff_lat >= 40.5774 and dropoff_lon <= -73.7004 and dropoff_lon >= -74.15:
            if dropoff_min_lon > dropoff_lon and dropoff_min_lat > dropoff_lat:
                dropoff_min_lon = dropoff_lon
                dropoff_min_lat = dropoff_lat
            if dropoff_max_lon < dropoff_lon and dropoff_max_lat < dropoff_lat:
                dropoff_max_lon = dropoff_lon
                dropoff_max_lat = dropoff_lat
```

For graphing this min max points we can use use `matplotlib` library. I first took a screenshot of the map with the same boundary coordinates given above form this webside: `https://www.openstreetmap.org/export#map=5/51.500/-0.100`. And then plot using scatter.

Visual Code:
```python
# plotting min and max pickup and dropoff on map
nyc = plt.imread("Images/NYC.png")
bound = (-74.15, -73.7004, 40.5774, 40.9176)
fig, ax = plt.subplots(figsize=(13.14, 13.10))
ax.scatter(pickup_min_lon, pickup_min_lat, c='green',
           s=30, label='Min Pickup', marker='s')
ax.scatter(pickup_max_lon, pickup_max_lat, zorder=1, alpha=0.9, c='blue',
           s=30, label='Max Pickup', marker='s')
ax.scatter(dropoff_min_lon, dropoff_min_lat, zorder=1,
           alpha=0.9, c='red', s=30, label='Min Dropoff', marker='s')
ax.scatter(dropoff_max_lon, dropoff_max_lat, zorder=1,
           alpha=0.9, c='brown', s=30, label='Max Dropoff', marker='s')
ax.set_title('Plotting on Map')
ax.set_xlim(-74.15, -73.7004)
ax.set_ylim(40.5774, 40.9176)
ax.legend(loc=4)
ax.imshow(nyc, extent=bound)
```

Output:
>![Sample Data from Dataset](/Images/GeoMinMax.png)


### 6. Distinct Values for each fields


### 7. Minimum and Maximum value of the following the following fields


### 8. Average number of passengers each hour of the day


### 9. New CSV file which has one out of every thousand rows for the Taxi trip DataSet


### 10. Comparing data set - with step 8 and 9
