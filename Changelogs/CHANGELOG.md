# CHANGELOG

<!-- neve-work:changelog-9b208495-ad74-4942-9b58-ace4db9b427b:begin -->
## Alterações · Work 9b208495-ad7

- `classes.py` — Alterado; +45/−2 linhas. Símbolos novos/alterados: `game`.
- `room_manager.py` — Criado; +109/−0 linhas. Símbolos novos/alterados: `RoomManager`.

### Resumos dos patches (informativos)
- `room_manager.py`: A intenção é implementar um gerenciador de salas que permite ao criador visualizar participantes e removê-los, preservando a modularidade do sistema. O efeito é a adição de novas funcionalidades de controle de acesso sem
- `classes.py`: A alteração adiciona a propriedade `room_users` para rastrear os participantes e implementa o método `create_room` para inicializar essa lista com o criador da sala. Isso permite que o usuário visualize a lista de membro

Validação de execução registrada separadamente pelo Work.
<!-- neve-work:changelog-9b208495-ad74-4942-9b58-ace4db9b427b:end -->


<!-- neve-work:changelog-b7d50278-1460-4209-9671-cd3378863406:begin -->
## 2026-11-25 · Alterações · Work b7d50278-146

- `Dockerfile` — Criado; +27/−0 linhas.
- `docker-compose.yml` — Criado; +19/−0 linhas.

### Resumos dos patches (informativos)
- `Dockerfile`: A alteração cria um ambiente de execução isolado e portátil para o jogo, permitindo que ele rode em qualquer máquina sem dependências locais. O efeito é a capacidade de subir o projeto rapidamente em VMs, mantendo a exec
- `docker-compose.yml`: A alteração cria um ambiente de containerização para rodar o jogo Hangman em qualquer máquina virtual com acesso ao código-fonte. O efeito é permitir a execução interativa do aplicativo através de um terminal persistente

Validação de execução registrada separadamente pelo Work.
<!-- neve-work:changelog-b7d50278-1460-4209-9671-cd3378863406:end -->

<!-- neve-work:changelog-23a24798-47e9-469d-bf39-d71de1fb8007:begin -->
## 2026-11-25 · Alterações · Work 23a24798-47e

- `Main.py` — Alterado; +62/−20 linhas.
- `auth.py` — Criado; +97/−0 linhas. Símbolos novos/alterados: `get_db_path`, `get_users_file_path`, `load_users`, `save_users`, `hash_password`, `register_user`, `authenticate_user`, `validate_session`.
- `classes.py` — Alterado; +11/−1 linhas. Símbolos novos/alterados: `join_room`.
- `config.py` — Criado; +113/−0 linhas. Símbolos novos/alterados: `get_db_path`, `get_users_file_path`, `load_users`, `save_users`, `hash_password`, `register_user`, `authenticate_user`, `validate_session`.
- `database.py` — Criado; +64/−0 linhas. Símbolos novos/alterados: `get_db_path`, `get_users_file_path`, `load_users`, `save_users`, `hash_password`, `register_user`, `authenticate_user`, `validate_session`.
- `palavras.txt` — Alterado; +2/−0 linhas.
- `room_manager.py` — Alterado; +25/−4 linhas. Símbolos novos/alterados: `RoomManager`.

### Resumos dos patches (informativos)
- `config.py`: A alteração introduz um módulo de configuração para gerenciar autenticação, sessões e permissões de usuários via arquivos locais. Ela habilita funcionalidades de registro e login com distinção de níveis de acesso sem dup
- `database.py`: A intenção é implementar um sistema de autenticação com níveis de permissão usando um arquivo JSON local para persistência de usuários. O efeito é adicionar funções para registro, validação de senha e geração de tokens, 
- `auth.py`: A intenção é implementar um sistema de autenticação com níveis de permissão ADMIN e MEMBER, enquanto o efeito é introduzir dependências de arquivos JSON e funções de hash que não estão presentes no código original.
- `classes.py`: A alteração adiciona parâmetros de sessão de usuário ao método `join_room` para validar autenticação e permissões antes de permitir o acesso. Isso impede que usuários não identificados ou com papéis inválidos entrem em s
- `room_manager.py`: A alteração adiciona campos de usuário e permissão ao registro da sala para suportar a nova funcionalidade de login. O efeito imediato é permitir que o sistema diferencie administradores de membros, embora a lógica de fi
- `Main.py`: A alteração introduz um sistema de autenticação que verifica o estado do usuário antes de iniciar o chat, garantindo que apenas usuários logados acessem a funcionalidade. O efeito imediato é que o fluxo do chat agora dep
- `palavras.txt`: A alteração adiciona dois novos tipos de usuário ao sistema para habilitar a funcionalidade de login com níveis de permissão distintos. Isso permite que o código identifique e trate corretamente os administradores e memb

Validação de execução registrada separadamente pelo Work.
<!-- neve-work:changelog-23a24798-47e9-469d-bf39-d71de1fb8007:end -->
