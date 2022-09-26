# **Analisador Léxico - *Python***
Autor: Brendon Vicente Rocha Silva | [LinkedIn][1]
<br />
<br />

## **Introdução**
Projeto de um analisador léxico, desenvolvido em *Python*, com utilização da
ferramenta *PLY* (módulo *LEX*).

Um analisador léxico é uma ferramenta capaz de converter lexemas em *tokens*.
Para o projeto em questão, a linguagem empregada foi a *LCC-2022-2*.
<br />
<br />

### ***LCC-2022-2***
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
                   IFSTAT      |
                   FORSTAT     |
                   {STATELIST} |
                   break;      |
                   ;)
VARDECL         → (int | float | string) ident ([int constant])*
ATRIBSTAT       → LVALUE = (EXPRESSION | ALLOCEXPRESSION | FUNCCALL)
FUNCCALL        → ident(PARAMLISTCALL)
PARAMLISTCALL   → (ident, PARAMLISTCALL | ident)?
PRINTSTAT       → print EXPRESSION
READSTAT        → read LVALUE
RETURNSTAT      → return
IFSTAT          → if(EXPRESSION) STATEMENT (else STATEMENT)?
FORSTAT         → for(ATRIBSTAT; EXPRESSION; ATRIBSTAT)
                    STATEMENT
STATELIST       → STATEMENT (STATELIST)?
ALLOCEXPRESSION → new (int | float | string) ([NUMEXPRESSION])+
EXPRESSION      → NUMEXPRESSION((< | > | <= | >= | == | !=)NUMEXPRESSION)?
NUMEXPRESSION   → TERM ((+ | −) TERM)∗
TERM            → UNARYEXPR((∗ | / | %) UNARYEXPR)∗
UNARYEXPR       → ((+ | −))? FACTOR
FACTOR          → (int constant | float constant | string constant | null | LVALUE | (NUMEXPRESSION))
LVALUE          → ident([NUMEXP RESSION])
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
- **se não houver erros léxicos -** uma lista de tokens (na mesma ordem em que eles
ocorrem no arquivo dado na entrada) e uma tabela de símbolos;
- **se houver erros léxicos -** uma mensagem simples de erro léxico indicando a 
linha e a coluna do arquivo de entrada onde ele ocorre.
<br />
<br />

### *Makefile*
Para executar o programa, através do *Makefile*, execute:
```
make run INPUT_FILE [ARG1=file_path ARG2=file_path]
```

- **INPUT_FILE -** deve ser o arquivo de entrada do programa, contendo o código 
fonte a ser analisado, em linguagem *LC-2022-2*;
  - ***Obs:** Se nenhum argumento opcional for passado, será impresso, em tela, a saída do programa.*
- **ARG1 (Opcional) -** será o arquivo de saída, contendo os tokens;
  - ***Obs:** (caso **ARG2** não seja fornecido, o arquivo descrito em **ARG1** conterá, 
  também, a tabela de símbolos).*
- **ARG2 (Opcional) -** caso fornecido, será o arquivo contendo a tabela de símbolos.
<br />
<br />

### Executando da Fonte
Para executar o programa, através do código fonte, execute:
```
pip install -r requirements.txt
python src/main.py INPUT_FILE ARG1 ARG2
```

As mesmas regras se mantêm para **INPUT_FILE**, **ARG1** e **ARG2**.

[1]: https://www.linkedin.com/in/brendon-vicente-rocha/