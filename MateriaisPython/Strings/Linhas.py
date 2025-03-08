#Múltiplas linhas

nome = "Amanda"

mensagem = f'''
    Olá meu nome é {nome}.
      Eu estou aprendendo Python.
    Essa mensaem tem diferentes recuos
'''

#O f''' mantém o texto da maneira que digitamos.
#Não importa se for aspas duplas ou apenas uma.

print(mensagem)

print( 
    f'''
    =========== Menu ===========

    1 - Depositar 
    2 - Sacar 
    3 - Sair

    ==============================

    Obrigado por usar nosso sistema!!
'''
)