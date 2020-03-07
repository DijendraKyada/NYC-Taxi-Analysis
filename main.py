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
pickup_min_lon = None
pickup_min_lat = None
dropoff_min_lon = None
dropoff_min_lat = None
pickup_max_lon = None
pickup_max_lat = None
dropoff_max_lon = None
dropoff_max_lat = None

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

        # min pickup
        if pickup_min_lon is None and pickup_min_lat is None:
            pickup_min_lon = row[10]
            pickup_min_lat = row[11]
        elif pickup_min_lon > row[10] and pickup_min_lat > row[11]:
            pickup_min_lon = row[10]
            pickup_min_lat = row[11]

        # max pickup
        if pickup_max_lon is None and pickup_max_lat is None:
            pickup_max_lon = row[10]
            pickup_max_lat = row[11]
        elif pickup_max_lon < row[10] and pickup_max_lat < row[11]:
            pickup_max_lon = row[10]
            pickup_max_lat = row[11]

        # min dropoff
        if dropoff_min_lon is None and dropoff_min_lat is None:
            dropoff_min_lon = row[12]
            dropoff_min_lat = row[13]
        elif dropoff_min_lon > row[12] and dropoff_min_lat > row[13]:
            dropoff_min_lon = row[12]
            dropoff_min_lat = row[13]

        # max dropoff
        if dropoff_max_lon is None and dropoff_max_lat is None:
            dropoff_max_lon = row[12]
            dropoff_max_lat = row[13]
        elif dropoff_max_lon < row[12] and dropoff_max_lat < row[13]:
            dropoff_max_lon = row[12]
            dropoff_max_lat = row[13]

    # incrementing pointer
    n += 1
    # if n > 20:break


# subtracting number_of_rows by 1 as first row was header
print("# of rows:", number_of_rows-1)

# min_pickup_time
print("Data ranges from:", min_pickup_time)

# max_dropoff_time
print("Data ranges till:", max_dropoff_time)

# Min Pickup
print("Min Pickup Longitude:", pickup_min_lon)
print("Min Pickup Latitude:", pickup_min_lat)

# Max Pickup
print("Max Pickup Longitude:", pickup_max_lon)
print("Max Pickup Latitude:", pickup_max_lat)

# Min Pickup
print("Min Dropoff Longitude:", dropoff_min_lon)
print("Min Dropoff Latitude:", dropoff_min_lat)

# Max Pickup
print("Max Dropoff Longitude:", dropoff_max_lon)
print("Max Dropoff Latitude:", dropoff_max_lat)

# printing total time taken to run the script
print(time.time()-start)
