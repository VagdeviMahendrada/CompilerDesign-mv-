from sly import Lexer
class CLexer(Lexer):
    tokens={'INTEGER','NEWLINE'}
    literals={'=','-',"(",")","*",'/','+'}
    INTEGER=r'\d+'
    NEWLINE=r'\n'
    def INTEGER(self,t):
        t.value=int(t.value)
        return t
    