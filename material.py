import random

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
        if self.num==10:
            numstr="J"
        elif self.num==11:
            numstr="Q"
        elif self.num==12:
            numstr="K"
        else:
            numstr=str(self.num)
        st=f"{numstr}{self.palo[0]}"
        return st
    
    def __eq__(self, other):
        return (self.num==other.num) and (self.palo==other.palo)

class Mazo():
    def __init__(self):
        palos={
            "copa": 0,
            "oro": 1,
            "basto":2, 
            "espada":3
        }
        self.orden=[]
        for palo in palos:
            for i in range(7):
                c=Carta(i+1, palo)
                self.orden.append(c)
            for i in range(10, 13):
                c=Carta(i, palo)
                self.orden.append(c)
    def revolver(self):
        orden_actual=self.orden.copy()
        self.orden=[]
        for _ in range(40):
            c=random.choice(orden_actual)
            orden_actual.remove(c)
            self.orden.append(c)
        return self.orden

    def repartir_mano(self):
        c1=random.choice(self.orden)
        self.orden.remove(c1)
        c2=random.choice(self.orden)
        self.orden.remove(c2)
        c3=random.choice(self.orden)
        self.orden.remove(c3)
        return [c1, c2, c3]

    def __str__(self):
        output=""
        for carta in self.orden:
            output+=carta.__str__()+" "
        return output

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

if __name__=="__main__":
    mazo=Mazo()
    print(mazo)
    mano=mazo.repartir_mano()
    print(*[m for m in mano])
    print(mazo)
    mano=mazo.repartir_mano()
    print(*[m for m in mano])
    print(mazo)
    mano=mazo.repartir_mano()
    print(*[m for m in mano])
    print(mazo)