"""Interface de linha de comando."""
import argparse
import sys

from . import core


def main(argv=None):
    p = argparse.ArgumentParser(prog="tarefas", description="Gerenciador de tarefas")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("listar", help="lista as tarefas")
    a = sub.add_parser("adicionar", help="adiciona uma tarefa")
    a.add_argument("titulo")
    c = sub.add_parser("concluir", help="marca como concluída")
    c.add_argument("id", type=int)
    r = sub.add_parser("remover", help="remove uma tarefa")
    r.add_argument("id", type=int)
    args = p.parse_args(argv)

    tarefas = core.carregar()
    try:
        if args.cmd == "listar":
            for t in tarefas:
                print(f"[{'x' if t['concluida'] else ' '}] {t['id']}. {t['titulo']}")
            return 0
        if args.cmd == "adicionar":
            t = core.adicionar(tarefas, args.titulo)
            print(f"Tarefa {t['id']} adicionada.")
        elif args.cmd == "concluir":
            core.concluir(tarefas, args.id)
            print("Tarefa concluída.")
        elif args.cmd == "remover":
            core.remover(tarefas, args.id)
            print("Tarefa removida.")
    except (ValueError, KeyError) as e:
        print(f"Erro: {e.args[0]}", file=sys.stderr)
        return 1
    core.salvar(tarefas)
    return 0


if __name__ == "__main__":
    sys.exit(main())
