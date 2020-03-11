# IA626_ParkingViolation

### Question:

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
import operator
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
Output and Result:
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

Result:

>___`This Dataset has 13,823,840 rows`___

### 2. Field names and Description

___Logic:___ We can show the field names by showing the data of the 1st row (0th Index)

>![Fields Names in the DataSet](/Images/FieldNames.png)

__Field Names__ | __Description__
-------------|------------
Medallion |Permit number to operate the taxi
Hack License|A New York City Taxi Drivers License number
Vendor ID|Code of the provider associated with the trip
Rate Code|Some Code of Rate. IT has Numerical value ranging from 1-15
Store and Fwd Flag|This flag indicates whether the trip record was held in vehicle memory before sending to the vendor
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
medallion | Varchar(50)
hack_license| Varchar(50)
vendor_id| Varchar(5)
rate_code| Varchar(5)
store_and_fwd_flag| Varchar(2)
pickup_datetime|Datetime
dropoff_datatime|Datetime
passenger_count|Int(2)
trip_time_in_secs|Float(8)
trip_distance|Float(8)
pickup_longitude|Float(8)
pickup_latitude|Float(8)
dropff_longitude|Float(8)
dropoff_latitude|Float(8)

### 5. Geographic Ranges

___Logic:___ Finding minimum and maximum of latitude and longitude for pickup and dropoff is fairly simple as we just have to provide limit - `Latitude goes from -90 to 90` and `Longitude goes from -180 to 180`. But since this dataset is of New York city we can bound the conditions of latitude and longitude accordingly. The boundary or `Bound Box` of NYC is `min_lat = 40.5774, max_lat = 40.9176, min_long = -74.15, max_long = -73.7004`. We have to do some addition check as some data had N/A or null values.

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

Results:
>___`Min Pickup Longitude: -74.098373, Min Pickup Latitude: 40.581219, Max Pickup Longitude: -73.776688, Max Pickup Latitude: 40.916344, Min Dropoff Longitude: -74.149223, Min Dropoff Latitude: 40.584255, Max Dropoff Longitude: -73.700539, Max Dropoff Latitude: 40.8559071`___

