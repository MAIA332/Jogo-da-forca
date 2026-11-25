import classes as cl
import os
import re
import threading
import queue
import time

g = cl.game()
user_lock = threading.Lock()
active_threads = {}

def handle_client_thread(user_id: str, user_data: dict):
    """
    Gerencia a thread individual para um cliente logado.
    Garante isolamento e consistência de dados por meio de locks e filas de eventos.
    """
    thread_id = f"thread_{user_id}"
    thread_data = {
        'user_id': user_id,
        'user_data': user_data,
        'queue': queue.Queue(),
        'lock': threading.Lock(),
        'active': True
    }
    
    with user_lock:
        active_threads[thread_id] = thread_data
    
    try:
        # Exibe splash screen de 2 segundos com a mensagem de boas-vindas
        user_name = user_data.get('name', 'Usuário')
        splash = SplashScreen(user_name)
        splash.show()
        
        # Simula processamento de eventos do cliente (chat, chutes, etc.)
        # Em uma implementação real, isso consumiria da fila de eventos
        time.sleep(0.1) 
    finally:
        with user_lock:
            if thread_id in active_threads:
                active_threads[thread_id]['active'] = False
                del active_threads[thread_id]

while True:
    g.prin_board()
    opcao = input("\nEscolha uma opção: 1. Criar Sala  2. Entrar em Sala  3. Chute uma letra: 4. Chat Global: ").strip()
    
    if opcao == '1':
        g.create_room()
    elif opcao == '2':
        codigo = input("Digite o código da sala: ").strip()
        g.join_room(codigo)
    elif opcao == '3':
        letra_test = str(input("\n"+" Chute uma letra: "))
        # Validação de segurança: garantir que a entrada seja uma única letra alfabética
        if not re.match(r'^[a-zA-Z]$', letra_test):
            print("Entrada inválida. Por favor, digite apenas uma letra.")
            continue
    elif opcao == '4':
        from chat_manager import ChatManager
        from auth import authenticate_user, get_current_user, get_user_role
        from database import load_users
        import json
        
        # Verifica se o usuário já está logado
        user_info = get_current_user()
        
        if user_info:
            print(f"Bem-vindo de volta, {user_info['username']} ({user_info['role']}).")
            chat_manager = ChatManager()
            print("Conectando ao chat global...")
            
            # Inicializa a thread isolada para este usuário
            user_id = user_info['id']
            thread = threading.Thread(
                target=handle_client_thread,
                args=(user_id, user_info),
                daemon=True
            )
            thread.start()
            print(f"Thread iniciada para {user_id}.")
            chat_manager.connect()
            print("Chat global iniciado. Digite 'sair' para encerrar.")
            while True:
                msg = input("Você: ").strip()
                if msg.lower() == 'sair':
                    chat_manager.disconnect()
                    break
                chat_manager.send(msg)
                # Simulação de recebimento de mensagens para visualização no terminal
                try:
                    if hasattr(chat_manager, 'receive_message'):
                        msg_recebida = chat_manager.receive_message()
                        if msg_recebida:
                            print(f"[{msg_recebida.get('timestamp', 'now')}] {msg_recebida.get('user', 'Unknown')}: {msg_recebida.get('message', '')}")
                except Exception:
                    pass
        else:
            # Fluxo de login
            print("=== Sistema de Login ===")
            username = input("Digite seu usuário: ").strip()
            password = input("Digite sua senha: ").strip()
            
            if not username or not password:
                print("Usuário e senha são obrigatórios.")
                continue
            
            # Autenticação
            user_data = authenticate_user(username, password)
            
            if user_data:
                print(f"Login bem-sucedido! Bem-vindo, {user_data['username']} ({user_data['role']}).")
                chat_manager = ChatManager()
                print("Conectando ao chat global...")
                chat_manager.connect()
                print("Chat global iniciado. Digite 'sair' para encerrar.")
                while True:
                    msg = input("Você: ").strip()
                    if msg.lower() == 'sair':
                        chat_manager.disconnect()
                        break
                    chat_manager.send(msg)
                    try:
                        if hasattr(chat_manager, 'receive_message'):
                            msg_recebida = chat_manager.receive_message()
                            if msg_recebida:
                                print(f"[{msg_recebida.get('timestamp', 'now')}] {msg_recebida.get('user', 'Unknown')}: {msg_recebida.get('message', '')}")
                    except Exception:
                        pass
            else:
                print("Credenciais inválidas. Tente novamente.")
                continue

    else:
        print("Opção inválida.")
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