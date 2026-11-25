import pytest

from tarefas import core


def test_adicionar_gera_ids_sequenciais():
    ts = []
    assert core.adicionar(ts, "a")["id"] == 1
    assert core.adicionar(ts, "b")["id"] == 2


def test_titulo_vazio_falha():
    with pytest.raises(ValueError):
        core.adicionar([], "   ")


def test_concluir_e_remover():
    ts = []
    core.adicionar(ts, "a")
    assert core.concluir(ts, 1)["concluida"] is True
    core.remover(ts, 1)
    assert ts == []


def test_id_inexistente():
    with pytest.raises(KeyError):
        core.concluir([], 99)


def test_salvar_e_carregar(tmp_path):
    arq = tmp_path / "t.json"
    ts = []
    core.adicionar(ts, "ação")
    core.salvar(ts, arq)
    assert core.carregar(arq) == ts
