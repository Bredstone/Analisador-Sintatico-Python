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

from tabulate import tabulate

class Symtable(object):
  '''Tabela de símbolos.'''

  def __init__(self):
    '''Método construtor.'''

    self.table = {}

  def add_item(self, item, value):
    '''
    Adiciona um item à tabela de símbolos.
    
    Parameters
    ----------
    item : str
      Lexema a ser adicionado.
    value : tuple(int, int)
      Tupla contendo linha e coluna do token.
    '''

    self.table[item] = self.table.get(item, []) + [value]

  def pretty_print(self, file=sys.stdout, tablefmt='fancy_grid'):
    '''
    Imprime, onde especificado, a tabela de símbolos para o código analisado.
    
    Parameters
    ----------
    file : str (default = sys.stdout)
      Caminho de saída para impressão dos tokens.
    tablefmt : str (default = 'fancy_grid')
      Formato de impressão da tabela (verificar documentação do tabulate para 
      referências).
    '''

    separator = '<BR />' if tablefmt == 'html' else '\n'
    print(
      tabulate(
        ((key, separator.join([str(x) for x in positions])) for key, positions in self.table.items()), 
        headers=['ID', '(LINHA, COLUNA)'],
        colalign=('left', 'center'),
        tablefmt=tablefmt
      ), file=file
    )
