# Funcoes necessarias para o fucionamento do projeto em si, aqui sera localizador as defs e etc

#Importações
from random import randint
from time import sleep
from os import system
from Modulos.banco import *
from rich import print
from rich.progress import track


#Funcoes

# "Menu" do Jogo que consiste em: Jogar, e Cancelar o Programa.
def Menu():
    Lista = ['Jogar','Cancelar O Programador'] # Formação do Menu
    linha()
    for numero , menu in enumerate(Lista):
        sleep(0.9)
        print(f'[bold][yellow]{numero+1} - {menu}[/][/]')
    linha()
    while True:
        try:
            opcao = int(input('\033[1;33mEscolha:\033[m '))
        except (ValueError , TypeError , KeyboardInterrupt):
            print('Algo deu errado')
        else:
            progresso()
            if opcao in (1,2):
                LimparTerminal()
                return opcao
            print('[bold][red]Apenas 1 e 2[/][/]')
            


# "Jogar" consiste em representar o jogo e jogar o mesmo, com as funcoes de verificação de respostas e etc
def Jogar():
    # global termos duas variavel necessario para o fucionamento do programa
    """
    palavras_forca: nao esta muito bem esclarecida mais, ele que vai receber as letras que estao na
    palavras escolhida, vai exbir
    
    """
    global palavras_forca , chance  , banco , palavras
    chance = 5
    banco = banco_de_dados()
    palavra_escolhida = Sortea(banco = banco)
    palavras_forca = [] # lista é essa que irar exbida para o jogador tentar acerta, e cada certo a letras irar parece no lugar dele
    for contador in range(0 , len(palavra_escolhida)):
        palavras_forca.append(['?'])
    sleep(2)
    while True:
        linha()
        print(f'[bold][green]Dica: {banco[palavras][1]}[/][/]')
        sleep(1)
        linha()
        print(f'[bold][yellow]chances restantes: {chance}[/][/]')
        sleep(1)
        while True:
            try:
                letra = str(input('\033[1;33mSeu palpite:\033[m ')).strip().lower()[0]
            except (ValueError , TypeError):
                print('[bold][red]Apenas string irmaozinho[/][/]')
            except KeyboardInterrupt:
                print('[bold][red]Filho de uma puta, sem CTRL + C[/][/]')
            else:
                linha()
                sleep(1)
                print(Verficação(letra = letra , palavras_escolhida = palavra_escolhida))
                sleep(3)
                LimparTerminal()
                linha()
                for pla in palavras_forca:
                    for letra in pla:
                        print(f'{letra}' , end=' ')

                print()
                sleep(3)
                break
        gg = ganhou(palavra = palavras_forca)
        if gg:
            linha()
            print(f'Palavra: {palavra_escolhida}')
            linha()
            print('[bold][green]GG!! Você conseguiu!!![/][/]')
            sleep(6)
            break

        if chance == 0:
            linha()
            print('[bold][red]Infelizmente suas chances acabaram[/][/]')
            linha()
            sleep(3)
            LimparTerminal()
            break


# "Verificação" verficar se tem o a letra/string na palavras sorteada.
def Verficação(letra , palavras_escolhida):
    global chance , palavras_forca
    certou = False
    """
    Com repetição, vamos verificar se a letra que o usuarios digitou esta na palavras escolhida
    aleatoriamente.
    """
    for posicao , string in enumerate(palavras_escolhida):
        if string == letra:
            del palavras_forca[posicao]
            palavras_forca.insert(posicao , letra)
            certou = True
    if certou:
        return f'[bold][green]Boa!!! Sim tem "{letra}"[/]'
    else:
        chance -= 1
        return f'[bold][red]Se-Fudeu kkk,  nao tem "{letra}" na palavra[/]'


# ganhou Verificando se o jogador ganhou
def ganhou(palavra):
    ganhou = 0 # vai verificar se o usuario ganhou ou nao
    for l in palavra:
        for letra in l:
            if letra == '?':
                ganhou +=1
    if ganhou == 0:
        return True


# "Sortea" sortear a palavras e rotorna a mesma.
def Sortea(banco):
    global palavras
    palavras = randint(0, len(banco)-1)
    return banco[palavras][0]


# "Linha" estetica
def linha():
    print('_'* 50)


#Limpar Terminal
def LimparTerminal():
    system('cls')


#Progresso
def progresso():
    for tarefa in track(range(5), '\033[1;32mCarregando\033[m'):
        sleep(2)


if __name__ == '__main__':
    print()