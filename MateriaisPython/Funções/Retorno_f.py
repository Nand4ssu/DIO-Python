#Retorno de Funções 

def calcular_total(numeros):
    return sum(numeros)
#O Sum foi utilizado para somar os números.

def retorno_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

#Ele retornará None por padrão caso não colocarmos um return explicito
#Ex de return explicito: return 42

def func_3():
    print("Olá mundo")

print(calcular_total([10, 20, 34])) #64
print(retorno_antecessor_e_sucessor(10)) #(9, 11)
print(func_3()) #Retorna None.