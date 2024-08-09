

import os

mensagens = []

nome = input("Digite seu nome: ")

while True:

    os.system('cls')

    if len(mensagens)>0:
        for m in mensagens:
            print (m['nome'], "-", m['texto'])

    print("__________________")

    texto = input("Digite a mensagem: ")
    if texto == "fim":
        print ("chat encerrado")
        break

    mensagens.append({
        "nome": nome,
        "texto": texto
    })
    