import classes as cl
import os
import re

g = cl.game()
while True:
    g.prin_board()
    letra_test = str(input("\n"+" Chute uma letra: "))
    # Validação de segurança: garantir que a entrada seja uma única letra alfabética
    if not re.match(r'^[a-zA-Z]$', letra_test):
        print("Entrada inválida. Por favor, digite apenas uma letra.")
        continue
    
    if(letra_test in g.rep_letter):
        print("Esta letra já foi")
        os.system("pause")
        break
        break
    g.verify_word(letra_test.lower())

    if(g.board_count == 6):
        os.system("cls")
        print("\n"+" Voce perdeu meu chapa :(")
        print("\n"+f"A palavra era {g.palavra}")
        exit()
    elif(g.palavra == g.n_l_word):
        os.system("cls")
        print("\n"+"Parabens voce ganhou :)")
        print("\n"+f"A palavra era {g.palavra}")
        exit()