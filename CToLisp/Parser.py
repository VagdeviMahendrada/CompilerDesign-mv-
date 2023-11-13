from sly import Parser
from Lexer import CLexer
from Ast import *

class CParser(Parser):
    tokens=CLexer.tokens
    literals=CLexer.literals
    @_('E')
    def S(self,p):
        return p[0]
    @_('ADD "(" NUM "," E ")"')
    def E(self,p):
        n=NumberAst(p.NUM)
        c=CallAst(p[0],n,p.E)
        return c
    @_('SUB "(" NUM "," E ")"')
    def E(self,p):
        n=NumberAst(p.NUM)
        c=CallAst(p[0],n,p.E)
        return c
    @_('NUM')
    def E(self,p):
        n=NumberAst(p[0])
        return n
    def error(self,p):
        print("Invalid Expression")
lexer=CLexer()
parser=CParser()
str="add(2,sub(4, add(5,8)))"
res=parser.parse(lexer.tokenize(str))
if res:
    # print("valid expr")
    res.printEqTarget()