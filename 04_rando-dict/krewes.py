'''
Daniel Park
Topher Lovers
SoftDev
K04: Random Student Generation from Dictionary
2024-09-13
time-spent: 0.2 HR
'''
import random

# A dictionary with SoftDev period as the key and list of students in that period as the corresponding value
krewes = {
    4: [ 
        'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
        'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
        'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
        'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
        ],
    5: [ 
        'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
        'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
        'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
        'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
        ]
    }

# generates a random student from any period in the krewes dictionary
def gen_rand_student():
    # generates a random period
    rand_period = list(krewes.keys())[random.randint(0, len(krewes) - 1)]
    # generates a random dev from the generated random period
    rand_devo = krewes[rand_period][random.randint(0, len(krewes[rand_period]) - 1)]
    return rand_devo

# tests the gen_rand_student() function
def test():
    for i in range(10):
        print(gen_rand_student())

test()