For graphing this min max points we can use use `matplotlib` library. I first took a screenshot of the map with the same boundary coordinates given above form this website: [OutStreetMap](https://www.openstreetmap.org/export#map=5/51.500/-0.100). And then plot using scatter.

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

We could also put those min max latitude and longitude of pickup and dropoff in google map to see where are they. Such as following:

__MinPickup__ | __MaxPickup__
---------------|---------------
![MinPickup](/Images/min_pickup.PNG) | ![MaxPickup](/Images/max_pickup.PNG)

__MinDropoff__ | __MaxDropoff__
---------------|---------------
![MinDropoff](/Images/min_dropoff.PNG) | ![MaxDropoff](/Images/max_dropoff.PNG)

### 6. Distinct Values for each fields

___Logic:___ Distinct values are use to analyze data in group. We could find distinct values of Medallion, Hack License, Vendor ID, Rate Code, Store and Fwd Flag, Pickup and Dropoff date times, Pickup and dropoff longitude and latitude. But There still would be a lot of data to do analysis. What we can do is, find distinct values and count their occurrence and show top 10 most occurred. In this case finding Distinct value of __Medallion, Hack License, Vendor Id and Rate code__ will most make sense. `Distinct values for Store and Fwd Flag are 'Y' and 'N' similar to its description `

Output:
>![Distinct Value and its count](/Images/Distinctvalueandcount.png)


The above logic can help us to identify that such as Hack_Licence number: `'CFCD208495D565EF66E7DFF9F98764DA'` made total of `2520` taxi trips, the highest amount of trips.

For showing top 10 most occurred items of the distinct values if have used sorted() method as following:

```python
sorted(medallion.items(), key=operator.itemgetter(1), reverse=True)[:10]
```

### 7. Minimum and Maximum value of the following the following fields

___Logic:___ We dealt with finding minimum and maximum values of Pickup/Dropoff Latitude and Longitude. Also we found out the data range covered by this data set i.e. finding minimum and maximum values of date and time. Besides this we can find minimum and maximum value of `Trip time in sec` and `Trip Distance`.

Output:
> ___`Minimum trip in sec: 1.0, Maximum trip in sec: 10800.0, Minimum trip distance: 0.01 and Maximum trip distance: 100.0`___

Trip as small as 1.0 second is highly unlikely but may be the meter was engaged and next second disengaged. This could be helpful in some scenario but not in ours.


### 8. Average number of passengers each hour of the day

___Logic:___ There are quite a few interpretation we can do on this dataset. We did one of that on latitude and longitude. Another analysis we could do is on number of passengers.

#### 1. Total number of passengers:
 Before we move any further lets just count the number of passenger. We can count as total number of passenger carried by a taxi in this dataset or total number of passenger took taxi trip in a given. I calculated total number of passengers who took taxi trips in this dataset in a given hour as this will help in further analysis.

 Code: I just used grouping for this.

 ```python
 # hourly passengers
     dt = int(row[5][11:13]) #gives hour: 00,01,02,....,23
     if row[7] != '' and int(row[7]) != 0:
         if dt in hour_passenger:
             hour_passenger[int(dt)] += int(row[7])
         else:
             hour_passenger[int(dt)] = int(row[7])

 ```

Above code return a dictionary. We could simply display this as a bar chat with use of following code:
```python
plt.bar(list(hour_passenger.keys()), hour_passenger.values(), color='grey')
plt.title('Passenger Count by hours')
plt.xlabel('Hours')
plt.ylabel('Count')
plt.show()
```

Output:
>![Hourly Passengers](/Images/Hour_Passenger.png)


Result:
> __From the chat we can see that in this data set hour 5th has least number of total passengers and hour 19th has most__


#### 2. Average number of passengers each hour of the day.
Asking this questions helps us to answer How many passengers on average are riding NYC's taxi on a given hour. We simply divide the count of passenger by hour with total number of days this data set.

Logic: Counting days:
```python
day = row[5][8:10] #gives day example 01,02,03,....,28/29/30/31
    if day in dist_day:
        dist_day[day] += 1
    else:
        dist_day[day] = 1
```
Finding average:
```python
no_of_days = len(dist_day)
avg_hour_day_passenger = {k: v / no_of_days for k, v in hour_passenger.items()}
```

Displaying this as bar chart:

```python
plt.bar(list(avg_hour_day_passenger.keys()), avg_hour_day_passenger.values(), color='green')
plt.title('Average number of passenger each hour of the day')
plt.xlabel('Hour')
plt.ylabel('Count')
plt.show()
```

Output:
>![Average number of passenger by hour each day](/Images/Avg_Hour_Day_Passengers.png)

Result:
> __From the chat we can see that in this data set on any given day hour 5th has least number of people riding taxi in NYC and at hour 19th the most__


#### 3. Average number of passenger by hour on a given day in a taxi

What if we want to find out what hours are busy? or what time of the day is fairly easy to get a taxi or what time of the day people commute through taxi the most? The easiest way is to find the total number of passenger by hour i.e. what we found in point 1. then average those numbers with the count of the hours.

Logic: Find total number of passengers by hour and counts of hours
```python
dt = int(row[5][11:13])

    if row[7] != '' and int(row[7]) != 0:
        if dt in hour_passenger:
            hour_passenger[int(dt)] += int(row[7])
            hour_count[int(dt)] += 1
        else:
            hour_passenger[int(dt)] = int(row[7])
            hour_count[int(dt)] = 1
```

Now find average:
```python
avg_hour_passenger = {x: float(hour_passenger[x])/hour_count[x] for x in hour_count}
```

We can display results in bar chart:
```python
plt.bar(list(avg_hour_passenger.keys()), avg_hour_passenger.values(), color='blue')
plt.title('Average number of passenger on a given hour per taxi')
plt.xlabel('Hour')
plt.ylabel('Count')
plt.show()
```

Output:

>![Average number of passenger by hours](/Images/Avg_hour_Passengers.png)

Result:
> __From the chat we can see that in this data set hour 6th is most likely to have less passenger in a taxi than at hour 00 or 23rd. We can also see that people mostly commute through taxi between 21th and 03rd hour of the day/night and least between 5th and 9th__




### 9. New CSV file which has one out of every thousand rows for the Taxi trip DataSet

___Logic:___ This is fairly simple to do. We can iterate a loop and put condition that if the row count is divisible by 1000 then write that line into new file. Given this condition writing 1st row of the data is necessary at its the header of the file.

First open the file in write mode and rewrite it with nothing. Basically clearing the data of the file, if it has any:

```python
f2 = open('Sources/Reduce_Taxi_Data.csv', 'w')
f2.write("")
f2.close()
```

Now again opening the file in append mode and creating a writer object:
```python
f2 = open('Sources/Reduce_Taxi_Data.csv', 'a')
writer = csv.writer(f2, delimiter=',', lineterminator='\n')
```

Logical code:

```python
if i % 1000 == 0:
        writer.writerow(row)
```

### 10. Comparing data set - with step 8 and 9

___Logic:___ Since we created a new file containing every 1000th row from our dataset we can repeat step 8 on our reduced dataset.

Outputs:

__1. Total number of passengers:__

Original | Reduced
----------|------------
![Hourly Passengers](/Images/Hour_Passenger.png)| ![Reduced Hourly Passengers](/Images/Rd_Hour_Passenger.png)

Result:
>

__2. Average number of passengers each hour of the day:__

Original | Reduced
---------|---------
![Average number of passenger by hour each day](/Images/Avg_Hour_Day_Passengers.png) | ![ Reduced Average number of passenger by hour each day](/Images/Rd_Avg_Hour_Day_Passengers.png)

Result:
>

__3. Average number of passenger by hour on a given day in a taxi__

Original|Reduced
---------|---------
![Average number of passenger by hours](/Images/Avg_hour_Passengers.png)|![Reduced Average number of passenger by hours](/Images/Rd_Avg_hour_Passengers.png)

Result:
>
