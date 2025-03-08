#Interpolação de Variáveis.

nome = "Amanda"
idade = 18
profissao = "Estudante de Ti"
linguagem = "Python"
saldo = 43.000

#Old Style %
print("Nome: %s, idade: %d" % (nome, idade))

#Modelo Format
#pode ser utilizado de várias formas, seja numerado ou nomeado.
print("Nome: {}, idade: {}".format(nome, idade))
print("Nome: {0}, Idade: {1}".format(nome, idade))
print("Nome: {name}, Idade: {age}".format(name=nome, age=idade))

#Criação de um dicionário.
dados = {"nome": "Amanda", "idade": 18, "saldo": 40000}
print("Nome: {nome} idade: {idade}".format(**dados))

#F
#O mais utilizado atualmente, se assemelha muito com o format
print(f"Nome: {nome} idade: {idade} Saldo: {saldo: 10.2f}")
 #o 10 no saldo significa o tamanho do espaço que dado antes do saldo (é opcional), o 2 é quantas casas
 #queremos mostrar.
print(f"Nome: {nome}, Idade: {idade} Saldo: {saldo:.2f}")
