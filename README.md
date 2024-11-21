# Gerenciador de Senhas

## Descrição

Este é um projeto de um Gerenciador de Senhas desenvolvido como parte do curso. O objetivo do projeto é treinar e praticar conhecimentos em desenvolvimento web, utilizando o framework Flask, banco de dados SQLite e outras tecnologias.

## Funcionalidades

- Cadastro de usuários
- Login de usuários
- Adição de novas senhas
- Listagem de senhas
- Atualização de senhas
- Exclusão de senhas
- Geração de senhas seguras

## Tecnologias Utilizadas

- Python
- Flask
- SQLite
- Bootstrap
- Jinja2
- Cryptography

## Requisitos

- Python 3.6 ou superior
- Pip (gerenciador de pacotes do Python)

## Inicialização

### Inicialização Manual

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv projeto_a3
    call projeto_a3\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Inicialize o banco de dados (se necessário):
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. Execute a aplicação:
    ```bash
    python app.py
    ```

6. Acesse a aplicação no navegador:
    ```
    http://localhost:5000
    ```

### Inicialização Automática

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Execute o script `rodar_projeto.py`:
    ```bash
    python app/rodar_projeto.py
    ```
3. Acesse a aplicação no navegador:
    ```
    http://localhost:5000
    ```

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `models/`: Diretório contendo os modelos do banco de dados.
- `controllers/`: Diretório contendo os controladores da aplicação.
- `routes/`: Diretório contendo os blueprints e rotas da aplicação.
- `templates/`: Diretório contendo os templates HTML.
- `static/`: Diretório contendo arquivos estáticos (CSS, JS, imagens).
- `requirements.txt`: Arquivo de dependências do projeto.

## Objetivo do Projeto

O objetivo do projeto é treinar e praticar conhecimentos em desenvolvimento web, utilizando o framework Flask, banco de dados SQLite e outras tecnologias. O projeto foi desenvolvido como parte do curso e inclui funcionalidades como cadastro de usuários, login, adição, listagem, atualização e exclusão de senhas, além de um gerador de senhas seguras.

## Desenvolvimento

O desenvolvimento do projeto seguiu as seguintes etapas:

1. **Levantamento de Requisitos**: Realizado através de entrevistas e classificado em requisitos funcionais e não funcionais.
2. **Diagrama de Casos de Uso e Diagrama de Classes**: Elaborados para representar a estrutura e funcionalidades do sistema.
3. **Diagrama de Atividades**: Criado para representar o fluxo de atividades do sistema.
4. **DER (Diagrama Entidade-Relacionamento)**: Desenvolvido para modelar o banco de dados.
5. **Estudo da Interface**: Realizado para definir a interface do usuário e a experiência de uso.
6. **Padrões de Projeto**: Aplicados para garantir a qualidade e manutenibilidade do código.
7. **Arquitetura do Sistema**: Definida para estruturar o sistema de forma organizada e eficiente.

## Apresentação

A apresentação do projeto será realizada conforme as orientações do curso. Todo o material deve ser postado no ulife até o dia 26/11.
