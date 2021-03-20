"""Precisei mudar dentro do mainfunctions uma das execessões na linha 292
if tyme >= 60:
         raise Warning("INTERNET IS SLOW, extraction of information might take longer time")
Onde está >= 60 estava 5 e isso estava ocorrendo o erro indicado na exceção"""

import pywhatkit

lista_numeros = ['+5511997484170']
mensagem = "Salveeee cachorro"

for numero in lista_numeros:    # para cada nýmero que existir em uma lista de números
    # substituia o 11 pela hora atual e o 25 pelo próximo minuto do seu relogio
    pywhatkit.sendwhatmsg(numero, mensagem, 11,25)    # biblioteca chama a função e enviar x msg.

