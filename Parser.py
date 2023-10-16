from sly import Parser
from Lexer import CLexer
from Program import Program
from Function import Function
from Ast import AST,AssignAst, NameAst, NumberAst,PrintAst
from SymbolTable import SymbolTable,SymbolTableEntry
import main
gst=SymbolTable()
lexer=CLexer()
lineNo=lexer.lineno
class CParser(Parser):
    tokens=CLexer.tokens
    literals=CLexer.literals
    @_('main_func')
    def program(self,p):
        pr=Program()
        pr.addFunctionDetails(p[0].name,p[0])
        return pr
    @_('return_type identifier "(" ")" "{" statements "}"')
    def main_func(self,p):
        f=Function(p[0],p[1])
        f.setStatementsAstList(p.statements)
        f.setLocalSymbolTable(gst)
        return f
    @_('INT')
    def return_type(self,p):
        return 'int'
    @_('statement ";" statements')
    def statements(self,p):
        return [p[0]]+p[2]
    @_('statement ";"')
    def statements(self,p):
        return p[0]
    @_('declaration_stmt')
    def statement(self,p):
        return p[0]
    @_('assignment_stmt')
    def statement(self,p):
        return p[0]
    @_('print_stmt')
    def statement(self,p):
        return p[0]
    @_('type list_of_variables')
    def declaration_stmt(self,p):
        for name in p[1]:
            gst.addSymbol(SymbolTableEntry(name,p[0]))
    @_('identifier "," list_of_variables')
    def list_of_variables(self,p):
        return [p[0]]+p[2]
    @_('identifier')
    def list_of_variables(self,p):
        return [p[0]]
    @_('identifier "=" identifier')
    def assignment_stmt(self,p):
        l=NameAst(gst.nameInSymbolTable(p[0]))
        r=NameAst(gst.nameInSymbolTable(p[2]))
        asgn=AssignAst(l,r,lineNo)
        return [asgn]
    @_('identifier "=" constant')
    def assignment_stmt(self,p):
        l=NameAst(gst.nameInSymbolTable(p[0]))
        r=NumberAst(p[2])
        asgn=AssignAst(l,r,lineNo)
        return [asgn]
    @_('PRINT identifier')
    def print_stmt(self,p):
        i=gst.nameInSymbolTable(p[1])
        pri=PrintAst(i)
        return [pri]
    @_('INT')
    def type(self,p):
        return 'int'
    @_('ID')
    def identifier(self,p):
        return p[0]
    @_('NUMBER')
    def constant(self,p):
        return p[0]
if __name__=='__main__':
    lexer=CLexer()
    parser=CParser()
    code='''int main(){
        int a,b;
        a=30;
        b=a;
        c=20;
        print a;
        print b;
        print c;
    }'''
    res=parser.parse(lexer.tokenize(code))
    if res:
        print("valid")
        res.print()
    else:
        print("invalid")