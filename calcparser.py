from sly import Parser
from calclexer import CLexer
class CParser(Parser):
        tokens=CLexer.tokens
        literals=CLexer.literals
        precedence=(('left','+','-'),('left','*','/'))
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
        @_('INTEGER')
        def expr(self,p):
                return p[0]
lexer=CLexer()
parser=CParser()
expr1="2+3+5"
expr2="2-3-5"
expr3="2*3-5"
expr4="(2*3)/2"
expr='''2+3+4
5+6+6
56*34-(2-3)'''
parser.parse(lexer.tokenize(expr1))
parser.parse(lexer.tokenize(expr2))
parser.parse(lexer.tokenize(expr3))
parser.parse(lexer.tokenize(expr4))
parser.parse(lexer.tokenize(expr))
