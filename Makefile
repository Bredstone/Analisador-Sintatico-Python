VENV = venv
PYTHON = $(VENV)/bin/python3 # Python 3 - 3.10
PIP = $(VENV)/bin/pip

help:
	@echo Usage: make [COMMAND]
	@echo 
	@echo Command:
	@echo '  help				Exibe ajuda acerca da execução.'
	@echo '  run				Executa o programa.'
	@echo '  clean				Remove os artefatos criados.'
	@echo 
	@echo RUN: make run INPUT_FILE [ARG1=file_path ARG2=file_path]
	@echo '  INPUT_FILE:'
	@echo '    Caminho do arquivo contendo os dados a serem analisados.'
	@echo
	@echo '  Se nenhum argumento for especificado, executa o programa e imprime, no'
	@echo '  terminal, os tokens computados e a tabela de símbolos.'
	@echo
	@echo '  ARG1:'
	@echo '    Caminho para escrita dos tokens (e tabela).'
	@echo '    Se apenas ARG1 for especificado, imprime os tokens computados e a'
	@echo '    tabela de símbolos no mesmo arquivo.'
	@echo '  ARG2:'
	@echo '    Caminho para escrita da tabela de símbolos.'

run: $(VENV)/bin/activate
	$(PYTHON) src/main.py $(INPUT_FILE) $(SYMBOLS_PATH) $(SYMTABLE_PATH)
	@make clean

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	@rm -rf $(VENV)
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +