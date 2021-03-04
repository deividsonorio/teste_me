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

--------------
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


#### Criando contâiners para o projeto

1. Instale o Docker, por exemplo, para Windows: [Docker](https://docs.docker.com/docker-for-windows/install/)

2. Baixe este repositório:

```
  git clone git@github.com:deividsonorio/teste_me.git
```


3. Na raiz da pasta do projeto, crie as imagens necessárias com o comando:

```
  docker build
```

3. Na raiz da pasta do projeto, rode o comando para subir as imagens:

```
  docker-compose up
```

4. Comando rodado com sucesso, o projeto estará disponível em https://localhost:8000 e a administração do Djando em https://localhost:8000.

<b>OBS:</b> Como o foco do projeto é o backend, não há página inicial. Os caminhos adicionados para acesso pelo navegador são meios de rodar os comandos sem necesidade de um terminal.

--------------
### Utilizando os comandos

- O arquivo de log deve ser colocado na pasta media/process/logs.txt. Ele não foi incluído devido à limitação de tamanho de arquivo no Github.

- Para testar os comandos, você pode acessar o contâiner com o comando:

```

  docker exec -i -t log_reader /bin/bash

```

<b>OBS</b>: Quando se utiliza o Docker no Windows, é disponilizada uma interface para acesso ao contâiner.


#### Lista de comandos

Na linha de comando do container:


``` 
  python manage.py processar_logs
```

  - Processa arquivo logs.txt na pasta media/process
  - Arquivo será renomeado após o processamento para evitar reprocessamento
  - Aceita parâmetro -a ou --arquivo, com caminho para o arquivo a ser processado (nesse caso arquivo não é renomeado)

```
  python manage.py csv_requisicoes_consumidor
```

- Cria relatório de Requisições por consumidor
- Arquivo será criado na pasta media/csv
- Aceita parâmetro -a ou --arquivo, com caminho indicando onde o arquivo deve ser salvo.

```

  python manage.py csv_requisicoes_servico
```

- Cria relatório de Requisições por serviço
- Arquivo será criado na pasta media/csv
- Aceita parâmetro -a ou --arquivo, com caminho indicando onde o arquivo deve ser salvo.

```
  python manage.py csv_tempo_medio
```

- Cria relatório de Requisições por tempo médio
- Arquivo será criado na pasta media/csv
- Aceita parâmetro -a ou --arquivo, com caminho indicando onde o arquivo deve ser salvo.

#### Comando através do hospedeiro

Os comandos ficam disponíveis na porta 8000 através de URLs configuradas como rotas do Django:

##### Comandos por curl/navegador

É possível, assim como pelo navegador, chamar os comandos por curl:


``` 
  curl localhost:8000/processar_logs/
```
  - Processa arquivo logs.txt na pasta media/process


```
  curl localhost:8000/csv_requisicoes_consumidor
```
- Cria relatório de Requisições por consumidor


```

  python manage.py csv_requisicoes_servico
```
- Cria relatório de Requisições por serviço

```
  curl localhost:8000/csv_tempo_medio/
```
- Cria relatório de Requisições por tempo médio


Podem ser utilizadas as mesmas URL's no navegador. Será retornado um JSON e uma tarefa iniciada para o comando.

--------------
### Testes unitátrios

É possível rodar os testes unitários através do comando:

```
   python manage.py test reader.tests

    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ............
    ----------------------------------------------------------------------
    Ran 12 tests in 0.385s

    OK
    Destroying test database for alias 'default'...
```

--------------
### Melhorias

Devido ao pouco tempo que tive devido a outros projetos, várias recursos e melhorias poderiam ser aplicados.

- [ ] Melhoria nos models e relacionamentos do banco de dados
- [ ] Melhoria no modo de expor comandos ou requisições
- [ ] Criação de variáveis e ambientes
- [ ] Preparação para deploy em ambiente de produção