## Teste técnico

O teste foi realizado em Python, com uso do framework Django.

O foco foi a criação de comandos que realizam a leitura de logs e criação dos arquivos CSV.

Sendo assim estes poderiam ser agendados em um cron no servidor ou chamados quando necessários, sem depender de interfaces.

Todavia foram adicionados meio dos comandos serem chamados através do navegador, criando tarefas assíncronas realizadas no backend.

### Requisitos

- Processar o arquivo de log, extrair informações e salvá-las no banco de dados.
- Gerar um relatório para cada descrição abaixo, em formato csv:
  - Requisições por consumidor;
  - Requisições por serviço;
  - Tempo médio de `request`, `proxy` e `gateway` por serviço.
- Documentar passo a passo de como executar o teste através de um arquivo `README.md`.
- Efetue o `commit` de todos os passos do desenvolvimento em um ***git público*** de sua preferência e disponibilize apenas o link para o repositório.

### Tecnologias utilizadas

- Python
- Django
- Docker
- PostgreSQL

--------------
### Dependências

Os pacotes necessários estão listados no arquivo requirements.txt na raiz do projeto.

A instalação dos mesmo é feita automaticamente pelo docker-compose.

--------------

### Instruções

O projeto foi desenvolvido de forma simples e rápida. 

Configurações de ambientes não foram adicionadas, focando no funcionamento para atender aos requisitos.


## Criando imagens para o projeto

1. Instale o Docker, por exemplo, para Windows: [Docker](https://docs.docker.com/docker-for-windows/install/)

2. Baixe deste repositório.

<code>

  git clone git@github.com:deividsonorio/teste_me.git

</code>


3. Na raiz da pasta do projeto, crie as imagens necessárias com o comando:

<code>

  docker build

</code>

3. Na raiz da pasta do projeto, rode o comando para subir as imagens:

<code>

  docker-compose up

</code>

4. Comando rodado com sucesso, o projeto estará disponível em https://localhost:8000 e a administração do Djando em https://localhost:8000.

OBS: Como o foco do projeto é o backend, não há página inicial. Os caminhos adicionados para acesso pelo navegador são meios de rodar os comandos sem necesidade de um terminal.

## Utilizando os comandos

- O arquivo de log deve ser colocado na pasta media/process/logs.txt. Ele não foi incluído devido à limitação de tamanho de arquivo no Github.

- Para testar os comandos, você pode acessar o contâiner com o comando:

<code>

  docker exec -i -t log_reader /bin/bash

</code>

OBS: Quando se utiliza o Docker no Windows, é disponilizada uma interface para acesso ao contâiner.
