#!/usr/bin/env bash
# Rode no SEU computador, logado no GitHub (gh auth login). Requer git e gh.
set -e
cd "$(dirname "$0")"

( cd gerenciador-de-tarefas && git init -q -b main && git add . \
  && git commit -qm "Projeto inicial: gerenciador de tarefas" \
  && gh repo create Gustavof07/gerenciador-de-tarefas --public \
       --description "Gerenciador de tarefas em linha de comando (Python)" --source . --push )

( cd Gustavof07 && git init -q -b main && git add . \
  && git commit -qm "README do perfil" \
  && gh repo create Gustavof07/Gustavof07 --public \
       --description "Perfil do GitHub" --source . --push )

echo "Pronto! Falta só: foto, bio e fixar o repositório no perfil."
