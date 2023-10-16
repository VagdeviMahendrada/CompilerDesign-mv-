from sly import Lexer
class CLexer(Lexer):
    tokens={INT,NUMBER,ID,PRINT}
    literals={';',',','=','(',')','{','}'}
    ignore=' \t\n'
    INT=r'int'
    PRINT=r'print'
    NUMBER=r'\d+'
    ID=r'[a-zA-Z_][a-zA-Z0-9_]*'
    