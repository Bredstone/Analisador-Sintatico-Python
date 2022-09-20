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
    if len(sys.argv) == 2:
      _, data_file = sys.argv
      output_file = output_file2 = None
    elif len(sys.argv) == 3:
      _, data_file, output_file = sys.argv
      output_file2 = None
    elif len(sys.argv) == 4:
      _, data_file, output_file, output_file2 = sys.argv
    else:
      raise Exception('Número de argumentos inválido!')
    
    with open(data_file) as file:
      lex = LexicalAnalyzer()
      lex.build()
      lex.read_input(file.read())
      if output_file: output_file = open(output_file, 'w')
      lex.pretty_print_input(output_file)
      if output_file2: output_file = open(output_file2, 'w')
      lex.symtable.pretty_print(output_file, tablefmt='html' if output_file2.endswith('.html') else None)
  except Exception as e:
    print(e)