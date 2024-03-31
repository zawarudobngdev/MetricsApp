# Use a imagem oficial do Python como base
FROM python:3.9

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia o arquivo de dependências e instala as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia o código fonte do back-end para o contêiner
COPY . .

# Define o comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "app.py"]
