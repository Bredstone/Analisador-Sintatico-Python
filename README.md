# **Analisador Sintático - *Python***
Autor: Brendon Vicente Rocha Silva | [LinkedIn][1]
<br />
<br />

## **Introdução**
- Projeto de um analisador sintático, desenvolvido em *Python*, com a utilização 
de um módulo de uma ferramenta autoral, [disponível aqui][2].
- O programa foi feito em conjunto com um analisador léxico, desenvolvido com a 
utilização da ferramenta *PLY* (módulo *LEX*).

Um analisador léxico é uma ferramenta capaz de converter lexemas em *tokens*.
O analisador léxico lê um programa de entrada e gera um fluxo de *tokens*.

O Analisador sintático, também conhecido como *parser*, tem como tarefa 
principal determinar se o programa de entrada, representado pelo fluxo de 
*tokens*, possui as sentenças válidas para a linguagem de programação.

<br />

**Para o projeto em questão, a linguagem empregada foi a *LCC-2022-2*.**
<br />
<br />

### ***CC-2022-2***
Abaixo encontra-se a gramática *CC-2022-2* na forma BNF:

```
PROGRAM         → (STATEMENT | FUNCLIST)?
FUNCLIST        → FUNCDEF FUNCLIST | FUNCDEF
FUNCDEF         → def ident (PARAMLIST) { STATELIST }
PARAMLIST       → ((int | float | string) ident, PARAMLIST | ( int | float | string ) ident)?
STATEMENT       → (VARDECL;    |
                   ATRIBSTAT;  |
                   PRINTSTAT;  |
                   READSTAT;   |
                   RETURNSTAT; |
                   IFSTAT;     |
                   FORSTAT     |
                   {STATELIST} |
                   break;      |
                   FUNCCALL;   |
                   ;)
VARDECL         → (int | float | string) ident ([int constant])*
ATRIBSTAT       → LVALUE = (EXPRESSION | ALLOCEXPRESSION)
FUNCCALL        → ident(PARAMLISTCALL)
PARAMLISTCALL   → (ident, PARAMLISTCALL | ident | FACTOR)?
PRINTSTAT       → print EXPRESSION
READSTAT        → read LVALUE
RETURNSTAT      → return (EXPRESSION)?
IFSTAT          → if(EXPRESSION) STATEMENT (else STATEMENT)? endif
FORSTAT         → for(ATRIBSTAT; EXPRESSION; ATRIBSTAT)
                    STATEMENT
STATELIST       → STATEMENT (STATELIST)?
ALLOCEXPRESSION → new (int | float | string) ([NUMEXPRESSION])+
EXPRESSION      → NUMEXPRESSION((< | > | <= | >= | == | !=)NUMEXPRESSION)?
NUMEXPRESSION   → TERM ((+ | −) TERM)∗
TERM            → UNARYEXPR((∗ | / | %) UNARYEXPR)∗
UNARYEXPR       → ((+ | −))? FACTOR
FACTOR          → (int_constant | float_constant | string_constant | null | LVALUE | (NUMEXPRESSION) | FUNCCALL)
LVALUE          → ident([NUMEXPRESSION])
```
<br />
<br />

### ***ConvCC-2022-2***
Para execução do código, foi necessário a conversão da gramática para a **forma convencional**:

```
PROGRAM         -> STATEMENT | FUNCLIST | &
FUNCLIST        -> FUNCDEF FUNCLIST | FUNCDEF
FUNCDEF         -> DEF ID ( PARAMLIST ) { STATELIST }
PARAMLIST       -> & | TYPE ID , PARAMLIST | TYPE ID
TYPE            -> INT | FLOAT | STRING
STATEMENT       -> VARDECL ; | ATRIBSTAT ; | PRINTSTAT ; | READSTAT ; | RETURNSTAT ; | IFSTAT ; | FORSTAT | { STATELIST } | BREAK ; | FUNCCALL ; | ;
VARDECL         -> TYPE ID INT_INDEX
INT_INDEX       -> [ INT_CONSTANT ] INT_INDEX | &
ATRIBSTAT       -> LVALUE = ATRIBSTAT'
ATRIBSTAT'      -> EXPRESSION | ALLOCEXPRESSION
FUNCCALL        -> ID ( PARAMLISTCALL )
PARAMLISTCALL   -> ID , PARAMLISTCALL | ID | FACTOR | &
PRINTSTAT       -> PRINT EXPRESSION
READSTAT        -> READ LVALUE
RETURNSTAT      -> RETURN EXPRESSION | RETURN
IFSTAT          -> IF ( EXPRESSION ) STATEMENT IFSTAT'
IFSTAT'         -> ENDIF | ELSE STATEMENT ENDIF
FORSTAT         -> FOR ( ATRIBSTAT ; EXPRESSION ; ATRIBSTAT ) STATEMENT
STATELIST       -> STATEMENT STATELIST'
STATELIST'      -> & | STATELIST
ALLOCEXPRESSION -> NEW TYPE ALLOC_SIZE
ALLOC_SIZE      -> [ NUMEXPRESSION ] ALLOC_SIZE'
ALLOC_SIZE'     -> ALLOC_SIZE | &
EXPRESSION      -> NUMEXPRESSION EXPRESSION'
EXPRESSION'     -> & | RELOP NUMEXPRESSION
RELOP           -> < | > | LESS_EQUAL_THAN | GREATER_EQUAL_THAN | EQUAL | DIFFERENT
NUMEXPRESSION   -> TERM NUMEXPRESSION'
NUMEXPRESSION'  -> SUM TERM NUMEXPRESSION' | &
SUM             -> + | -
TERM            -> UNARYEXPR TERM'
TERM'           -> & | MULTI UNARYEXPR TERM'
MULTI           -> * | / | %
UNARYEXPR       -> SUM FACTOR | FACTOR
FACTOR          -> INT_CONSTANT | FLOAT_CONSTANT | STRING_CONSTANT | NULL | LVALUE | ( NUMEXPRESSION ) | FUNCCALL
LVALUE          -> ID NUM_INDEX
NUM_INDEX       -> [ NUMEXPRESSION ] NUM_INDEX | &
```
<br />
<br />

