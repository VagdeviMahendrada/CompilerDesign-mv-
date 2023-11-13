from sly import Lexer
class CLexer(Lexer):
    tokens={NUMBER,NEWLINE}
    literals={'+','-','*','/','{','}','(',')'}
    ignore=' \t'
    NUMBER=r'\d+'
    NEWLINE=r'\n'
    # ID=r'[a-zA-Z_][a-zA-Z0-9_]*'