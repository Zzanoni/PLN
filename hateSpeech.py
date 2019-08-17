import re
from unicodedata import normalize

def verificarTexto(texto):
    palavras = tratarTexto(texto)
    with open ('blacklist.txt', 'r') as lista:
        for linha in lista:
            i = 0
            #Quebra linha por linha da Blacklist
            linha = linha.strip('\n')
            while i<len(palavras):
                if palavras[i] == linha:
                    #Palavra ofensiva identificada
                    return 1
                i+=1
    #Nenhuma palavra ofensiva identificada
    return 0

def tratarTexto(texto):
    #Remove os caracteres especiais
    textoSemPont = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]',
        '', removerAcentos(texto.lower()))
    #Quebra o texto em palavras
    palavras = textoSemPont.split(" ")
    return palavras

def removerAcentos(texto):
    #Remover os acentos das palavras
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

def notificar(texto, score):
    if score == 1:
        print("O texto '", texto, "' foi classificado como OFENSIVO.")
    else:
        print("O texto '", texto, "' foi classificado como NÃO OFENSIVO.")

if __name__ == "__main__":
    while True:
        texto = input()
        resultado = verificarTexto(texto)
        notificar(texto, resultado)
