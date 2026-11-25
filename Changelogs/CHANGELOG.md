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
