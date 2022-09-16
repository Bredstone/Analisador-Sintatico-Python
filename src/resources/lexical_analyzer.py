#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Analisador Léxico.

Projeto de um analisador léxico, desenvolvido em Python, com utilização da
ferramenta PLY (módulo LEX).

@Author: Brendon Vicente Rocha Silva
@Email: bredstone13@gmail.com
@Date: September - 2022
"""

import resources.ply.lex as lex

class LexicalAnalyzer(object):
  '''Analisador léxico para linguagem CC-2022-2.'''
  
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
  t_STRING_CONSTANT    = r'".*"'
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
    ----------
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
    Lê uma entrada e computa os tokens contidos nela.
    
    Parameters
    ----------
    data : str
      Dados a serem lidos.
    '''

    self.data = data
    self.lexer.input(data)
    self.token_list = [token for token in self.lexer]

  def pretty_print_input(self):
    '''Imprime os tokens computados pelo analisador, em formato legível.'''

    n_tabs = 0
    last_line = 1
    string = ''
    for token in self.token_list:
      if token.value == '}': n_tabs -= 1

      if token.lineno != last_line: 
        last_line = token.lineno
        string += '\n' + '  ' * n_tabs

      string += (
        ('\b' if token.value in '[]]);,' and string[-1] not in '[(' else '') + 
        token.type + 
        (' ' if token.value not in '[(' else ''))

      if token.value == '{': n_tabs += 1
    
    print(string)

  