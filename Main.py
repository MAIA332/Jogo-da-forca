import classes as cl
import os

g = cl.game()
while True:

    g.prin_board()
    letra_test = str(input("\n"+" Chute uma letra: "))

    if(letra_test in g.rep_letter):
        print("Esta letra ja foi")
        os.system("pause")

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