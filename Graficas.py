"""
-Clase: Graficas.py
-Descripción: Clase en la cual se crean las funciones que dibujan las graficas
    que el bot manda a los usuarios periodicamente. Ademas de estas funciones
    tambien existe una función auxiliar para el coloreado de las gráficas
"""

#Libreria para funciones matematicas de alto nivel
import numpy as np

#Libreria para el diseño de gráficas
import matplotlib.pyplot as plt


#Función que va recibiendo la velocidad del viento para cada valor de la gráfica
#y en función de este le otorga un color determinado
def colors(t):
    if(t>=0 and t<0.555556):
        return 'royalblue'
    if(t>0.555556 and t<=1.66667):
        return 'turquoise'
    if(t>1.66667 and t<=3.33333):
        return 'mediumspringgreen'
    if(t>3.33333 and t<=5.55556):
        return 'limegreen'
    if(t>5.55556 and t<=8.1):
        return 'lightsalmon'
    if(t>8.1 and t<=10.8333):
        return 'salmon'
    if(t>10.8333 and t<=13.8889):
        return 'orange'
    if(t>13.8889 and t<=17.2222):
        return 'orangered'
    if(t>17.2222 and t<=20.8333):
        return 'firebrick'
    if(t>20.8333 and t<=24.7222):
        return 'red'
    else:
        return 'darkred'
    

def colors2(t):
    if(t<=0):
        return 'royalblue'
    if(t>0 and t<=0.10):
        return 'turquoise'
    if(t>0.10 and t<=0.5):
        return 'mediumspringgreen'
    if(t>0.5 and t<=1.25):
        return 'limegreen'
    if(t>1.25 and t<=2.5):
        return 'lightsalmon'
    if(t>2.5 and t<=4):
        return 'salmon'
    if(t>4 and t<=6):
        return 'orange'
    if(t>6 and t<=9):
        return 'orangered'
    if(t>9 and t<=14):
        return 'firebrick'
    else:
        return 'red'

#Función que crea una gráfica con los datos de dirección de viento y lo guarda en una imagen.
#Ah esta función se le pasan tres argumentos:
#   -grados: vector con la direccion del viento para las horas establecidas
#   -aux: variable auxiliar que indica si la grafica es para el dia actual o para 
#   -tem: vector con la temperatura del aire para las horas establecidas
def grafica1(grados,aux,tem,data):
    print(grados)
    print(tem)
    if(len(grados)==13):
        x= np.linspace(0,24,13)
        ejex=["00:00","02:00","04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00","00:00"]
   
    else:
        x = np.linspace(1, 23, 12)
        ejex=["00:00","02:00","04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00"]
   


    fig = plt.figure()
    fig.set_size_inches(8,2)
    ax = fig.gca()
    #print(x)
    #print(np.zeros(x.shape))

    print(tem)
    t=[]

    characters=" ºC"
    i=0
    for z in tem:
      t.append(''.join(y for y in z if y not in characters))
      t[i]=float(t[i])
      i=i+1
      

    a=[]
    i=0
    print("--------------------------------------------")


    while(i<len(grados)):
        b=-np.tan(grados[i])*x[i]
        a.append(1-b)
        i=i+1;

    print(len(x))
    #print(a)
    plt.xticks(x,ejex)
    plt.xlabel("horas",size=8)
    plt.title("Dirección del viento")
    #ax.get_yaxis().set_visible(True)
    i=0

    d=[]
    for r in data:
        n=r[2].split(" m/s")
        d.append(float(n[0]))

    print(".----------------------------------------.....")
    while i< len(x):
        print(x[i])
        print(a[i])
        ax.quiver(x[i],22,a[i],-100 ,color= colors(t[i]) )
        i=i+1

    y=[0,5,10,15,20,25,30,35,40,45]
    ejey=["0ºC","5ºC","10ºC","15ºC","20ºC","25ºC","30ºC","35ºC","40ºC","45ºC"]
    t=[]
    for row in tem:
        r=row.split(" ºC")
        t.append(float(r[0]))


    plt.plot(x,t,marker=".",color="black",linestyle='solid')
    print(t)
    plt.yticks(y,ejey)
    plt.ylabel("Temperatura(ºC)",size=8)

    if(aux==0):
        plt.savefig("WindDirection.png",bbox_inches="tight")
    
    else:
        plt.savefig("WindDirection2.png",bbox_inches="tight")



