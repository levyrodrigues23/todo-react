FROM node:18-alpine AS build

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos de dependências
COPY package.json package-lock.json* ./

# Instalando as dependências
RUN npm ci

# Copiando o resto do código-fonte
COPY . .

# Construindo a aplicação
RUN npm run build

# Estágio de produção
FROM nginx:stable-alpine

# Copiando os arquivos de build para o diretório do Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Expondo a porta 80
EXPOSE 80

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]
