#Scanner per individuare le porte aperte di un sistema in un range voluto dall'utente
import socket
indirizzo=input("Inserisco IP della macchina che vuoi scannerizzare: ")
porte=input("Inserisci range di porte che vuoi analizzare nel formato a-b: ")
a,b=map(int, porte.split("-"))
for i in range(a,b+1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    risposta=s.connect_ex((indirizzo,i))
    if risposta==0:
        print(f"{i} è aperta")
    s.close()



