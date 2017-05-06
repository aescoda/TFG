tupla = ("Alex", "neus", 12)
lista = ["Carlos", "javier", 15]
lista3 = [tupla, lista]
lista[0]= lista[0][0:2];

#print(lista3   );

def func(a,b):
    i=0
    z=0;
    while i<3:
        z=z+a+b;
        print(z)
        i = i+1

func(6,5)
