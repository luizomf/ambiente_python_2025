# Ambiente Python + VS Code 2025

**Quer entender tudo o que está nesse projeto?**

Eu explico passo a passo como montar esse ambiente moderno nos vídeos abaixo:

- Parte 1: [Ambiente Python Moderno - Tradicional](https://youtu.be/QTw5eB6GTM8)
- Parte 2: [Ambiente Python Moderno - Pyenv e Pyenv-win](https://youtu.be/X38M7C_A2XU)
- Parte 3: [Ambiente Python Moderno - UV Astral](https://youtu.be/HuAc85cLRx0)
- Parte 4: [Como iniciar novos projetos com Ambiente Python Moderno](https://youtu.be/TcfFXur4YKg)

---

## Sobre

Este projeto serve como um esqueleto moderno para projetos Python utilizando:

- Python 3.13+
- VS Code com extensões
- Ambiente virtual (venv ou [uv](https://docs.astral.sh/uv/getting-started/))
- Controle de versões do Python ([pyenv](https://github.com/pyenv/pyenv) / [pyenv-win](https://github.com/pyenv-win/pyenv-win) ou [uv](https://docs.astral.sh/uv/getting-started/))
- Lint e formatação com [Ruff](https://github.com/astral-sh/ruff)
- Tipagem estática e Lint com Pylance e [Pyright](https://github.com/microsoft/pyright)
- Execução e testes rápidos com Code Runner
- Configuração geral do VS Code
- Temas para ícones e VS Code
- Configuração inicial do Git no projeto

---

## Requisitos iniciais

Recomendo já ter as versões oficiais das coisas que vamos configurar. Isso evita que a extensão do Python para VS Code não funcione por algum motivo que desconheço (ao meu ver, um bug da própria extensão, mas infelizmente precisamos dela para integração com o VS Code).

Portanto, tenha o seguinte já instalado no seu computador:

1. O [Python](https://www.python.org/downloads/)
2. O [Git](https://git-scm.com/downloads)
3. O [VS Code](https://code.visualstudio.com/)

Se você usa Windows, libere o PowerShell para executar scripts:

1. Abra o Terminal ou PowerShell **como administrador**
2. Cole o comando abaixo e pressione `ENTER`:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Reinicie o computador se necessário.

---

## Ambiente Python com Python, pip e venv

Esse é o ambiente tradicional mais atualizado. Tradicional porque vamos usar coisas
que são amplamente usadas no mundo Python, como: o python na sua última versão, pip (que vem com o Python) e o venv para criar nosso ambiente virtual.

O processo é super simples:

1. Crie uma pasta para o seu projeto
2. Abra essa pasta com o VS Code (File > Open Folder)
3. Abra o terminal dentro da pasta (CTRL ou CMD + J) e digite

```sh
python -m venv .venv
# Ativa o ambiente virtual e depois instale o python-dotenv
pip install python-dotenv
```

Pronto, agora siga as instruções do vídeo tutorial.

---

## pyenv e pyenv-win

O Pyenv é uma lib que gerencia versões do Python. Ele permite que você instale, desinstale e use várias versões do Python no mesmo sistema operacional.

Para Windows você precisa liberar o PowerShell:

```powershell
# Execute o powershell como administrador
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Links - ([pyenv](https://github.com/pyenv/pyenv) / [pyenv-win](https://github.com/pyenv-win/pyenv-win))

Após a instalação, os comandos abaixo vão te ajudar.

```sh
# Comandos
pyenv commands # lista os comandos
pyenv install -l # lista as versões do Python disponíveis
pyenv install 3.13.3 # Instala o Python 3.13.3
pyenv versions # Mostra as verões do Python instaladas
pyenv local 3.13.3 # Configura o Python 3.13.3 na pasta e suas sub-pastas
pyenv global 3.13.3 # configura o Python 3.13.3 globalmente no sistema todo
pyenv exec # Executa algum comando com o Python selecionado, ex abaixo:

pyenv install 3.11.9 # Instala o Python 3.11.9
pyenv global 3.11.9 # Configura o Python 3.11.9 como global (usarei com exec)
pyenv exec python -m venv .venv # Cria um ambiente virtual com o Python global
```

Pronto, agora siga as instruções do vídeo tutorial.

---

## Gerenciando tudo com o uv

[uv](https://docs.astral.sh/uv/getting-started/) é uma ferramenta que promete bastante. Sua intenção é substituir praticamente todas as outras ferramentas: pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, e outras... Até agora tem cumprido tudo com perfeição. Além disso, é uma ferramenta extremamente rápida, escrita em Rust.

```sh
# Instalação do uv (Windows, Linux, Mac)
# Windows PowerShell:
iwr https://astral.sh/uv/install.ps1 -useb | iex

# Linux/macOS (curl)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```sh
# Cria o projeto completo
diretório: uv init nome-do-projeto

# Ou inicializa dentro de um projeto existente:
uv init
```

```sh
# Instala Python, cria venv e instala dependências em 1 comando
uv sync
```

```sh
# Instala pacotes
uv add requests ruff pyright

# Remove pacotes
uv remove requests

# Requerimentos via requirements.txt
uv add -r requirements.txt
```

```sh
# Executa scripts Python sem ativar venv
uv run src/main.py

# Instala ferramentas como ruff ou pyright globalmente
uv tool install ruff
uvx ruff
uv tool uninstall ruff
```

---

## Configuração do Git

```bash
# Inicia o repositório
git init # Não precisa fazer isso se a uv já fez

# Configura usuário global
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# Padroniza branches para 'main'
git config --global init.defaultBranch main
git branch -m main

# Padroniza finais de linha para multiplataforma
git config --global core.autocrlf input
git config --global core.eol lf

git config --list --global

# Primeiro commit
git add .
git commit -m "initial"

# Configurar o repositório
git remote add origin URL_REPO_SSH
git push origin main -u

# Nos próximos
git add .
git commit -m "MENSAGEM"
git push
```

---

## `.env` e `.env-example`

É extremamente comum precisarmos de variáveis de ambiente em nossos projetos. Sabendo
disso, já adicionei o `python-dotenv` como dependência do projeto.

Para instalar escolha uma das opções abaixo:

```bash
# Opção 1: pip
pip install python-dotenv
# Opção 2: uv pip
uv pip install python-dotenv
# Opção 3: uv
uv sync
```

Copie o arquivo `.env-example` para outro arquivo chamado de `.env` para ativar as
variáveis de ambiente. Já deixei um teste na função principal que pode responder duas coisas:

- `Check dotenv: dotenv is working fine`
- `Check dotenv: Not working. Read the README.md`

As mensagens são auto explicativas. Se você receber `Not working`, provavelmente não copiou o arquivo `.env-example` para `.env`.
