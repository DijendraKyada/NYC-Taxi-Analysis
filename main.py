import csv
import time
from datetime import datetime

# initializing start time
start = time.time()

# opening file in read form
fn = 'Sources/trip_data_7.csv'
f = open(fn, "r")
reader = csv.reader(f)

n = 0
number_of_rows = 0
min_pickup_time = None
max_dropoff_time = None
pickup_lon = {}
pickup_lat = {}
dropoff_lon = {}
dropoff_lat = {}


for row in reader:
    # printing header
    if n == 0:
        print("Header of the file:", row)

    # counting number of rows
    number_of_rows += 1

    # printing first 5 data(rows)
    if n > 0 and n < 6:
        print(row)

    # sample date time from data 2013-07-01 01:47:00
    if n > 0:

        # finding lowest value of pickup datetime
        pickuptime = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
        if min_pickup_time is None:
            min_pickup_time = pickuptime
        elif pickuptime < min_pickup_time:
            min_pickup_time = pickuptime

        # finding highest value of dropoff datetime
        dropofftime = datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S')
        if max_dropoff_time is None:
            max_dropoff_time = dropofftime
        elif dropofftime > max_dropoff_time:
            max_dropoff_time = dropofftime

        # pickup Longitude
        if row[10] in pickup_lon:
            pickup_lon[row[10]] += 1
        else:
            pickup_lon[row[10]] = 1

    # incrementing pointer
    n += 1
    # if n > 20:break


# subtracting number_of_rows by 1 as first row was header
print("# of rows:", number_of_rows-1)

# min_pickup_time
print("Data ranges from:", min_pickup_time)

# max_dropoff_time
print("Data ranges till:", max_dropoff_time)

# Pickup Longitude
print("Pickup Longitude:", pickup_lon)

# printing total time taken to run the script
print(time.time()-start)
