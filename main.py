import csv
import time

start = time.time()

fn = 'Sources/trip_data_7.csv'
f = open(fn, "r")
n = 0
for line in f:
    print(line)
    break
print(time.time()-start)
print("Hello")
