import csv
import math
f= open('DataSet.csv')
lns=csv.reader(f) 

dataset=list(lns)

print ("Porfavor ingrese los datos solicitados \n\n")
print("Edad: ",end="")
edad=int(input())
print("Cuatrimestre que cursa: ",end="")
cuatrimestre=int(input())
print("Promedio hasta el momento: ",end="")
promedio=int(input())
print("Materias reprobadas: ",end="")
reprobadas=int(input())
print("Numero de vecinos a considerar: ",end="")
k=int(input())
distancias=[0,0]
beca=[0,0]
contador=0

for i in dataset:
    dataset[contador][0]=int(dataset[contador][0])
    dataset[contador][1]=int(dataset[contador][1])
    dataset[contador][2]=int(dataset[contador][2])
    dataset[contador][3]=int(dataset[contador][3])
    dataset[contador][4]=int(dataset[contador][4])
    if (contador<2):
        interna=((dataset[contador][2]-promedio)**2)+((dataset[contador][3]-reprobadas)**2)
        raiz=math.sqrt(interna)
        distancias[contador]=raiz
        beca[contador]=dataset[contador][4]
    else:
        interna=((dataset[contador][2]-promedio)**2)+((dataset[contador][3]-reprobadas)**2)
        raiz=math.sqrt(interna)
        distancias.append(raiz)
        beca.append(dataset[contador][4])
    contador+=1

i=0

distancias
while (i<contador):
    j=i
    while( j < contador):
        if (distancias[i]>distancias[j]):
            temp=distancias[i]
            distancias[i]=distancias[j]
            distancias[j]=temp
            tempo=beca[i]
            beca[i]=beca[j]
            beca[j]=tempo
        j=j+1
    i=i+1



cont1=0
cont2=0

for x in range(0,k):
    if(beca[x]==1):
        cont1=cont1+1
    else:
        cont2=cont2+1
    print(beca[x])

if(cont1==cont2):
    if(beca[0]==1):
        print("El alumno tiene una beca")
    else:
        print("El alumno no tiene una beca")

if(cont1>cont2):
    print("El alumno tiene una beca")
if(cont2>cont1):
    print("El alumno no tiene beca")
