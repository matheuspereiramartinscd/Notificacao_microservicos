
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

### Instalação

#### 1. **Clone o repositório**:
```bash
git clone https://github.com/seuusuario/projeto.git
cd projeto
```

#### 2. **Instale as dependências do Python**:

No diretório do projeto, crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scriptsctivate
```

Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

#### 3. **Configuração do Docker**:

Certifique-se de ter o Docker e o Docker Compose instalados. Para instalar o Docker, siga as instruções no [site oficial](https://www.docker.com/products/docker-desktop).

#### 4. **Rodando os Containers**:

Execute o seguinte comando para subir os containers do RabbitMQ, API principal e serviço de notificação:
```bash
docker-compose up --build
```

Os serviços serão iniciados e estarão disponíveis em:
- **RabbitMQ Management Console**: http://localhost:15672 (usuário: guest, senha: guest)
- **API Principal**: http://localhost:5000

#### 5. **Testando a API**:

Use uma ferramenta como o [Postman](https://www.postman.com/) ou `curl` para enviar requisições POST para o endpoint `/send_notification`:

```bash
curl -X POST http://localhost:5000/send_notification -H "Content-Type: application/json" -d '{"message": "Sua notificação foi processada!"}'
```

Isso irá enviar a mensagem para a fila de notificações do RabbitMQ, que será consumida pelo serviço de notificação.

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
