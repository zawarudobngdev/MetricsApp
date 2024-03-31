# Use a imagem oficial do Node.js como base
FROM node:14

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia o arquivo de dependências e instala as dependências
COPY package*.json ./
RUN npm install

# Copia o código fonte do front-end para o contêiner
COPY . .

# Compila o código do Vue.js para produção
RUN npm run build

# Define o comando padrão a ser executado quando o contêiner for iniciado
CMD ["npm", "run", "serve"]
