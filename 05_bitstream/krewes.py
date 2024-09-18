'''
Daniel Park
Topher Lovers
SoftDev
K05: File Parsing
2024-09-17
time-spent: 0.5 HR
'''
import random

# generates a list of dictionaries from a file containing a list of devos, their period, and their ducky name 
def gen_dict(file_name):
    # read file
    file = open(file_name, "r")
    devo_content = file.read()
    file.close()

    # list of devos, their period, and their ducky name
    devos = devo_content.split("@@@")
    krewes = []

    # generates the list of dictionaries
    for devo in devos:
        devo_info = devo.split("$$$")
        krewes.append({'period': devo_info[0], 'devo': devo_info[1], 'ducky': devo_info[2]})
    return krewes


# generates a random devo
def gen_rand_devo(krewes):
    return krewes[random.randint(0, len(krewes) - 1)]

def test():
    krewes = gen_dict("krewes.txt")
    rand_devo_info = gen_rand_devo(krewes)
    print(rand_devo_info)

test()