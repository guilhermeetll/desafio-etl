# Desafio de Engenharia de Dados | ETL de Proposições Legislativas

## 🚀 Objetivo:

Desenvolver um pipeline de dados em Python para extrair informações sobre proposições legislativas do estado de Minas Gerais para o ano de 2023, realizar a limpeza necessária dos dados e carregá-los em um esquema de banco de dados relacional.

## 💻 Tecnologias que utilizei:

- Python
- MySQL
- Docker
- Docker Compose

## 📜 Requisitos atingidos:

- Extração de Dados: 🚀

- Limpeza de Dados:🚀

- Carregamento de Dados:🚀

- Dockerização: 🚀

## 🥇 Diferenciais Atingidos:

- Uso de Docker Compose. 🚀
- Documentação clara do processo de configuração e execução do pipeline. 🚀
- Implementação de testes para validar a integridade dos dados. (Em andamento com testes unitários)
- Evitar a inserção de dados duplicados no banco. 🚀

## 🛠️ Execução

### Pré-requisitos

	.	Docker deve estar instalado em sua máquina.

### Passos para Rodar

	1.	Clone o Repositório:

    ```
    git clone <URL_DO_REPOSITORIO>
    cd <DIRETORIO_DO_REPOSITORIO>
    ```

    2.	Construir e Subir os Containers:
    ```
    docker-compose up --build
    ```

    **O código Python será executado automaticamente quando o container da aplicação for iniciado. O script Python realizará a extração, limpeza e carregamento dos dados.**