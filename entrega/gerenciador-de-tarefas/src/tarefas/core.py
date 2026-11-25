"""Regras de negócio: carregar, salvar e manipular tarefas."""
import json
from pathlib import Path

ARQUIVO_PADRAO = Path.home() / ".tarefas.json"


def carregar(caminho=ARQUIVO_PADRAO):
    caminho = Path(caminho)
    if not caminho.exists():
        return []
    return json.loads(caminho.read_text(encoding="utf-8"))


def salvar(tarefas, caminho=ARQUIVO_PADRAO):
    Path(caminho).write_text(
        json.dumps(tarefas, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def adicionar(tarefas, titulo):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("O título não pode ser vazio.")
    novo_id = max((t["id"] for t in tarefas), default=0) + 1
    tarefa = {"id": novo_id, "titulo": titulo, "concluida": False}
    tarefas.append(tarefa)
    return tarefa


def concluir(tarefas, id_tarefa):
    for t in tarefas:
        if t["id"] == id_tarefa:
            t["concluida"] = True
            return t
    raise KeyError(f"Tarefa {id_tarefa} não encontrada.")


def remover(tarefas, id_tarefa):
    for i, t in enumerate(tarefas):
        if t["id"] == id_tarefa:
            return tarefas.pop(i)
    raise KeyError(f"Tarefa {id_tarefa} não encontrada.")
