#Métodos úteis 

nome = "AmaNDa"

print(nome.upper())
#O comando upper, deixará o nome inteiro em maiúsculo. 
print(nome.lower())
#Deixa o nome inteiro em minúsculo.
print(nome.title())
#Transforma o nome em um titulo.

texto = "   Olá mundo!    "

print(texto.strip() + ".")
#Tira os espaços dados tanto na direita quanto na esquerda.
print(texto.rstrip() + ".")
#Mantém o espaço da esquerda.
print(texto.lstrip() + ".")
#Mantém o espaço da direita.

menu = "Python"

print(menu.center(14))
#Centraliza o "texto" conforme o espaço que colocamos, neste caso 
#o espaço é 14.
print("-".join(menu))
#Coloca o - entre cada letra de Python.
