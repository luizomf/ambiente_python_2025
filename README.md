# Ambiente Python + VS Code 2025

Um esqueleto de um projeto Python com as configurações prontas para o VS Code, Ruff e PyRight.

## Instalações

- Baixar e instalar Python
- Baixar e instalar Git
- Baixar e instalar VS Code
- Instalar e configurar o Pyenv

## Configurar o Git

```sh
# Inicia o repositório
git init

# Configurar o nome do usuário
git config --global user.name "Luiz Otávio"

# Configurar o e-mail do usuário
git config --global user.email "luizomf@gmail.com"

# Configura os novos branchs para serem iniciados como main
git config --global init.defaultBranch main

# Muda o nome do branch para main caso necessário
git branch -m main

# Garantir que o Git converta CRLF para LF apenas ao commitar (ótimo para projetos multiplataforma)
git config --global core.autocrlf input

# Forçar o Git a usar LF como fim de linha sempre
git config --global core.eol lf

# Verificar as configurações aplicadas
git config --list --global

# Adicionando o repositório
git add .
git commit -m "initial"
git remote add origin LINK-REPO
git push origin main -u
```

---

## Configurar o Python

```sh
# Execute o terminal como administrador e digite
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

pyenv install -l  # escolha a versão (possivelmente 3.x.x -> agora 3.13.3)
pyenv install 3.13.3
pyenv global 3.13.3
python --version # deve sair a versão instalada

# Dentro da pasta do seu projeto
# Crie e ative o ambiente
python -m venv venv

# Ative o ambiente
source venv/bin/activate
# ou no Windows (powershell)
.\venv\Scripts\Activate.ps1
# ou no Windows (cmd)
.\venv\Scripts\activate.bat

# Pronto, ambiente python configurado
```

# Ruff e Pyright

```sh
# Ative o ambiente (como mostro acima)
pip install ruff pyright
```

## Arquivo `pyproject.toml`

Use o arquivo de exemplo do projeto

## Quando já tiver a estrutura pronta

```sh
pip install -e .
# agora você poderá chamar o seu app pelo nome
```

## Pyenv

```sh
# Execute o terminal como administrador e digite
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# No Windows siga as instruções em:
# https://github.com/pyenv-win/pyenv-win
# Para instalar o Pyenv

pyenv install -l  # escolha a versão (possivelmente 3.x.x -> agora 3.13.3)
pyenv install 3.13.3
pyenv global 3.13.3  # ou local
python --version # deve sair a versão instalada
```
