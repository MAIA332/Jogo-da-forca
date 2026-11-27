# Dockerfile para Jogo da Forca em Python
# Baseado em Python 3.11 (versão estável e compatível com o projeto)
# Otimizado para rodar em qualquer máquina (Windows, macOS, Linux) via Docker
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências (se houver requirements.txt)
# Caso contrário, instala as dependências diretamente do código
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app

ENTRYPOINT ["python", "Main.py"]
