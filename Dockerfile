# Dockerfile para Jogo da Forca em Python
# Baseado em Python 3.11 (versão estável e compatível com o projeto)
# Otimizado para rodar em qualquer máquina (Windows, macOS, Linux) via Docker
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências (se houver requirements.txt)
# Caso contrário, instala as dependências diretamente do código
COPY . .

# Instala as dependências com tratamento de erros robusto
RUN pip install --no-cache-dir -r requirements.txt 2>/dev/null || pip install --no-cache-dir -e . 2>/dev/null || pip install --no-cache-dir -r requirements.txt

# Instala o sistema de arquivos VFS para suporte a arquivos de texto em Windows
RUN apt-get update && apt-get install -y --no-install-recommends \
    vfs \
    && rm -rf /var/lib/apt/lists/*

# Define o comando de entrada padrão
CMD ["python", "Main.py"]

# Define o diretório de trabalho para o jogo
WORKDIR /app

# Expor a porta padrão do jogo (ajuste conforme necessário se houver servidor)
# Para CLI, não é estritamente necessário, mas é bom para consistência
EXPOSE 8000

# Define o comando de entrada
CMD ["python", "-m", "Main"]
# Executa o Main.py diretamente, permitindo execução interativa
ENTRYPOINT ["python", "Main.py"]

# Permite que o usuário passe argumentos para o jogo
CMD ["--help"]
