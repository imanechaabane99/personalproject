#Funzione che fa la somma
def fun_somma(a,b):
    somma=a+b;
    return(somma)
print(fun_somma(6,5)) 

#Funzione che inverte la stringa
def inverti_stringa(frase):
    print(frase[::-1])

stringa=("La mamma va a comprare il latte")
inverti_stringa(stringa)

#Funzione che conta le parole che iniziano con una determinata lettera
def conta_let(lista_parole, lettera):
    lista_finale=[]
    for parola in lista_parole:
        if parola[0]==lettera:
            lista_finale.append(parola)
    return(lista_finale)

parole=["ghiaccio","camerino","simpson", "abaco","serpente","stupido"]
let="s"
print(conta_let(parole,let))

#Funzione che conta la lunghezza delle parole e le mette in una lista
def conta_lun(lista_parole):
    lunghezza=[]
    for parola in lista_parole:
        a=len(parola)
        lunghezza.append(a)
    return(lunghezza)
print(conta_lun(parole))
#Funzione che calcola il valore max di una lista di numeri
def valore_max(lista_num):
    a=lista_num[0]
    for i in range(1,len(lista_num)):
        if(lista_num[i]>a):
            a=lista_num[i]
    return(a)
lista_num=[45,8,52,93,17,14,5,10,73]
print(valore_max(lista_num))