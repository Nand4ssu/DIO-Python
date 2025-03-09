def exibir_mensagem():
    print("Olá mundo!")
#O def informa ao interpretador que o "exibir_mensagem" é uma função

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome ="Anônimo"):
    print(f"Seja bem vindo {nome}!")


#Executando as funções:
exibir_mensagem()
exibir_mensagem_2(nome="Amanda")
#É obrigátorio 'passar' o nome, senão dará erro.
exibir_mensagem_3()
#A mensagem 3 podemos definir o nome ou não. Caso não seja definido, irá chamar "Anônimo"
exibir_mensagem_3(nome= "Chappie")
