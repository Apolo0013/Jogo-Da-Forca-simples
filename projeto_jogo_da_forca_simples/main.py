# Projeto do jogo da forca simples com modularização e funcoes e os carai a quatros
from Modulos.defs import *


while True:
    opcao = Menu()
    if opcao == 1:
        Jogar()
        LimparTerminal()
    else:
        break
