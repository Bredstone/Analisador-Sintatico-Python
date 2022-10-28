#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Analisador Sintático.

Projeto de um analisador sintático, desenvolvido em Python; em conjunto com um 
analisador léxico, construído com auxílio da ferramenta PLY (módulo LEX).

@Author: Brendon Vicente Rocha Silva
@Email: bredstone13@gmail.com
@Date: October - 2022
"""

import sys

from resources.parser.grammar import Grammar

if __name__ == '__main__':
  try:
    if len(sys.argv) < 2 or len(sys.argv) > 4:
      raise Exception('Número de argumentos inválido!')

    _, data_file_path, *output_file_path = sys.argv
    output_file = None
    verbose = False

    with open(data_file_path) as file:
      parser = Grammar.fromFile('./src/resources/grammar.txt')
      
      if len(output_file_path) >= 1: 
        output_file = open(output_file_path[0], 'w')
        verbose = True

      if parser.readInputLEX(file, output_file=output_file, verbose=verbose):
        print('Código válido!')
  except Exception as e:
    print(e)