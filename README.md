
# Sistema de Automação de Notificações

Este projeto tem como objetivo a automação do envio e recebimento de notificações em um ambiente de microserviços. Utiliza RabbitMQ como sistema de filas para garantir o envio assíncrono e eficiente de mensagens entre os serviços, permitindo que diferentes partes da aplicação se comuniquem de maneira desacoplada.

## Funcionalidades

- **Envio de Notificações**: Serviço API principal que recebe requisições POST com uma mensagem e envia a notificação para a fila do RabbitMQ.
- **Processamento de Notificações**: Serviço de notificação que consome mensagens da fila e realiza o processamento das notificações.
- **Integração com RabbitMQ**: Uso de RabbitMQ para comunicação entre os serviços, garantindo que as notificações sejam enviadas de forma assíncrona e escalável.

## Tecnologias Utilizadas

### Backend
- **Flask**: Framework Python para desenvolvimento rápido de APIs RESTful.
- **pika**: Biblioteca Python para integração com RabbitMQ.
- **Docker**: Containerização dos serviços para facilitar o desenvolvimento e a implantação.
- **RabbitMQ**: Sistema de mensagens para comunicação assíncrona entre os serviços.

### Infraestrutura
- **Docker Compose**: Orquestração dos containers para facilitar a configuração e o gerenciamento dos serviços.

## Como Rodar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/projeto.git
cd projeto
```

### 2. Crie e Ative um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

Se o arquivo `requirements.txt` estiver presente:

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` não exista, crie um com o seguinte conteúdo:

```makefile
Flask==2.2.2
pika==1.2.0
```

### 4. Rodando o Projeto com Docker

Se você estiver usando Docker para rodar os contêineres, o arquivo `docker-compose.yml` é fornecido para facilitar o setup.

```bash
docker-compose up --build
```

Isso irá iniciar o RabbitMQ, a API Principal e o Serviço de Notificação.

### 5. Testando a API com o Postman

#### 5.1 Enviar Notificação

Para testar a API no Postman, siga os seguintes passos:

1. Abra o Postman.
2. Crie uma nova requisição `POST` para o endpoint `/send_notification`:

    - **URL**: `http://localhost:5000/send_notification`
    - **Método**: `POST`
    - **Body** (Formato JSON):
    
    ```json
    {
        "message": "Seu processo foi atualizado."
    }
    ```

3. Clique em **Send**.

#### 5.2 Resposta Esperada

A resposta esperada será um status indicando que a mensagem foi colocada na fila do RabbitMQ:

```json
{
    "status": "Notification queued"
}
```

#### 5.3 Consumir a Notificação

O **Serviço de Notificação** irá consumir automaticamente as mensagens da fila RabbitMQ e processá-las. Ele irá exibir no log algo similar a:

```
INFO:root:Received message: Seu processo foi atualizado.
```

## Estrutura do Projeto

- **api_principal/**: Contém o código da API principal.
- **servico_notificacao/**: Contém o código para o serviço que consome as notificações.
- **docker-compose.yml**: Arquivo para rodar os contêineres Docker.

## Considerações Finais

Este projeto proporciona uma integração simples entre Flask e RabbitMQ para envio e consumo de notificações. Com o uso de Docker, o processo de setup e execução foi simplificado. O Postman pode ser utilizado para testar facilmente a API.

## Estrutura do Projeto

- **api_principal**: Serviço responsável por receber as requisições e publicar as mensagens na fila do RabbitMQ.
- **servico_notificacao**: Serviço que consome as mensagens da fila e processa as notificações.
- **Dockerfile**: Arquivo de configuração para criar os containers dos serviços.
- **docker-compose.yml**: Arquivo para orquestrar a execução dos containers.

## Exemplo de Código

### Envio de Notificação (API Principal)
```python
@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.json
    message = data.get('message', 'No message provided')
    channel.basic_publish(exchange='', routing_key='notifications', body=message)
    return jsonify({"status": "Notification queued"}), 200
```

### Consumo de Notificação (Serviço de Notificação)
```python
def callback(ch, method, properties, body):
    logging.info(f"Received message: {body.decode()}")
```

## Considerações Finais

Este projeto pode ser expandido para incluir mais funcionalidades, como diferentes tipos de notificações (email, SMS), escalabilidade com múltiplos consumidores, e persistência das notificações em banco de dados.
