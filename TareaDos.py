import csv
f= open('DataSet.csv')
lns=csv.reader(f) 
datos=list(lns)

print ("Ingresa Datos \n\n")
Edad=int (input("Edad entre 18 y 28 años : \n"))
if Edad<18 or Edad>28:
    while Edad<18 or Edad>28:
        print ("Error\n\nIngresa Nuevos Datos \n\n")
        Edad=int (input("Edad entre 18 y 28 años : \n"))
        if Edad<18 or Edad>28:
            print("Error en la edad")
        
Cuatrimestre=int (input("Cuatrimestre de primero a noveno: \n"))
if Cuatrimestre<1 or Cuatrimestre>9:
    while Cuatrimestre<1 or Cuatrimestre>9:
        print ("Error\n\nIngresa Nuevos Datos \n\n")
        Cuatrimestre=int (input("Cuatrimestre entre primero y noveno: \n"))
        if Cuatrimestre<1 or Cuatrimestre>9:
            print("Error")


Promedio=int (input("Promedio de 0 a 10 redondeado: \n"))

    
Materias=int (input("Materias Reprobadas de 0 a 4: \n"))
if Materias<0 or Materias>4:
    while Materias<0 or Materias>4:
        print ("Error\n\nIngresa Nuevos Datos \n\n")
        Materias=int (input("Materias Reprobadas entre cero y cuatro: \n"))
        if Materias<0 or Materias>4:
            print("Error")

Si=[0,0,0,0,0]
No=[0,0,0,0,0]
Prediccion=[Edad,Cuatrimestre,Promedio,Materias]
Res=[0,0,0]
Probabilidad=[0,0]
contador=0

for i in datos:
    datos[contador][0]=int(datos[contador][0])
    datos[contador][1]=int(datos[contador][1])
    datos[contador][2]=int(datos[contador][2])
    datos[contador][3]=int(datos[contador][3])
    datos[contador][4]=int(datos[contador][4])
    
    
    if datos[contador][4]==1:
        Si[4]+=1       
    else:
        No[4]+=1
        
    if datos[contador][4]==1 and datos[contador][0]==Prediccion[0]:
        Si[0]+=1
        
    if datos[contador][4]==0 and datos[contador][0]==Prediccion[0]:
        No[0]+=1
        
    if datos[contador][4]==1 and datos[contador][1]==Prediccion[1]:
        Si[1]+=1
        
    if datos[contador][4]==0 and datos[contador][1]==Prediccion[1]:
        No[1]+=1
        
    if datos[contador][4]==1 and datos[contador][2]==Prediccion[2]:
        Si[2]+=1
        
    if datos[contador][4]==0 and datos[contador][2]==Prediccion[2]:
        No[2]+=1

    if datos[contador][4]==1 and datos[contador][3]==Prediccion[3]:
        Si[3]+=1
        
    if datos[contador][4]==0 and datos[contador][3]==Prediccion[3]:
        No[3]+=1
    
    contador+=1   


Res[0]=(Si[0]/Si[4])*(Si[1]/Si[4])*(Si[2]/Si[4])*(Si[3]/Si[4])*(Si[4]/contador)        

Res[1]=(No[0]/No[4])*(No[1]/No[4])*(No[2]/No[4])*(No[3]/No[4])*(No[4]/contador) 

Res[2]=Res[0]+Res[1]

Probabilidad[0]=100*(Res[0]/Res[2])
Probabilidad[1]=100*(Res[1]/Res[2])

print ("Probabilidad de tener beca: "+str(Probabilidad[0])+"%")
print ("Probabilidad de no tener beca: "+str(Probabilidad[1])+"%")