import random
import numpy as np
import matplotlib.pyplot as plt
import statistics

palos={
    "copa": 0,
    "oro": 1,
    "basto":2, 
    "espada":3
    }

class Carta():
    def __init__(self, num, palo):
        self.num=num
        self.palo=palo
        if(self.num>=10):
            self.env=0
        else:
            self.env=self.num
        if(self.num>3):
            self.rank=self.num
        if(self.num<=3):
            self.rank=self.num+20
        if(self.num==7 and self.palo=="oro"):
            self.rank=31
        if(self.num==7 and self.palo=="espada"):
            self.rank=32
        if(self.num==1 and self.palo=="basto"):
            self.rank=33
        if(self.num==1 and self.palo=="espada"):
            self.rank=34
    def get_num(self):
        return self.num
    def get_palo(self):
        return self.palo
    def get_env(self):
        return self.env
    def get_rank(self):
        return self.rank
    
    def __str__(self):
        st=f"{self.num}{self.palo[0]}"
        return st
    
    def __eq__(self, other):
        return (self.num==other.num) and (self.palo==other.palo)


def generar_mazo():
    palos={
        "copa": 0,
        "oro": 1,
        "basto":2, 
        "espada":3
    }
    mazo=[]
    for palo in palos:
        for i in range(7):
            c=Carta(i+1, palo)
            mazo.append(c)
        for i in range(10, 13):
            c=Carta(i, palo)
            mazo.append(c)
    return mazo

def generar_mano(mazo):
    c1=random.choice(mazo)
    mazo.remove(c1)
    c2=random.choice(mazo)
    mazo.remove(c2)
    c3=random.choice(mazo)
    mazo.remove(c3)
    return [c1, c2, c3], mazo

def generar_manos(mazo):
    manos=[]
    for c1 in range(len(mazo)-2):
        for c2 in range(c1+1, len(mazo)-1):
            for c3 in range(c2+1, len(mazo)):
                mano=[mazo[c1], mazo[c2], mazo[c3]]
                manos.append(mano)
                #print(mano[0], mano[1], mano[2])
    return manos

def evaluar_envido(mano: list[Carta]):
    c1=mano[0]
    c2=mano[1]
    c3=mano[2]
    if(c1.get_palo()==c2.get_palo()):
        if(c3.get_palo()==c1.get_palo()):
            envido=20+max(
                c1.get_env()+c2.get_env(),
                c1.get_env()+c3.get_env(),
                c2.get_env()+c3.get_env()
                )
        else:
            envido=20+c1.get_env()+c2.get_env()
    elif(c1.get_palo()==c3.get_palo()):
        envido=20+c1.get_env()+c3.get_env()
    elif(c2.get_palo()==c3.get_palo()):
        envido=20+c2.get_env()+c3.get_env()
    else:
        envido=max(c1.get_env(), c2.get_env(), c3.get_env())
    return envido

def ganar_envido(estamano, mazo):
    mazo.remove(estamano[0])
    mazo.remove(estamano[1])
    mazo.remove(estamano[2])
    print(estamano[0], estamano[1], estamano[2])
    manos=generar_manos(mazo)
    esteenv=evaluar_envido(estamano)
    gana=0
    empata=0
    pierde=0
    for m in manos:
        if(evaluar_envido(m)<esteenv):
            gana+=1
        elif(evaluar_envido(m)==esteenv):
            empata+=1
        elif(evaluar_envido(m)>esteenv):
            pierde+=1
    total=gana+empata+pierde
    return gana/total, empata/total, pierde/total

mazo_completo=generar_mazo()
manos=generar_manos(mazo_completo)
mano=[Carta(3, "oro"), Carta(7, "basto"), Carta(1, "oro")]
print(ganar_envido(mano, mazo_completo))



'''
for c1 in range(len(mazo_completo)-2):
    for c2 in range(c1+1, len(mazo_completo)-1):
        for c3 in range(c2+1, len(mazo_completo)):
            resultado=ganar_envido([mazo_completo[c1], mazo_completo[c2], mazo_completo[c3]], mazo_completo.copy())
            print(resultado)

'''


'''
todos_envidos=[]
for _ in range(100000):
    mano, mazo=generar_mano(mazo_completo.copy())
    envido=evaluar_envido(mano)
    todos_envidos.append(envido)
    print(mano[0], mano[1], mano[2], f" con envido: {envido}")
print(statistics.median(todos_envidos))
n, bins, patches = plt.hist(todos_envidos, 34, density=True, facecolor='g', alpha=0.75)
plt.xlim(-1, 34)
plt.show()
'''