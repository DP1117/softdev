'''
Will Nzeuton, Daniel Park
Blue Stuff
SoftDev
K13: More work with templates
2024-10-02
time-spent: 1 HR
'''

from flask import Flask, render_template
import csv, random

app = Flask(__name__)

# generates a random job
@app.route("/wdywtbwygp")
def gen_rand_job():
    template_list = []
    # opening csvfile
    with open('data/occupations.csv', newline='') as csvfile:
        # list of rows in csvfile
        rows = list(csv.reader(csvfile))
    # column names defined in first row (Job class and Percentage)
    columns = rows[0]
    # dictionary with Job Class and Percentage as key and a list of their corresponding values as the value
    job_dict = {columns[0] : [], columns[1]: [], columns[2]: []}
    # disregard first and last row
    for row in rows[1:len(rows) - 1]:
        job_dict[columns[0]].append(row[0])
        job_dict[columns[1]].append(float(row[1]))
        job_dict[columns[2]].append(row[2])
    # generates a random float between 0 and the total percentage
    rand = random.uniform(0, float(rows[len(rows) - 1][1]))
    rand_job = ""
    for i in range(1, len(rows) - 1):
        # decrease random float by the percentage until it is less than 0
        rand -= float(rows[i][1])
        if rand <= 0:
            rand_job = job_dict[columns[0]][i - 1]
            break
    print(job_dict.values())
    reformatted = []
    for i in range(len(list(job_dict.values())[0])):
        reformatted.append([list(job_dict.values())[0][i], list(job_dict.values())[1][i], list(job_dict.values())[2][i]])
    return render_template('tablified.html', occupations = reformatted, job = rand_job.lower(), title = "How to get a job???")
    
app.debug = True
app.run()