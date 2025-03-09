#Args e Kwargs

def exibir_poema(data_extenso, *args, **kwargs):
    #Tanto args e kwargs podem ter um nome diferente, como: **dicionario.
    texto = "\n".join(args)
    #⬆️Pega todos os valores que estiverem em args e concatenando com \n
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sábado, 08 de Março de 2025", "Zen of Python", "Beautiful is better than ugly. ", autor="Tim Peters", ano=1999)
