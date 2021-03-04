## Teste técnico

Em primeiro lugar, muito obrigado por participar do nosso processo seletivo, esperamos que tenha ocorrido tudo de acordo.

--------------

### Nossos contatos

1. Para dúvidas sobre as funcionalidades ou escopo do teste: **bruno.bermann@melhorenvio.com**, **luan.einhardt@melhorenvio.com** e **rodrigo.silveira@melhorenvio.com**
2. Para dúvidas sobre a empresa, prazos: **vanessa.santos@melhorenvio.com**

--------------

### Sobre prazos de execução
​Lhe será dado um período de 7 dias para a execução do teste contanto a partir do dia do recebimento do mesmo. Qualquer discrepância ou dúvida quanto a isto pode ser tratada diretamente conosco.

--------------

### Nossa Stack

Opte por utilizar em seu teste algumas das tecnologias da nossa stack:

- PHP/Laravel
- Golang
- Javascript/NodeJS
- Python
- Mongo
- MySQL

--------------

### Instruções

O arquivo [logs.txt](https://drive.google.com/file/d/1-2ublgv6A1_PtpxP1Nvjl626Miu68nMR/view) contém informações de log geradas por um sistema de API Gateway. Cada solicitação foi registrada em um objeto JSON separado por uma nova linha `\n`, com o seguinte formato:

```
{
    "request": {
        "method": "GET",
        "uri": "/get",
        "url": "http://httpbin.org:8000/get",
        "size": "75",
        "querystring": {},
        "headers": {
            "accept": "*/*",
            "host": "httpbin.org",
            "user-agent": "curl/7.37.1"
        },
    },
    "upstream_uri": "/",
    "response": {
        "status": 200,
        "size": "434",
        "headers": {
            "Content-Length": "197",
            "via": "gateway/0.3.0",
            "Connection": "close",
            "access-control-allow-credentials": "true",
            "Content-Type": "application/json",
            "server": "nginx",
            "access-control-allow-origin": "*"
        }
    },
    "authenticated_entity": {
        "consumer_id": "80f74eef-31b8-45d5-c525-ae532297ea8e"
    },
    "route": {
        "created_at": 1521555129,
        "hosts": null,
        "id": "75818c5f-202d-4b82-a553-6a46e7c9a19e",
        "methods": ["GET","POST","PUT","DELETE","PATCH","OPTIONS","HEAD"],
        "paths": [
            "/example-path"
        ],
        "preserve_host": false,
        "protocols": [
            "http",
            "https"
        ],
        "regex_priority": 0,
        "service": {
            "id": "0590139e-7481-466c-bcdf-929adcaaf804"
        },
        "strip_path": true,
        "updated_at": 1521555129
    },
    "service": {
        "connect_timeout": 60000,
        "created_at": 1521554518,
        "host": "example.com",
        "id": "0590139e-7481-466c-bcdf-929adcaaf804",
        "name": "myservice",
        "path": "/",
        "port": 80,
        "protocol": "http",
        "read_timeout": 60000,
        "retries": 5,
        "updated_at": 1521554518,
        "write_timeout": 60000
    },
    "latencies": {
        "proxy": 1430,
        "gateway": 9,
        "request": 1921
    },
    "client_ip": "127.0.0.1",
    "started_at": 1433209822425
}
```

***Algumas considerações sobre o objeto JSON acima:***

`latencies` contém alguns dados sobre as latências envolvidas:

-   `proxy` é o tempo levado pelo serviço final para processar a requisição.
-   `gateway` é a latência referente a execução de todos os plugins pelo gateway (API Gateway).
-   `request` é o tempo decorrido entre o primeiro byte ser lido do cliente e o último byte ser enviado a ele. Útil para detectar clientes lentos.

--------------

### Requisitos

- Processar o arquivo de log, extrair informações e salvá-las no banco de dados.
- Gerar um relatório para cada descrição abaixo, em formato csv:
    - Requisições por consumidor;
    - Requisições por serviço;
    - Tempo médio de `request`, `proxy` e `gateway` por serviço.
- Documentar passo a passo de como executar o teste através de um arquivo `README.md`.
- Efetue o `commit` de todos os passos do desenvolvimento em um ***git público*** de sua preferência e disponibilize apenas o link para o repositório.

--------------

### Sobre o quê esperamos de você

**Se você se considera júnior**, opte por realizar apenas os requisitos acima, tente fazer o máximo que conseguir da melhor forma que conseguir, não gaste seu tempo com requisitos para plenos e sêniors, isto só vai fazer com que você não consiga entregar o básico da melhor forma possível.

**Se você se considera pleno**, construa seu código de uma forma organizada e componentizada. Os itens a seguir passam a ser requisitos essenciais. Neste nível também olharemos de forma mais detalhada o seu código bem como prestaremos mais atenção na performance do mesmo.

- SOLID, KISS, YAGNI, DRY
- Design Patterns
- Clean Code

**Se você se considera sênior**, além dos itens anteriormente citados, verificaremos como você criou a arquitetura do seu projeto, como você documentou e testou o mesmo. Lembre-se que se espera de um profissional sênior a capacidade de gerar conhecimento para os pares, portanto aqui é onde você poderá mostrar o seu nível, tente mostrar seu potencial com uso de técnicas, padrões e features avançadas.

- Teste unitário
- Docker
- Arquitetura

--------------

### Considerações finais

O que será avaliado no teste é como o ***código foi escrito*** e a ***lógica*** por trás dele, então caso não consiga completar 100% dos requisitos, entregue o teste.
