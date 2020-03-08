import csv
import time
from datetime import datetime
import matplotlib.pyplot as plt


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

        # min and max geo
        if row[10] != '' and row[11] != '' and row[12] != '' and row[13] != '':
            pickup_lon = float(row[10])
            pickup_lat = float(row[11])
            dropoff_lon = float(row[12])
            dropoff_lat = float(row[13])
            '''
            This is the boundary of NYC
            min_lat = 40.5774
            max_lat = 40.9176
            min_long = -74.15
            max_long = -73.7004
            '''

            # min and max pickup
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

    # incrementing pointer
    n += 1
    if n > 20:
        break


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


# printing total time taken to run the script
print(time.time()-start)
