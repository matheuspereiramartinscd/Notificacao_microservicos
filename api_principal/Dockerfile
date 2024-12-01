# Dockerfile para o serviço api_principal

# Usando uma imagem base (por exemplo, Python)
FROM python:3.9-slim

# Copiar o script wait-for-it.sh para dentro do contêiner
COPY wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it

# Instalar dependências do Python
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

# Copiar o código da aplicação
COPY . /app/

# Expor a porta necessária
EXPOSE 5000

# Definir o comando de inicialização com wait-for-it
ENTRYPOINT ["wait-for-it", "rabbitmq:5672", "--", "python", "app.py"]
