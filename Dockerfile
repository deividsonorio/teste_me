# imagem oficial do Python 3.9
FROM python:3.9

# variável de ambiente que garante que a saída python seja enviada
# para o terminal sem armazenr primeiro
ENV PYTHONUNBUFFERED 1

# cria o diretório raiz para o projeto no container
RUN mkdir /teste_me

# seta o diretório de trabalho para /teste_me
WORKDIR /teste_me

# Copia o conteúdo do diretório atual para o container em /teste_me/
ADD . /teste_me/

# Instala os pacotes especificados no requirements.txt
RUN pip install -r requirements.txt