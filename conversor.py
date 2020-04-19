import os
import platform
from time import sleep

#Essa classe tem 2 métodos o de converter texto em binário e de converter textos binários em texto 
class Conversor:
    # Esse método irá conerter texto em texto binário
    def codifica(self, texto):
        texto_bin = ""
        for letra in texto:
            letra_bin = bin(ord(letra))[2:]
            if len(letra_bin) < 8:
                texto_bin += "0"*(8-len(letra_bin)) + letra_bin + " "
        return texto_bin
    

    # Esse mátodo ira fazer a conversão do texto binário em texto
    def decodifica(self, texto_bin):
        try:
            texto = ""
            texto_bin = texto_bin.split()
            for letra_bin in texto_bin:
                texto += chr(int(letra_bin, 2))
            return texto
        except ValueError:
            print("[ ! ] O TEXTO INFORMADO NÃO ESTÁ EM BINÁRIO")
            return 1


# Essa função é responsável por pegar o valor que o usuário digitar e verificar se é um valor inteiro e se caso for irá retorna-lo
def validaint(frase):
    while True:
        entrada = str(input(frase))
        if entrada.isnumeric():
            return int(entrada)
        print(f"[ ! ] Por favor informe um valor válido!")


# Responsável por mostrar as opções disponíveis para o usuário e garantir que ele digite uma opção que está disponível
def inicio(lista_opc, minimo, maximo):
    for cont in range(0, len(lista_opc)):
        print(f"[ {cont+1} ] {lista_opc[cont]}")
    print("[ 0 ] SAIR")
    print()
    while True:
        opc = validaint("Escolha uma opção: ")
        if opc > maximo or opc < minimo:
            print(f"[ ! ] Informe uma opção entre {minimo} e {maximo}.")
            continue
        print()
        return opc


def pegatexto(frase):
    while True:
        texto = str(input(frase))
        if len(texto) == 0:
            print("[ ! ] Digite algo")
            continue
        break
    return texto


# É responsável por identidicar o sistema operacional e limpar a tela
def limpatela():
    sistema = platform.system().lower()
    if sistema == "windows":
        os.system("cls")
    else:
        os.system("clear")


# Irá mostrar na tela em uma forma mais animada o texto passado como parametro
def titulo_animado(texto, tam=60, sinal="=", tempo=0.005):
    texto = f"{texto:^{tam}}"
    decoracao = sinal*tam
    def animacao(caracteres):
        for carac in caracteres:
            print(carac, end="", flush=True)
            sleep(tempo)
        print()
    animacao(decoracao)
    animacao(texto)
    animacao(decoracao)
    print()


# função principal do programa
def main():
    try:
        c = Conversor()
        cont = 0
        while True:
            limpatela()
            if cont == 0:
                titulo_animado("Introdução - Esse programa serve para codificar e decodificar código binário", 80, "*", 0.005)
            if cont % 5 == 0:
                titulo_animado("Created by: Bernardino Silva", 60, '=', 0.006)
            opcoes = ["Codificar", "Decodificar"]
            opc = inicio(opcoes, 0, 2)
            if opc > 0:
                titulo_animado(opcoes[opc-1].upper(), 60, '-', 0.002)
            if opc == 1:
                texto = pegatexto("Texto para CODIFICAR: ")
                codificado = c.codifica(texto)
                print(f"\n[ CODIFICADO ] \n\n{codificado}\n")
            elif opc == 2:
                binario = pegatexto("Binário para DECODIFICAR: ")
                decodificado = c.decodifica(binario)
                print()
                if decodificado == 1:
                    print("[ ERRO ]  NÃO FOI POSSÍVEL DECODIFICAR\n")
                else:
                    print(f"\n[ DECODIFICADO ] \n\n{decodificado}\n")
            else:
                input("Pressione ENTER para sair...")
                exit()
            input("Pressione ENTER para continuar")
            cont += 1
    except KeyboardInterrupt:
        print("\n\nAté a próxima... E bons estudos!")
        input("Pressione ENTER para sair...")

main()