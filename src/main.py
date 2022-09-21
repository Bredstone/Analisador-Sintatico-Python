#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Analisador Léxico.

Projeto de um analisador léxico, desenvolvido em Python, com utilização da
ferramenta PLY (módulo LEX).

@Author: Brendon Vicente Rocha Silva
@Email: bredstone13@gmail.com
@Date: September - 2022
"""

import sys

from resources.lexical_analyzer import LexicalAnalyzer

if __name__ == '__main__':
  try:
    if len(sys.argv) < 2 or len(sys.argv) > 4:
      raise Exception('Número de argumentos inválido!')

    _, data_file_path, *output_file_path = sys.argv
    output_file = None

    with open(data_file_path) as file:
      lex = LexicalAnalyzer()
      lex.build()
      lex.read_input(file.read())

      if len(output_file_path) >= 1: 
        output_file = open(output_file_path[0], 'w')
      lex.pretty_print_input(output_file)

      if len(output_file_path) == 2: 
        output_file = open(output_file_path[1], 'w')
      lex.symtable.pretty_print(output_file)
  except Exception as e:
    print(e)