### ***Tokens* utilizados**
Um *token* é um segmento de texto ou símbolo que pode ser manipulado por um 
analisador sintático, que fornece um significado ao texto.

Dentro da linguagem *LCC-2022-2*, foram utilizados os seguintes:
<br />
<br />

**Palavras Reservadas**
- def  
- int  
- float
- string
- break
- print
- read 
- return
- if
- else
- endif
- for  
- new  
- null
<br />
<br />

***Tokens* Literais**
- `{  }  (  )  [  ]  ;  ,  <  >  =  +  -  *  /  %`
<br />
<br />

***Tokens* não triviais**
- LESS_EQUAL_THAN (`<=`)
- GREATER_EQUAL_THAN (`>=`)
- EQUAL (`==`)
- DIFFERENT (`!=`)
- INT_CONSTANT (`[0-9]+(E[\+-]?[0-9]+)?`)
  - *Strings* formadas por um ou mais algarismos, podendo conter indicador de 
  exponencial (caractere *E*) | **Ex:** 1234E+123
- FLOAT_CONSTANT (`[0-9]+\.[0-9]+(E[\+-]?[0-9]+(\.[0-9]+)?)?`)
  - *Strings* formadas por um ou mais algarismos, com separador decimal 
  (caractere *.*), podendo conter indicador de exponencial 
  (caractere *E*) | **Ex:** 1.234E+1.23
- STRING_CONSTANT (`(".*"|\'.*\')`)
  - *Strings* quaisquer, cercadas por aspas ou aspas duplas (incluindo strings 
  vazias) | **Ex:** 'teste'
- ID (`[a-zA-Z_][a-zA-Z_0-9]*`)
  - *Strings* iniciadas por uma letra (de A à Z, ignorando capitalização) 
  ou *underline* (caractere *_*), seguido por *N* letras, números ou 
  underlines | **Ex:** multiplicar_matrizes
<br />
<br />

## Execução
### Entrada e Saída de Dados
Deve ser fornecido o caminho de um arquivo no formato *.lcc* escrito na linguagem
*LCC-2022-2* derivada por *CC-2022-2*.

As seguintes saídas são esperadas:
- **se não houver erros léxicos ou sintáticos -** uma mensagem indicando que a entrada é válida;
- **se houver erros léxicos -** uma mensagem simples de erro léxico indicando a 
linha e a coluna do arquivo de entrada onde ele ocorre;
- **se houver erros sintáticos -** uma mensagem indicando qual o local do erro, assim como qual 
entrada na tabela de reconhecimento sintático está vazia.
<br />
<br />

### *Makefile*
Para executar o programa, através do *Makefile*, execute:
```
make run INPUT_FILE [OUTPUT_FILE]
```

- **INPUT_FILE -** deve ser o arquivo de entrada do programa, contendo o código 
fonte a ser analisado, em linguagem *LC-2022-2*;
- **OUTPUT_FILE (Opcional) -** será o arquivo de saída contendo os logs de 
execução (pilha e entrada de dados, a cada iteração).
<br />
<br />

### Executando da Fonte
Para executar o programa, através do código fonte, execute:
```
pip install -r requirements.txt
python src/main.py INPUT_FILE OUTPUT_FILE
```

As mesmas regras se mantêm para **INPUT_FILE** e **OUTPUT_FILE**.

[1]: https://www.linkedin.com/in/brendon-vicente-rocha/
[2]: https://github.com/Bredstone/Linguagens-Formais