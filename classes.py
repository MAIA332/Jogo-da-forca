# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import os




def rand_word():
    with open("palavras.txt","r") as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()

class game():
        # Board (tabuleiro)
    board = ['''

    >>>>>>>>>>Hangman<<<<<<<<<<

    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

    palavra = rand_word()
    board_count = 0
    l_word = "_"*len(palavra)
    n_l_word = ""
    rep_letter = []
    
    v_l_word = []

    palavra = palavra.lower()
      
    for l in l_word:
        v_l_word.append(l)


    def verify_word(self,letter):
        self.rep_letter.append(letter)
       
        if letter in self.palavra :
            p = 0
            while p < len(self.palavra):
                if(self.palavra[p] == letter):
                    print(self.palavra[p])
                    self.v_l_word[p] = letter
                    p+=1
                    
                else:
                    p+=1

            self.n_l_word = "".join(self.v_l_word)

        else:
            self.board_count +=1
            print("\n"+'\033[31m'+" Não tem essa letra amiguinho"+'\033[0;0m')
            os.system("pause")

    def prin_board(self):
        os.system("cls")

        print(self.board[self.board_count])
        print("\n"+" "+self.n_l_word)
        print("\n"+" Letras Que ja foram: "+str(self.rep_letter))

