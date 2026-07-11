#Script che fa un audit delle password di vari utenti e restituisce gli utenti con la password minore di 8

def analisi_password(lista_password):
    lista_nomi=[]
    for credenziali in lista_password:
        if(len(credenziali["password"])<8):
            lista_nomi.append(credenziali["utente"])
    return(lista_nomi)        

lista_credenziali=[
    {"utente":"Marco Rossi","password":"j6saj"},
    {"utente":"Elisa Facchinetti","password":"Nb58sb458g"},
    {"utente":"Roberto Giudice","password":"hx6ge9gdhw"},
    {"utente":"Stefano Torinelli","password":"8h7508"},
    {"utente":"Alessandra Rizzoli","password":"shsuyhihs"},
    {"utente":"Melissa Tardelli ","password":"nsy56t"}

]
nomi=analisi_password(lista_credenziali)
print("Gli utenti che hanno le credenziali troppo deboli sono:")
print(nomi)

        