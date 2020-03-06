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

## 1.a. Range of data cover

___Logic:___ Taxi trip has initial pickup time and then final dropoff time. Since this dataset has pickup time and dropoff time so we can say that this dataset ranges from minimum value of pickup time(the pickup time of the first ever trip in this dataset) till maximum value of dropoff time(dropoff time of the last trip ever made in this dataset).

## 1.b. Number of Rows in this data set

___Logic:___ Since I am running a single loop for most of the stuff I could just have a counter variable to count the number of rows in that loop.

__`This Dataset has 13,823,841 rows`__

## 2. Field names and Description

___Logic:___ We can show the field names by showing the data of the 1st row (0th Index)

![Fields Names in the DataSet](/Images/Field_Names.png)
Format: ![Fields Names in the DataSet]
