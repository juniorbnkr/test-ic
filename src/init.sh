#!/bin/bash
# Etapas de ingestão
# python3 /ingestion/attachments.py
# python3 /ingestion/demonstracoes.py

# Etapas de tranformação (load)
# python3 /transformation/rol_procedimentos_csv.py
# python3 /transformation/operadoras_ativas.py
# python3 /transformation/demonstracoes.py
echo -e "\e[34;47m Pipeline finalizado. Confira as tabelas no no banco localhost \e[m"

#server
echo -e "\e[34;47m Inicializando server... \e[m"
python3 /server/main.py


