#!/usr/bin/python3
# -*-  coding: utf-8 -*-
import csv

def handle_hours(course):
    weeks = int(course[2])
    begin_time = int(course[3])
    hours = int(course[4])
    for x in range(weeks):
        key = begin_time-1+x 
        weeks_hours[key] += hours

def print_hours(weeks_hours):
    for key,value in weeks_hours.items():
        print("Week {} has {}'s study hours".format(key+1,value))

#        print(x,begin_time,hours,weeks)
#        weeks_hours[begin_time-1+x] += hours


weeks_hours = {}
for x in range(20):
    weeks_hours[x] = 0
with open("schoolCourse.csv", "r") as f:
    reader = csv.reader(f)
    for line in reader:
        handle_hours(line)
#    print(weeks_hours)    
    print_hours(weeks_hours)


