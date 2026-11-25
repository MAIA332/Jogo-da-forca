# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import os




def rand_word() -> str:
    with open("palavras.txt", "r", encoding="utf-8") as f:
        bank = f.readlines()
    if not bank:
        raise ValueError("A lista de palavras está vazia.")
    return random.choice(bank).strip()

def create_room() -> str:
    import secrets
    room_code = "".join(secrets.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(6))
    return room_code

def join_room(room_code: str) -> bool:
    # Implementação básica para validação futura
    if len(room_code) != 6:
        return False
    return True

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


    def verify_word(self, letter):
        # Camada 1: Validação de entrada básica
        if not isinstance(letter, str) or len(letter) != 1:
            self.board_count += 1
            print("\n" + '\033[31m' + " Entrada de letra inválida amiguinho" + '\033[0;0m')
            input()
            return

        # Camada 2: Validação de caracteres permitidos (segurança contra injeção de caracteres especiais)
        if not letter.isalpha():
            self.board_count += 1
            print("\n" + '\033[31m' + " Apenas letras são permitidas amiguinho" + '\033[0;0m')
            input()
            return

        self.rep_letter.append(letter)
        
        if letter in self.palavra:
            p = 0
            while p < len(self.palavra):
                if self.palavra[p] == letter:
                    self.v_l_word[p] = letter
                    p += 1
                else:
                    p += 1
            
            self.n_l_word = "".join(self.v_l_word)
        else:
            self.board_count += 1
            print("\n" + '\033[31m' + " Não tem essa letra amiguinho" + '\033[0;0m')
            input()

    def create_room(self):
        """Cria uma nova sala com um código único."""
        import random
        self.room_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
        print(f"\nSala criada! Código: {self.room_code}")
        print("Compartilhe este código com seus amigos para que eles entrem.")
        return self.room_code

    def join_room(self, room_code):
        """Verifica se o jogador pode entrar na sala especificada."""
        if room_code == self.room_code:
            print("\nBem-vindo à sala! Você pode começar a jogar.")
            return True
        else:
            print("\nCódigo de sala inválido. Tente novamente.")
            return False

    def share_room_code(self):
        """Exibe o código da sala atual para compartilhamento."""
        if hasattr(self, 'room_code') and self.room_code:
            print(f"\nSeu código de sala é: {self.room_code}")
        else:
            print("\nVocê ainda não criou uma sala.")


    def prin_board(self):
        os.system("cls")

        print(self.board[self.board_count])
        print("\n"+" "+self.n_l_word)
        print("\n"+" Letras Que ja foram: "+str(self.rep_letter))

