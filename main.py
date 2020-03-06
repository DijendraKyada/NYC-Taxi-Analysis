import csv
import time
from datetime import datetime

# initializing start time
start = time.time()

# opening file in read form
fn = 'Sources/trip_data_7.csv'
f = open(fn, "r")
reader = csv.reader(f)

# printing header of the file
n = 0
number_of_rows = 0
min_pickup_time = None
max_dropoff_time = None

for row in reader:
    if n == 0:
        # this is header
        print("Header of the file:", row)
    number_of_rows += 1

    # 2013-07-01 01:47:00
    if n > 0:
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
    n += 1

# subtracting number_of_rows by 1 as first row was header
print("# of rows:", number_of_rows-1)

# min_pickup_time
print("Data ranges from:", min_pickup_time)

# max_dropoff_time
print("Data ranges till:", max_dropoff_time)

print(time.time()-start)