#Función que crea una gráfica con los datos de dirección de oleaje y lo guarda en una imagen.
#Ah esta función se le pasan tres argumentos:
#   -grados: vector con la direccion de oleaje para las horas establecidas
#   -aux: variable auxiliar que indica si la grafica es para el dia actual o para 
#   -tem: vector con la temperatura del agua para las horas establecidas
def grafica2(grados,aux,tem,data):
    print(tem)
    if(len(grados)==13):
        x= np.linspace(0,24,13)
        ejex=["00:00","02:00","04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00","00:00"]
   
    else:
        x = np.linspace(1, 23, 12)
        ejex=["00:00","02:00","04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00"]
   

    fig = plt.figure()
    fig.set_size_inches(8,2)
    ax = fig.gca()
    #print(np.zeros(x.shape))

    t=[]
    characters=" ºC"
    i=0
    for z in tem:
      t.append(''.join(y for y in z if y not in characters))
      t[i]=float(t[i])
      i=i+1


    a=[]
    i=0
    #print("--------------------------------------------")
    #print(grados)
    #print(x)
    while(i<len(grados)):
        b=-np.tan(grados[i])*x[i]
        a.append(1-b)
        i=i+1;
   
    plt.xticks(x,ejex)
    plt.xlabel("horas",size=8)
    plt.title("Dirección de oleaje")
    ax.get_yaxis().set_visible(True)
    i=0
    d=[]
    for r in data:
        n=r[2].split(" m")
        d.append(float(n[0]))

    while i< len(x):
        ax.quiver(x[i],22,a[i],-100,color=colors2(t[i]) )
        i=i+1

    y=[0,5,10,15,20,25,30,35,40,45]
    ejey=["0ºC","5ºC","10ºC","15ºC","20ºC","25ºC","30ºC","35ºC","40ºC","45ºC"]
    t=[]
    for row in tem:
        r=row.split(" ºC")
        t.append(float(r[0]))


    plt.plot(x,t,marker=".",color="black",linestyle='solid')
    print(t)
    plt.yticks(y,ejey)
    plt.ylabel("Temperatura(ºC)",size=8)


    if(aux==0):
        plt.savefig("SwellDirection.png",bbox_inches="tight")
    else:
         plt.savefig("SwellDirection2.png",bbox_inches="tight")


def guia(x):
    
    if(x==0):
        i=0
        l=["<0.555556 m/s",
        "0.56 m/s > y <=1.67","1.67 m/s > y <=3.34 m/s",
        "3.34 m/s > y <=5.56 m/s","5.56 m/s > y <=8.1 m/s",
        "8.1 m/s > y <=10.84 m/s","10.84 m/s > y <=13.89 m/s",
        "13.89 m/s > y <=17.23 m/s","17.23 m/s > y <=20.84 m/s",
        "20.84 m/s > y <=24.73 m/s",">24.73 m/s"]

        plt.figure(figsize=(2.5,3))
        plt.axhline(y=2, xmin=0.1, xmax=0.3, color="royalblue")
        plt.axhline(y=3, xmin=0.1, xmax=0.3, color="turquoise")
        plt.axhline(y=4, xmin=0.1, xmax=0.3, color="mediumspringgreen")
        plt.axhline(y=5, xmin=0.1, xmax=0.3, color="limegreen")
        plt.axhline(y=6, xmin=0.1, xmax=0.3, color="lightsalmon")
        plt.axhline(y=7, xmin=0.1, xmax=0.3, color="salmon")
        plt.axhline(y=8, xmin=0.1, xmax=0.3, color="orange")
        plt.axhline(y=9, xmin=0.1, xmax=0.3, color="orangered")
        plt.axhline(y=10, xmin=0.1, xmax=0.3, color="firebrick")
        plt.axhline(y=11, xmin=0.1, xmax=0.3, color="red")
        plt.axhline(y=12, xmin=0.1, xmax=0.3, color="darkred")

        n=2
        i=0
        while i<len(l):
            plt.text(0.6,n,l[i], ha="center", size="x-small")
            n=n+1
            i=i+1

        plt.axis('off')
        #plt.show()
        plt.savefig("guia.png",bbox_inches="tight")
    else:
        i=0
        l=["<0 m",
        "0 m > y <=0.10","0.10 m > y <=0.5 m",
        "0.5 m > y <=1.25 m","1.25 m > y <=2.5 m",
        "2.5 m > y <=4 m","4 m > y <=6 m",
        "6 m > y <=9 m","9 m > y <=14 m",
        ">14 m"]

        plt.figure(figsize=(2.5,3))
        plt.axhline(y=2, xmin=0.1, xmax=0.3, color="royalblue")
        plt.axhline(y=3, xmin=0.1, xmax=0.3, color="turquoise")
        plt.axhline(y=4, xmin=0.1, xmax=0.3, color="mediumspringgreen")
        plt.axhline(y=5, xmin=0.1, xmax=0.3, color="limegreen")
        plt.axhline(y=6, xmin=0.1, xmax=0.3, color="lightsalmon")
        plt.axhline(y=7, xmin=0.1, xmax=0.3, color="salmon")
        plt.axhline(y=8, xmin=0.1, xmax=0.3, color="orange")
        plt.axhline(y=9, xmin=0.1, xmax=0.3, color="orangered")
        plt.axhline(y=10, xmin=0.1, xmax=0.3, color="firebrick")
        plt.axhline(y=11, xmin=0.1, xmax=0.3, color="red")

        n=2
        i=0
        while i<len(l):
            plt.text(0.6,n,l[i], ha="center", size="x-small")
            n=n+1
            i=i+1

        plt.axis('off')
        #plt.show()
        plt.savefig("guia2.png",bbox_inches="tight")


