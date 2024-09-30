'''
Daniel Park
Blue Stuff
SoftDev
K13: Running flask app on template
2024-09-24
time-spent: 0.5 HR
'''

from flask import Flask, render_template
import csv, random

app = Flask(__name__)

# generates a random job
@app.route("/wdywtbwygp")
def gen_rand_job():
    # opening csvfile
    with open('data/occupations.csv', newline='') as csvfile:
        # list of rows in csvfile
        rows = list(csv.reader(csvfile))
    # column names defined in first row (Job class and Percentage)
    columns = rows[0]
    # dictionary with Job Class and Percentage as key and a list of their corresponding values as the value
    job_dict = {columns[0] : [], columns[1]: []}
    # disregard first and last row
    for row in rows[1:len(rows) - 1]:
        job_dict[columns[0]].append(row[0])
        job_dict[columns[1]].append(float(row[1]))
    # generates a random float between 0 and the total percentage
    rand = random.uniform(0, float(rows[len(rows) - 1][1]))
    rand_job = ""
    for i in range(1, len(rows) - 1):
        # decrease random float by the percentage until it is less than 0
        rand -= float(rows[i][1])
        if rand <= 0:
            rand_job = f"Random {columns[0]}: {job_dict[columns[0]][i - 1]}\n{columns[1]}: {job_dict[columns[1]][i -  1]}"
    return render_template('tablified.html', occupations = job_dict)
            
app.debug = True
app.run()
