'''
Daniel Park
Topher Lovers
SoftDev
K05: File Parsing
2024-09-17
time-spent: 0.2 HR
'''

file = open("krewes.txt", "r")
devo_content = file.read()
file.close()

devos = devo_content.split("@@@")
krewes = {}


for devo in devos:
    devo_info = devo.split("$$$")
    if list(krewes.keys())krewes[devo_info[0]]
    krewes[devo_info[0]] = krewes.append(devo_info[1:len(devo_info)])

print(krewes)