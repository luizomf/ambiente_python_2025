# Ambiente Python + VS Code 2025

**Quer entender tudo o que está nesse projeto?**


Eu explico passo a passo como montar esse ambiente moderno no vídeo abaixo:

- [https://youtu.be/zk40AZqF-FE](https://youtu.be/zk40AZqF-FE)

---

## Sobre

Este projeto serve como um esqueleto moderno para projetos Python utilizando:

- Python 3.13+
- VS Code com extensões otimizadas
- Ambiente virtual (venv)
- Lint e formatação com [Ruff](https://github.com/astral-sh/ruff)
- Tipagem estática com [Pyright](https://github.com/microsoft/pyright)
- Execução e testes rápidos com Code Runner

---

## 🚀 Requisitos iniciais

1. Instalar o [Python](https://www.python.org/downloads/)
2. Instalar o [Git](https://git-scm.com/downloads)
3. Instalar o [VS Code](https://code.visualstudio.com/)
4. Instalar e configurar o [pyenv (ou pyenv-win)](https://github.com/pyenv-win/pyenv-win)

---

## 💾 Configuração do Git

```bash
# Inicia o repositório
git init

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
```

---

## 🧑‍💻 Ambiente Python com pyenv

```bash
# Instala e configura a versão desejada do Python
pyenv install -l
pyenv install 3.13.3
pyenv global 3.13.3

python --version  # Deve exibir 3.13.3
```

---

## 🔧 Ambiente virtual

```bash
# Dentro da pasta do projeto:
python -m venv venv

# Ativação:
# Linux/macOS
source venv/bin/activate

# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
.\venv\Scripts\activate.bat
```

---

## 🔍 Linting e Tipagem

```bash
# Com o ambiente ativado:
pip install ruff pyright
```

O VS Code reconhecerá essas ferramentas automaticamente se você usar as extensões recomendadas (ver abaixo).

---

## 📄 Instalação do App (modo editável)

```bash
pip install -e .
```

Agora você pode rodar o app diretamente no terminal com:

```bash
app_b  # ou o nome definido no [project.scripts]
```

---

## 🌐 Extensões recomendadas do VS Code

```json
{
  "recommendations": [
    "ms-python.python",
    "charliermarsh.ruff",
    "tamasfe.even-better-toml",
    "formulahendry.code-runner",
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",
    "chadalen.vscode-jetbrains-icon-theme",
    "omthemes.omthemes"
  ]
}
```

---

## 🌐 Outras dicas

- O `pyproject.toml` deste repositório já está configurado com tudo que você precisa: Ruff, Pyright e dependências opcionais
- O VS Code vai funcionar **sem instalar ruff ou pyright no terminal**, graças às extensões. Mas instale-os com `pip` se quiser rodar fora do editor
- O `ruff` está configurado para corrigir automaticamente e aplicar centenas de boas práticas de produção

---

Pronto! Seu ambiente está moderno, limpo e produtivo para qualquer projeto Python em 2025 ✨
