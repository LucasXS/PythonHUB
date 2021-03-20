import pywhatkit

lista_numeros = ['+55119SEUNUMERO', '+55119SEUNUMERO2']
mensagem = "Olá, Gostaria de ganhar um premio agora?"

for numero in lista_numeros:    # para cada nýmero que existir em uma lista de números
    pywhatkit.sendwhatmsg(numero, mensagem, 0,3)    # biblioteca chama a função e enviar x msg.

# Precisei mudar dentro do mainfunctions uma das execessões linha 292
# if tyme >= 60:
#         raise Warning("INTERNET IS SLOW, extraction of information might take longer time")
# Onde está >= 60 estava 5 e isso estava ocorrendo o erro indicado no exceção
