#Argumentos Nomeados

def salvar_carro(marca, modelo, ano, placa):
    #salvando carro no banco de dados..
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


#Formas de passagens e execução de argumentos 
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

#Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234