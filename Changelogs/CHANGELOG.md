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


<!-- neve-work:changelog-6dcbe1ac-6ebd-47f2-91d3-45f9cc6afe93:begin -->
## 2026-11-25 · Alterações · Work 6dcbe1ac-6eb

- `Main.py` — Alterado; +1/−1 linhas.
- `auth.py` — Alterado; +5/−2 linhas. Símbolos novos/alterados: `load_users`, `save_users`.
- `classes.py` — Alterado; +33/−0 linhas. Símbolos novos/alterados: `TestUser`, `temp_dir`, `mock_session_manager`, `create_session`.
- `config.py` — Alterado; +10/−4 linhas. Símbolos novos/alterados: `load_users`, `save_users`.
- `room_manager.py` — Alterado; +20/−9 linhas. Símbolos novos/alterados: `RoomManager`.
- `tests/__init__.py` — Criado; +193/−0 linhas. Símbolos novos/alterados: `TestUser`, `temp_dir`, `mock_session_manager`, `mock_auth_service`, `valid_user`, `admin_user`, `invalid_credentials`, `expired_session_token`.
- `tests/test_auth.py` — Criado; +96/−0 linhas. Símbolos novos/alterados: `TestUser`, `temp_dir`, `mock_session_manager`, `create_session`, `test_login_valid_credentials`, `test_login_invalid_credentials`, `test_register_new_user`, `test_register_duplicate_user`.

### Resumos dos patches (informativos)
- `tests/__init__.py`: A intenção é criar um ambiente de teste isolado para validar a lógica de autenticação e autorização sem afetar dados reais. O efeito é garantir que os defeitos sejam corrigidos automaticamente antes de qualquer execução 
- `tests/test_auth.py`: A proposta visa automatizar testes de autenticação e autorização isolados para garantir a integridade do sistema sem alterar dados reais. O efeito esperado é a detecção e correção automática de falhas nos contratos de lo
- `classes.py`: A alteração introduz uma classe de teste e utilitários para simular usuários e sessões sem tocar no código de produção. Isso permite criar testes automatizados para validar credenciais e permissões de forma isolada.
- `room_manager.py`: A alteração visa restringir a criação de salas a usuários com permissão ADMIN e adicionar parâmetros de contexto para filtrar usuários na sala. Isso garante que apenas administradores possam criar salas e que a visualiza
- `auth.py`: A alteração adiciona validação de tipo para garantir que o arquivo JSON carregado seja um dicionário, prevenindo erros de execução com dados corrompidos ou formatos inválidos. Ao elevar exceções de falhas de escrita em v
- `Main.py`: A alteração visa corrigir um erro de digitação na mensagem de sucesso do login. O efeito é tornar a saída do sistema mais profissional e legível.
- `config.py`: A alteração visa garantir a resiliência do sistema contra arquivos de configuração corrompidos ou inválidos, prevenindo falhas de leitura e salvamento. Isso assegura que o módulo de autenticação continue operando com dad

Validação de execução registrada separadamente pelo Work.
<!-- neve-work:changelog-6dcbe1ac-6ebd-47f2-91d3-45f9cc6afe93:end -->


<!-- neve-work:changelog-63c25336-bf81-412f-99ae-8b0eb0bfedc6:begin -->
## 2026-11-25 · Alterações · Work 63c25336-bf8

- `Dockerfile` — Alterado; +1/−1 linhas.
- `Main.py` — Alterado; +44/−0 linhas. Símbolos novos/alterados: `handle_client_thread`.
- `classes.py` — Alterado; +91/−2 linhas. Símbolos novos/alterados: `TestUser`, `TempDirManager`, `temp_dir`.
- `config.py` — Alterado; +2/−2 linhas. Símbolos novos/alterados: `get_db_path`, `get_users_file_path`.
- `room_manager.py` — Alterado; +111/−0 linhas. Símbolos novos/alterados: `RoomManager`.

### Resumos dos patches (informativos)
- `config.py`: A intenção é atualizar os comentários para refletir a nova arquitetura de isolamento por thread, sem alterar a lógica de criação de diretórios. O efeito é apenas uma melhoria na documentação, mantendo o comportamento atu
- `classes.py`: A alteração implementa um padrão de thread por cliente para garantir isolamento e consistência de dados em operações concorrentes. O efeito é a criação de threads dedicadas por usuário com gerenciamento centralizado de r
- `room_manager.py`: A alteração introduz threads dedicadas por usuário para processar mensagens em paralelo, visando aumentar a eficiência do sistema. Isso garante a integridade dos dados através de bloqueios e filas, mas pode causar incons
- `Main.py`: A alteração propõe criar uma thread dedicada para cada usuário logado, isolando o processamento de eventos e garantindo a consistência dos dados. Isso aumenta a eficiência do sistema ao permitir que múltiplos clientes op
- `Dockerfile`: A alteração remove um espaço em branco desnecessário e substitui o ENTRYPOINT pelo CMD para definir o comando de execução padrão. Isso garante que o container execute o módulo Main corretamente ao ser iniciado.

Validação de execução registrada separadamente pelo Work.
<!-- neve-work:changelog-63c25336-bf81-412f-99ae-8b0eb0bfedc6:end -->


<!-- neve-work:changelog-ae6fa984-06d3-4150-9ce4-3bb9f47d6d43:begin -->
## 2026-11-25 · Alterações · Work ae6fa984-06d

