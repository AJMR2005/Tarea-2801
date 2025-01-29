#Arnold Merchan Rojas 
#punto 1 Programa que verifica los elementos dentro de una lista y me fice si hay elementos repetidos
print('el programa verifica los elementos dentro de una lista y me fice si hay elementos repetidos')
#pide el numero de elementos dentro de la lista
Nelementos=int(input('ingrese el numero de elementos'))
elemtrep=0
elemento=0
x=0
#se crea lista vacia
lista=[]
#se crea un for en el que me va agreagar un elemento a la lista hasta q hayan N elementos
for i in range(Nelementos):
    Elemento=input(f'ingrese el elmento {i+1}: ')
    lista.append(Elemento)

for i in lista:
    #cuenta cuantas veces se repite cierto elemento
    contador=lista.count(i)
    if contador>1:
        print(f'el elemento {i} se encuentra {contador} veces')
    if contador<1:
        print('no hay elementos repetidos')

print('_______________________________________________________________\n\n\n\n\n')  
    

       


#punto 2el programa determina si las palabras en la lista son palndromes
print('el programa programa determina si las palabras en la lista son palndromes')
#crear una lista vacia
list_elemt= []
#se ingresa numero de elementos de la lista
Elemetos=int(input('ingrese el numero de elementos'))
#variable global a usar mas adelante
h=0
##se crea un for en el que me va agreagar un elemento a la lista hasta q hayan N elementos
for i in range(Elemetos):
    palabra=str(input(f'ingrese la palabra {i+1}'))
    list_elemt.append(palabra)


#se analiza cada palabra al reves
for i in list_elemt:
    reves=i[::-1]
    #si la palabra al reves es igual que al derecho me va a imprimir  que la palabra es palindrome y va a sumar 1 a la variabñe h
    if reves==i:
        print(f'la palabra {i} es palindrome')
        h=h+1
        #si h es = a 0 significa que no hay palabras palindromes en la lista
if h==0:
    print('no hay palabras palindromes')


print('_______________________________________________________________\n\n\n\n\n')  



#punto 3 el programa determina si dentro de una lista de palagras hay una palabra con 2 o mas vocales
print('el programa determina si dentro de una lista de palagras hay una palabra con 2 o mas vocales')
g=0
palab=[]
Npalan=int(input('ingrese el numero de palabras que desea incluir en la lista'))
for i in range(Npalan):
    word=input(f'ingrese la palabra #{i+1}')
    palab.append(word)  

for i in palab:
#se cuentan las vocales de cada elemento de la lista
    x= i.count('a')
    y= i.count('e')
    z= i.count('i')
    b= i.count('o')
    c= i.count('u')
    totvoc=x+y+z+b+c
    #si el total de vocales es mayor a 2  me va a decir que esa palabra va a tener mas de dos vocales y va a sumar 1 a la variable global
    if totvoc>2:
        print(f'la parablra {i} tiene mas de dos vocales') 
        g=g+1  
        #si g sigue siendo 0 significa que no hay palabras con mas de 2 vocales

if g==0:
    print('no existe')






print('_______________________________________________________________\n\n\n\n\n')  

    
#punto 4 el programa determina si una lista es palindrome
print('el programa determina si una lista es palindrome')
list_palin=[]
s=0
q=0
p=('')
Nelement=int(input('ingrese el numero de palabras que desea incluir en la lista'))
for i in range(Nelement):
    word=input(f'ingrese la palabra #{i+1}')
    list_palin.append(word) 


for i in list_palin:
#declaro la variable q = a i
    q=i
    #comparo mi variable global con p con el elemento
    if p!= i:
        #como es diferente me une la palabra p con la cuardada en q
        p= p+q
#con esta variable rectifico que ya todos los elementos de de la lista esten dentro de la cadena de caracteres
        fin=p.find(list_palin[Nelement-1])
#si no encuentra el elemento buscado dentro de la cadena de caracteres find me bota -1  por lo que asi rectifico que todos los elementos esten en la cadena de caracteres

        if fin!=-1:
            #pongo al contrario la cadena de caracteres
            contrario=p[::-1]
            #comparo la cadena al reves y al derecho si es igual es palindrome
            if contrario==p:
                print('la lista es palindrome')
                s=s+1
if s==0:
    print(' la lista no es pa lindrome')


print('_______________________________________________________________\n\n\n\n\n')  

print('el programa encuentra el numero maximo dentro de una lista')
#punto 5 el programa encuentra el numero maximo dentro de una lista

def crear_lista():
    lista_auto=[]
    numelemen=int(input('ingrese el numero de elementos de su lista'))
    for i in range(numelemen):
        objeto=input(f'ingrese e elemento #{i+1}   :')
        lista_auto.append(objeto)
    return lista_auto
ab={'j'}    
lista5=crear_lista()
long=len(lista5)
#variable global a se declar comom entero he igual a 0
a=int(0)
#se corre toda la lista
for i in lista5:
    #cada elemento de la lista lo llamamos con la variable numero y lo convertimos a entero
    numero=int(i)
    #la variable a siempre va a guardar el numero mayo desde que sean positivos
    if a<numero:       
        a=numero
        #print(f'el numero mayor es ={a}')
        print(a)
        ultimo=int(lista5[long-1])
       
        if ultimo==numero:
            print(f'el numero mayor es ={a}')
    #en dado caso que encuentre un numero a mayor que el elemento me verifica si dicho elemenrto s el ultimo y si es el mayor
    elif a>numero:
        ultimo=int(lista5[long-1])
        a=a
        if ultimo==numero:
            print(f'el numero mayor es ={a}')



        


        

      