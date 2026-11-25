# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import os




def rand_word() -> str:
    """
    Retorna uma palavra aleatória do arquivo de palavras.
    Design: Mantém a funcionalidade original, mas com docstring alinhada ao estilo técnico do terminal.
    """
    try:
        with open("palavras.txt", "r", encoding="utf-8") as f:
            bank = f.readlines()
        
        if not bank:
            raise ValueError("A lista de palavras está vazia.")
        
        return random.choice(bank).strip()
    except FileNotFoundError:
        raise ValueError("Arquivo 'palavras.txt' não encontrado.")
    except Exception as e:
        raise ValueError(f"Erro ao ler palavras: {e}")

def init_chat_global():
    """Inicializa o módulo de chat global, importando dependências necessárias."""
    from chat_manager import ChatManager
    from templates.chat import render_template
    from templates.menu import render_menu_interactive
    return ChatManager, render_template, render_menu_interactive

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

    def create_room(self, user_id: str) -> str:
        """Cria uma nova sala com um código único e inicia a lista de participantes."""
        import random
        self.room_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
        print(f"\nSala criada! Código: {self.room_code}")
        print("Compartilhe este código com seus amigos para que eles entrem.")
        # Inicializa a lista de participantes com o ID do usuário que criou a sala
        self.room_users = {user_id}
        return self.room_code
        # Nova funcionalidade de chat global será implementada em arquivos separados (gerenciador.py, main.py)
        # Utilizando WebSockets para comunicação em tempo real entre todos os usuários conectados.
        # A lógica de broadcast e gerenciamento de conexões será encapsulada na classe GerenciadorConexoes.
        # A interface HTML será criada em templates/chat.html para interação do usuário.
        # Este método permanece como ponto de entrada para a criação de salas, mas a comunicação global
        # será tratada através das novas rotas de WebSocket definidas no main.py.

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
            print("Opções disponíveis:")
            print("1. Ver participantes da sala")
            print("2. Remover um participante da sala")
            choice = input("\nEscolha uma opção (1 ou 2): ")
            if choice == '1':
                if hasattr(self, 'room_users') and self.room_users:
                    print("\nParticipantes da sala:")
                    for i, user_id in enumerate(self.room_users, 1):
                        print(f"{i}. {user_id}")
                else:
                    print("\nNenhum participante na sala.")
            elif choice == '2':
                if hasattr(self, 'room_users') and self.room_users:
                    print("\nLista de participantes:")
                    for i, user_id in enumerate(self.room_users, 1):
                        print(f"{i}. {user_id}")
                    try:
                        remover_idx = int(input("\nDigite o número do participante a remover: "))
                        if 1 <= remover_idx <= len(self.room_users):
                            user_id_remover = self.room_users[remover_idx - 1]
                            if self.remove_user_from_room(self.room_code, user_id_remover):
                                print(f"\nUsuário {user_id_remover} foi removido da sala.")
                            else:
                                print("\nFalha ao remover o usuário.")
                        else:
                            print("\nNúmero inválido.")
                    except ValueError:
                        print("\nEntrada inválida.")
                else:
                    print("\nNenhum participante na sala.")
        else:
            print("\nVocê ainda não criou uma sala.")

    def remove_user_from_room(self, room_code: str, user_id: str) -> bool:
        """Remove um usuário da sala se for o criador."""
        if not hasattr(self, 'room_users') or not self.room_users:
            return False
        if user_id not in self.room_users:
            return False
        if self.room_users.index(user_id) != 0:  # Apenas o primeiro (criador) pode remover
            return False
        self.room_users.remove(user_id)
        return True


    def prin_board(self):
        os.system("cls")

        print(self.board[self.board_count])
        print("\n"+" "+self.n_l_word)
        print("\n"+" Letras Que ja foram: "+str(self.rep_letter))

