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

import resources.ply.lex as lex
from resources.symtable import Symtable

class LexicalAnalyzer(object):
  '''Analisador léxico para linguagem LCC-2022-2.'''
  
  # Lista de palavras reservadas.
  reserved = {
    'def': 'DEF',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'break': 'BREAK',
    'print': 'PRINT',
    'read': 'READ',
    'return': 'RETURN',
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'new': 'NEW',
    'null': 'NULL',
  }

  # Lista de tokens.
  tokens = (
  'ID',
  'LESS_EQUAL_THAN',
  'GREATER_EQUAL_THAN',
  'EQUAL',
  'DIFFERENT',
  'INT_CONSTANT',
  'FLOAT_CONSTANT',
  'STRING_CONSTANT',
) + tuple(reserved.values())

  # Lista de literais.
  literals = '{}()[];,<>=+-*/%'

  # Especificação dos tokens
  t_LESS_EQUAL_THAN    = r'<='
  t_GREATER_EQUAL_THAN = r'>='
  t_EQUAL              = r'=='
  t_DIFFERENT          = r'!='
  t_INT_CONSTANT       = r'[0-9]+(E[\+-]?[0-9]+)?'
  t_FLOAT_CONSTANT     = r'[0-9]+\.[0-9]+(E[\+-]?[0-9]+(\.[0-9]+)?)?'
  t_STRING_CONSTANT    = r'(".*"|\'.*\')'
  t_ignore             = ' \t'
  
  def t_ID(self, t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = self.reserved.get(t.value,'ID')
    return t

  def t_newline(self, t):
    r'\n+'
    t.lexer.lineno += len(t.value)

  def t_error(self, t):
    raise Exception(f"Caractere inválido '{t.value[0]}', na linha {t.lineno} e coluna {self.find_column(t)}")

  def find_column(self, t):
    '''
    Encontra a coluna de determinado token.
    
    Returns
    -------
    int
      Coluna do token avaliado.
    '''

    line_start = self.data.rfind('\n', 0, t.lexpos) + 1
    return (t.lexpos - line_start) + 1

  def build(self, **kwargs):
    '''Constrói o analisador.'''

    self.lexer = lex.lex(module=self, **kwargs)

  def read_input(self, data):
    '''
    Lê uma entrada, computa os tokens contidos nela e constrói a tabela
    de símbolos.
    
    Parameters
    ----------
    data : str
      Dados a serem lidos.
    '''

    if not hasattr(self, 'lexer'):
      raise Exception('O analisador não foi inicializado!')

    self.data = data
    self.lexer.input(data)
    self.token_list = []
    self.symtable = Symtable()
    for token in self.lexer:
      self.token_list.append(token)

      if token.type == 'ID':
        self.symtable.add_item(token.value, (token.lineno, self.find_column(token)))

  def pretty_print_input(self, file=sys.stdout):
    '''
    Imprime, onde especificado, os tokens computados pelo analisador, em 
    formato legível.
    
    Parameters
    ----------
    file : str (default = sys.stdout)
      Caminho de saída para impressão dos tokens.
    '''

    if not hasattr(self, 'data'):
      raise Exception('Nenhum dado fornecido como entrada!')

    n_tabs = 0
    last_line = 1
    string = ''

    for token in self.token_list:
      if token.value in '})': n_tabs -= 1

      while token.lineno != last_line: 
        last_line += 1
        string += '\n' + '  ' * n_tabs

      if token.value in '[]);,' and string[-1] not in '[(': string = string[:-1]
      string += token.type
      if token.value not in '[(': string += ' '

      if token.value in '{(': n_tabs += 1
    
    print(string, file=file)

  