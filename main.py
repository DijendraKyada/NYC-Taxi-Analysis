import csv
import time

# initializing start time
start = time.time()

# opening file in read form
fn = 'Sources/trip_data_7.csv'
f = open(fn, "r")
reader = csv.reader(f)

# printing header of the file
n = 0
for row in reader:
    if n == 0:
        print(row)
    break

# printing time
print(time.time()-start)
