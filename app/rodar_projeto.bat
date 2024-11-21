@echo off
setlocal

REM Define o nome do ambiente virtual e o arquivo de requisitos
set NOME_AMBIENTE=projeto_a3
set ARQUIVO_REQUISITOS=requirements.txt

REM Verifica se o diretório de migrações existe
if not exist "migrations" (
    echo Inicializando o banco de dados...
    flask db init
    flask db migrate -m "Migração inicial"
    flask db upgrade
) else (
    echo O diretório de migrações já existe.
)

REM Verifica se o ambiente virtual existe
if not exist "%NOME_AMBIENTE%\Scripts\activate" (
    echo Criando ambiente virtual...
    python -m venv %NOME_AMBIENTE%
) else (
    echo O ambiente virtual já existe.
)

REM Ativa o ambiente virtual
call "%NOME_AMBIENTE%\Scripts\activate"

REM Instala os pacotes necessários
if exist %ARQUIVO_REQUISITOS% (
    echo Instalando pacotes necessários...
    pip install -r %ARQUIVO_REQUISITOS%
) else (
    echo Arquivo de requisitos não encontrado.
)

REM Executa a aplicação
echo Executando a aplicação...
python app.py

endlocal