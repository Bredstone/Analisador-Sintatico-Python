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
	@echo RUN: make run INPUT_FILE [OUTPUT_FILE=file_path]
	@echo '  INPUT_FILE:'
	@echo '    Caminho do arquivo contendo os dados a serem analisados, na linguagem CC-2022-2.'
	@echo
	@echo '  Se nenhum argumento for especificado, executa o programa e imprime, no'
	@echo '  terminal, se a entrada é válida ou não.'
	@echo
	@echo '  OUTPUT_FILE [OPTIONAL]:'
	@echo '    Caminho para escrita dos logs de execução (pilha e entrada de dados, a cada iteração).'

run: $(VENV)/bin/activate
	$(PYTHON) src/main.py $(INPUT_FILE) $(OUTPUT_FILE)
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