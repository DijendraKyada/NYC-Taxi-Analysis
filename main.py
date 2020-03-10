import csv
import time
import operator
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
medallion = {}
licence = {}
vendor = {}
ratecode = {}
tripdistance_min = None
tripdistance_max = None
tripsec_min = None
tripsec_max = None
hour_passenger = {}


nyc = plt.imread("Images/NYC.png")

# opening the new file and overwriting it with nothing
f2 = open('Sources/Reduce_Taxi_Data.csv', 'w')
f2.write("")
f2.close()
f2 = open('Sources/Reduce_Taxi_Data.csv', 'a')
writer = csv.writer(f2, delimiter=',', lineterminator='\n')

n = 0
for i, row in enumerate(reader):
    # printing header
    if i == 0:
        print("Header of the file:", row)
        writer.writerow(row)

    # counting number of rows
    number_of_rows += 1

    # printing first 5 data(rows)
    if i > 0 and i < 6:
        print(row)

    # sample date time from data 2013-07-01 01:47:00
    if i > 0:

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

        # Medallion Count
        if row[0] in medallion:
            medallion[row[0]] += 1
        else:
            medallion[row[0]] = 1

        # Licence Count
        if row[1] in licence:
            licence[row[1]] += 1
        else:
            licence[row[1]] = 1

        # Vendor count
        if row[2] in vendor:
            vendor[row[2]] += 1
        else:
            vendor[row[2]] = 1

        # Rate count
        if row[3] in ratecode:
            ratecode[row[3]] += 1
        else:
            ratecode[row[3]] = 1

        # min and max trip in sec
        if row[8] != '':
            tripsec = float(row[8])
            if tripsec_min is None and tripsec != 0.0:
                tripsec_min = tripsec
            elif tripsec_min > tripsec and tripsec != 0.0:
                tripsec_min = tripsec
            if tripsec_max is None and tripsec != 0.0:
                tripsec_max = tripsec
            elif tripsec_max < tripsec and tripsec != 0.0:
                tripsec_max = tripsec

        # min and max trip distance
        if row[9] != '':
            tripdistance = float(row[9])
            if tripdistance_min is None and tripdistance != 0.0:
                tripdistance_min = tripdistance
            elif tripdistance_min > tripdistance and tripdistance != 0.0:
                tripdistance_min = tripdistance
            if tripdistance_max is None and tripdistance != 0.0:
                tripdistance_max = tripdistance
            elif tripdistance_max < tripdistance and tripdistance != 0.0:
                tripdistance_max = tripdistance

        # hourly passengers
        dt = row[5].split(' ')[1]
        dt = dt.split(':')[0]
        if row[7] != '' and int(row[7]) != 0:
            if dt in hour_passenger:
                hour_passenger[dt] += int(row[7])
            else:
                hour_passenger[dt] = int(row[7])

        if i % 1000 == 0:
            writer.writerow(row)


# Closing reduced data file
f2.close()

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


bound = (-74.15, -73.7004, 40.5774, 40.9176)
# fig = plt.figure(figsize=(8, 7))
# ax = fig.add_subplot(1, 1, 1)
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
plt.close()

# Distinct values and its counts
print("Medallion: ", sorted(medallion.items(), key=operator.itemgetter(1), reverse=True)[:10])
print('Hack Licence: ', sorted(licence.items(), key=operator.itemgetter(1), reverse=True)[:10])
print('Vendor ID: ', sorted(vendor.items(), key=operator.itemgetter(1), reverse=True)[:10])
print('Rate Code: ', sorted(ratecode.items(), key=operator.itemgetter(1), reverse=True)[:10])

# Min and Max Trip in sec and Trip Distance
print("Min Trip in sec:", tripsec_min)
print("MaxTrip in sec:", tripsec_max)
print("Min Trip Distance:", tripdistance_min)
print("Max Trip Ditance:", tripdistance_max)

# Hourly Passenger Count
print(hour_passenger)
plt.bar(list(hour_passenger.keys()), hour_passenger.values(), color='blue')
plt.show()


# printing total time taken to run the script
print(time.time()-start)