- `Main.py` — Alterado; +8/−4 linhas. Símbolos novos/alterados: `handle_client_thread`.
- `splash.py` — Criado; +18/−0 linhas. Símbolos novos/alterados: `SplashScreen`.

### Resumos dos patches (informativos)
- `splash.py`: A alteração cria uma classe dedicada para exibir uma mensagem de boas-vindas personalizada com um atraso controlado. Isso centraliza a lógica da splash screen, evitando duplicação e facilitando futuras integrações com o 
- `Main.py`: A alteração introduz um módulo SplashScreen para exibir uma mensagem de boas-vindas personalizada durante 2 segundos ao iniciar a sessão. Isso garante que o usuário receba uma mensagem contextualizada antes que o sistema

Validação de execução registrada separadamente pelo Work.
<!-- neve-work:changelog-ae6fa984-06d3-4150-9ce4-3bb9f47d6d43:end -->


<!-- neve-work:changelog-7706767c-062c-4cd1-8855-1bbb3758c4d2:begin -->
## 2026-11-25 · Alterações · Work 7706767c-062

- `assets/splash_ascii.py` — Criado; +20/−0 linhas. Símbolos novos/alterados: `SplashScreen`.
- `splash.py` — Alterado; +6/−0 linhas. Símbolos novos/alterados: `SplashScreen`.

### Resumos dos patches (informativos)
- `assets/splash_ascii.py`: Foram propostas 20 linhas adicionadas e 0 removidas em 1 região(ões). Confira os trechos abaixo e o objetivo da tarefa.
- `splash.py`: Foram propostas 6 linhas adicionadas e 0 removidas em 2 região(ões). Confira os trechos abaixo e o objetivo da tarefa.

Validação de execução registrada separadamente pelo Work.
<!-- neve-work:changelog-7706767c-062c-4cd1-8855-1bbb3758c4d2:end -->

<!-- neve-work:changelog-ec28b599-d9ec-4362-ae2c-018122c5f82b:begin -->
## 2026-11-25 · Alterações · Work ec28b599-d9e

- `classes.py` — Alterado; +122/−36 linhas. Símbolos novos/alterados: `TestUser`, `create_room`, `hash_password`, `verify_password`, `game`.
- `security.py` — Criado; +48/−0 linhas. Símbolos novos/alterados: `PasswordHasher`.

### Resumos dos patches (informativos)
- `security.py`: A intenção é implementar um mecanismo de hashing de senhas com sal para mitigar ataques de força bruta e rainbow tables. O efeito é a adição de uma nova classe de utilidade que centraliza a lógica de criptografia sem alt
- `classes.py`: A intenção é adicionar um método de hash de senha com sal para proteger credenciais, mas o efeito é falhar devido a uma lógica de verificação incorreta que compara hashes em vez de senhas.
- `classes.py`: A alteração remove duplicatas de importação e resolve o ciclo circular ao manter a dependência entre classes.py e si mesmo. Isso garante que o código execute sem erros de importação, preservando a funcionalidade original
- `classes.py`: A alteração resolve a importação circular removendo a referência direta e substituindo-a por uma importação relativa, eliminando o erro de execução. Isso permite que o módulo seja carregado corretamente sem criar classes

Validação de execução registrada separadamente pelo Work.
<!-- neve-work:changelog-ec28b599-d9ec-4362-ae2c-018122c5f82b:end -->


<!-- neve-work:changelog-0f5032dc-c1a2-523e-8f2e-e400ad539b3c:begin -->
## 2026-11-26 · Alterações · Work 0f5032dc-c1a

- `Dockerfile` — Alterado; +11/−1 linhas.
- `room_manager.py` — Alterado; +27/−19 linhas. Símbolos novos/alterados: `RoomManager`.

### Resumos dos patches (informativos)
- `room_manager.py`: A alteração adiciona lógica para mudar o diretório de execução para o caminho padrão do Docker ou Linux, garantindo que o aplicativo rode corretamente em qualquer ambiente. Isso elimina a dependência de configurações loc
- `Dockerfile`: A alteração adiciona o suporte ao sistema de arquivos VFS para permitir que o jogo acesse arquivos de texto em sistemas Windows e macOS além do Linux. Isso garante que a imagem Docker funcione corretamente em qualquer má

Validação de execução registrada separadamente pelo Work.
<!-- neve-work:changelog-0f5032dc-c1a2-523e-8f2e-e400ad539b3c:end -->


<!-- neve-work:changelog-f8f85016-12ae-50f4-adbc-bc9498616a13:begin -->
## 2026-11-27 · Alterações · Work f8f85016-12a

- `Dockerfile` — Alterado; +3/−22 linhas.
- `docker-compose.yml` — Alterado; +4/−0 linhas.

### Resumos dos patches (informativos)
- `Dockerfile`: A alteração simplifica a instalação de dependências e remove comandos desnecessários para garantir que o container rode corretamente em qualquer ambiente. Isso torna o projeto muito mais fácil de implementar ao eliminar 
- `docker-compose.yml`: A alteração adiciona suporte a terminais interativos e entrada padrão, facilitando a execução local do CLI dentro de containers. Isso permite que o usuário teste o aplicativo diretamente no terminal sem precisar configur

Validação de execução registrada separadamente pelo Work.
<!-- neve-work:changelog-f8f85016-12ae-50f4-adbc-bc9498616a13:end -->
