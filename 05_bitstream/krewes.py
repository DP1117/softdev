'''
Daniel Park
Topher Lovers
SoftDev
K05: File Parsing
2024-09-17
time-spent: 0.5 HR
'''
import random

# generates a dictionary from a file containing a list of devos, their period, and their ducky name 
def gen_dict(file_name):
    # read file
    file = open(file_name, "r")
    devo_content = file.read()
    file.close()

    # list of devos, their period, and their ducky name
    devos = devo_content.split("@@@")
    krewes = {}

    # generates the dictionary with period number as the key and a list
    # containing lists of devo and ducky names as the value
    for devo in devos:
        devo_info = devo.split("$$$")
        period = devo_info[0]
        if not period in list(krewes.keys()):
            krewes[period] = []
        krewes[period].append(devo_info[1:len(devo_info)])
    return krewes

# generates a random student's info from any period in the krewes dictionary
def gen_rand_student(krewes):
    # generates a random period
    rand_period = list(krewes.keys())[random.randint(0, len(krewes) - 1)]
    # generates a random devo's info from the generated random period
    rand_devo_info = krewes[rand_period][random.randint(0, len(krewes[rand_period]) - 1)]
    return [rand_period, rand_devo_info[0], rand_devo_info[1]]

def test():
    krewes = gen_dict("krewes.txt")
    rand_devo_info = gen_rand_student(krewes)
    print(rand_devo_info)

test()