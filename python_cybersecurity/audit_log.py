#Analizza gli accessi al server e restituisce gli ip associati a quelli falliti 
def analizza_accessi(lista_log, stato_da_filtrare):
    lista_sospetti=[]
    for log in lista_log:
        if log["stato"]==FAILED:
            lista_sospetti.append(log["ip"])
    return(lista_sospetti)

log_server=[

    {"ip":"192.168.1.30","stato":"SUCESS"},
    {"ip":"192.168.40.12","stato":"FAILED"},
    {"ip":"192.168.61.101","stato":"SUCESS"},
    {"ip":"192.168.2.122","stato":"FAILED"},
]
ip_hacker=analizza_accessi(log_server,"FAILED")
print(f"rivelati tentativi di attacco da {ip_hacker} ")
