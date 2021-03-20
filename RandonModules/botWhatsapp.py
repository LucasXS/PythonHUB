import pywhatkit

lista_numeros = ['+5511960649838']
mensagem = "Olá, essa é uma mensagem enviada pelo pywhatkit"

for numero in lista_numeros:    # para cada nýmero que existir em uma lista de números
    pywhatkit.sendwhatmsg(numero, mensagem, 23,22) # biblioteca chama a função e enviar x msg.

# Precisei mudar dentro do mainfunctions uma das execessões linha 292
# if tyme >= 60:
#         raise Warning("INTERNET IS SLOW, extraction of information might take longer time")
# Onde está >= 60 estava 5 e isso estava ocorrendo o erro indicado no exceção
