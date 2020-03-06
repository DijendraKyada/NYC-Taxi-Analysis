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
number_of_rows = 0
for row in reader:
    if n == 0:
        print(row)
    number_of_rows += 1
    n += 1

# printing time
print("# of rows:", number_of_rows)
print(time.time()-start)
