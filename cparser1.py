from sly import Parser
from clexer1 import CLexer
class CParser(Parser):
    tokens=CLexer.tokens
    literals=CLexer.literals
    precedence=(('left','-','+'),('left','*','/'))
    @_('L NEWLINE expr')
    def L(self,p):
        print(p[2])
    @_('expr')
    def L(self,p):
        print(p[0])
    @_('expr "+" expr')
    def expr(self,p):
        return p[0]+p[2]
    @_('expr "-" expr')
    def expr(self,p):
        return p[0]-p[2]
    @_('expr "*" expr')
    def expr(self,p):
        return p[0]*p[2]
    @_('expr "/" expr')
    def expr(self,p):
        return p[0]/p[2]
    @_('"(" expr ")"')
    def expr(self,p):
        return p[1]
    @_('NUMBER')
    def expr(self,p):
        return int(p[0])
f=open("calip")
ip=f.read()
lexer=CLexer()
parser=CParser()
parser.parse(lexer.tokenize(ip))    