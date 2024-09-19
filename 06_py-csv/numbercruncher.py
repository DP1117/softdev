'''
Daniel Park
Blue Stuff
SoftDev
K06: Parsing CSV File
2024-09-18
time-spent: 0.5 HR
'''

import csv, random

with open('occupations.csv', newline='') as csvfile:
    rows = list(csv.reader(csvfile))
    columns = rows[0]
    final_row = rows[len(rows) - 1]
    rand = random.uniform(0, float(final_row[1]))
    for row in rows[1:len(rows) - 1]:
        rand -= float(row[1])
        if rand <= 0:
            print(columns[0] + ": " + row[0])
            print(columns[1] + ": " + row[1])
            break

def algo_test():
    test_list = [60,10,30]
    for i in range(10):
        appearances = [0, 0, 0]
        for i in range(10000):
            rand_num = random.randint(0, 100)
            loc = 0
            for num in test_list:
                rand_num -= num
                if rand_num <= 0:
                    appearances[loc] += 1
                    break
                loc += 1
        print(appearances)
