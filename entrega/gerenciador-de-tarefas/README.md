# Gerenciador de Tarefas

> Aplicação de linha de comando em Python para adicionar, listar, concluir e remover tarefas.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Licença](https://img.shields.io/badge/licença-MIT-green)
![Testes](https://img.shields.io/badge/testes-pytest-brightgreen)

## 📋 Sobre

Projeto acadêmico que demonstra organização de código, testes automatizados e boas práticas de documentação em um repositório GitHub. As tarefas ficam salvas em um arquivo JSON local (`~/.tarefas.json`).

## ✨ Funcionalidades

- ✅ Adicionar tarefas
- ✅ Listar tarefas com status
- ✅ Marcar tarefas como concluídas
- ✅ Remover tarefas
- ✅ Persistência em arquivo JSON

## 🚀 Como executar

Requisito: Python 3.9 ou superior.

```bash
git clone https://github.com/Gustavof07/gerenciador-de-tarefas.git
cd gerenciador-de-tarefas
export PYTHONPATH=src
```

Exemplos de uso:

```bash
python -m tarefas adicionar "Entregar trabalho da faculdade"
python -m tarefas listar
python -m tarefas concluir 1
python -m tarefas remover 1
```

Saída de `listar`:

```
[x] 1. Entregar trabalho da faculdade
[ ] 2. Estudar para a prova
```

## 🧪 Testes

```bash
pip install pytest
pytest
```

## 📁 Estrutura

```
gerenciador-de-tarefas/
├── src/tarefas/
│   ├── core.py      # regras de negócio
│   ├── cli.py       # interface de linha de comando
│   └── __main__.py
├── tests/           # testes automatizados
├── docs/            # documentação adicional
├── pyproject.toml
├── LICENSE
└── README.md
```

## 🛠️ Tecnologias

Python · argparse · JSON · pytest

## 👤 Autor

**Gustavo** — [@Gustavof07](https://github.com/Gustavof07)

## 📄 Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE).
