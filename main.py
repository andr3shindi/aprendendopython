print("Hello world")

def soma (valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("Digite o valor 1 para somar: "))
    valor2 = int(input("Digite o valor 2 para somar: "))
    resposta = soma(valor1, valor2)
    print("A soma é ", resposta)
    print("________")
   



'''
listPlayers = []
qtdPlayers = int(input("quantos players deseja criar? "))
for n in range (qtdPlayers):
    nome = input("Nome do jogador: ")
    hp = int(input("Qtde de HP: "))
    mana = int(input("quantidade  de mana: "))
    player = {
    "nome": nome,
    "hp": hp,
    "mana": mana
    }
    listPlayers.append(player)

for l in listPlayers:
    print(player['nome'])
    print(player['hp'])
    print(player['mana'])

quantos = int(input("Digite quantidade de loop:"))


map = []

for x in range(quantos):
    id = input("insira um ID: ")
    valor = float(input("Insira um valor"))
    linha = [id, valor]
    map.append(linha)

print (map)

for m in map:
    print("ID: ",m[0])
    print("Valor: ",m[1])
    id = m[0]
    valor = m[1]
    print("printa tudo ", id, " teste ", valor)




list = []
list.append("test1")
list.append("test2")

print (list)

#print (nome, type(nome))
print (idade, type(idade))
#print (peso, type(peso))


if idade >=18:
    print("Tu é velho")
else:
    print ("Tu é novo")
    '''