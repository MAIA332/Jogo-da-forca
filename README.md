# Jogo da Forca em Python
<!-- neve-readme-current -->

**Atualizado em 2026-11-25.**

- `Dockerfile` — Criado; +27/−0 linhas.
- `docker-compose.yml` — Criado; +19/−0 linhas.
- `Main.py` — Alterado; +62/−20 linhas.
- `auth.py` — Criado; +97/−0 linhas. Símbolos novos/alterados: `get_db_path`, `get_users_file_path`, `load_users`, `save_users`, `hash_password`, `register_user`, `authenticate_user`, `validate_session`.
- `classes.py` — Alterado; +11/−1 linhas. Símbolos novos/alterados: `join_room`.
- `config.py` — Criado; +113/−0 linhas. Símbolos novos/alterados: `get_db_path`, `get_users_file_path`, `load_users`, `save_users`, `hash_password`, `register_user`, `authenticate_user`, `validate_session`.
- `database.py` — Criado; +64/−0 linhas. Símbolos novos/alterados: `get_db_path`, `get_users_file_path`, `load_users`, `save_users`, `hash_password`, `register_user`, `authenticate_user`, `validate_session`.
- `palavras.txt` — Alterado; +2/−0 linhas.
- `room_manager.py` — Alterado; +25/−4 linhas. Símbolos novos/alterados: `RoomManager`.

<!-- neve-readme-current -->

Bem-vindo ao repositório do Jogo da Forca em Python! Este projeto é uma implementação do clássico jogo da forca, uma oportunidade para aprimorar suas habilidades de programação e entretenimento. O jogo utiliza um arquivo externo `palavras.txt` para armazenar as palavras a serem adivinhadas.

## Objetivo

O objetivo principal deste repositório é fornecer um exemplo prático de como criar um jogo de adivinhação da forca em Python. O projeto utiliza conceitos básicos da linguagem para criar uma experiência de jogo divertida e interativa.

## Recursos e Destaques

- Funcionalidade completa do jogo da forca: Adivinhe a palavra oculta letra por letra até completar ou enforcar o personagem.
- Arquivo Externo: O arquivo `palavras.txt` contém uma lista de palavras a serem adivinhadas no jogo.
- Interatividade: O jogador pode interagir com o jogo através do terminal.
- Mensagens Descritivas: O jogo fornece mensagens claras para orientar o jogador durante o jogo.
- Simplicidade e Clareza: O código é projetado para ser fácil de entender, adequado para aprendizado.
- Design Moderno: Interface inspirada em ferramentas de monitoramento como Cloudecode e Glances, com tema escuro e elementos interativos.
- Autenticação e Controle de Acesso: Módulo `security.py` implementa criptografia de senhas com MD5 e sal único por usuário, além de validação de sessões e permissões administrativas.
- Testes Automatizados: Suporte a testes unitários com fixtures isoladas (`tmp_path`, `monkeypatch`) para validação de credenciais e sessões.
- Gerenciamento de Salas: Classe `RoomManager` gerencia a criação e gestão de salas de chat.
- Configuração Dinâmica: Carregamento e salvamento de usuários via `load_users` e `save_users` no `config.py`.
- Multi-threading Avançado: Padrão de isolamento por cliente logado, com thread dedicada para cada sessão, garantindo eficiência e consistência de dados.
- Splash Screen de Boas-vindas: Ao autenticar, o sistema exibe uma tela de carregamento personalizada com um mascote em ASCII (estilo "claude code") e a mensagem "Olá {nome do usuário}".

**Atualização:** 2026-11-25

Adicionei a linha de atualização conforme solicitado, mantendo o resto do conteúdo inalterado.
## Como Jogar

1. Clone ou faça o download do repositório para sua máquina local.
2. Execute o arquivo `main.py` utilizando um ambiente Python.
3. Siga as instruções no terminal para jogar. Adivinhe as letras da palavra oculta.
4. Ganhe ao adivinhar a palavra ou enforque o personagem ao errar muitas vezes.
5. Utilize o arquivo `palavras.txt` para adicionar ou modificar palavras do jogo.

## Interface

A interface do jogo foi projetada para ser moderna e interativa, utilizando um tema escuro com elementos em tons de verde e laranja, inspirado em ferramentas de monitoramento de sistemas. O menu é navegável por teclado e inclui uma aba de chat estilizada para comunicação entre jogadores.

![image](https://user-images.githubusercontent.com/67965680/211147230-d26e0796-af42-4200-98f9-5afcdb74c995.png)

---

<p align="center">

  Feito com ❤️ por Lukas Maia
</p>


<!-- neve-work:readme:begin -->
## Alterações desta atualização

- `classes.py` — Alterado; +45/−2 linhas. Símbolos novos/alterados: `game`.
- `room_manager.py` — Criado; +109/−0 linhas. Símbolos novos/alterados: `RoomManager`.

### Resumos dos patches (informativos)
- `room_manager.py`: A intenção é implementar um gerenciador de salas que permite ao criador visualizar participantes e removê-los, preservando a modularidade do sistema. O efeito é a adição de novas funcionalidades de controle de acesso sem
- `classes.py`: A alteração adiciona a propriedade `room_users` para rastrear os participantes e implementa o método `create_room` para inicializar essa lista com o criador da sala. Isso permite que o usuário visualize a lista de membro

Validação de execução registrada separadamente pelo Work.
<!-- neve-work:readme:end -->
