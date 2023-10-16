from sly import Parser
from Lexer1 import CLexer
from SymbolTable1 import SymbolTableEntry,SymbolTable
from Ast1 import NameAst,NumberAst,AssignAst,PrintAst
from Program1 import Program
from Function1 import Function
gst=SymbolTable()
class CParser(Parser):
    tokens=CLexer.tokens
    literals=CLexer.literals
    @_('program')
    def s(self,p):
        return p[0]
    @_('return_type identifier "(" ")" "{" statements "}" ')
    def program(self,p):
        pr=Program()
        f=Function()
        f.setStatementsAstList(p.statements)
        f.setLocalSymbolTable(gst)
        pr.addFunctionDetails(p.identifier,f)
        return pr
    @_('INT')
    def return_type(self,p):
        return p[0]
    @_('statement ";" statements')
    def statements(self,p):
        return [p[0]]+p[2]
    @_('statement ";"')
    def statements(self,p):
        return [p[0]]
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
        # se=SymbolTableEntry(,p[0])
        # gst.addSymbol()
        for i in p[1]:
            se=SymbolTableEntry(i,p[0])
            gst.addSymbol(se)
    @_('identifier "," list_of_variables')
    def list_of_variables(self,p):
        return [p[0]]+p[2]
    @_('identifier')
    def list_of_variables(self,p):
        return [p[0]]
    @_('identifier "=" identifier')
    def assignment_stmt(self,p):
        la=NameAst(gst.nameInSymbolTable(p[0]))
        ra=NameAst(gst.nameInSymbolTable(p[2]))
        aa=AssignAst(la,ra)
        return aa
    @_('identifier "=" constant')
    def assignment_stmt(self,p):
        la=NameAst(gst.nameInSymbolTable(p.identifier))
        ra=NumberAst(p.constant)
        aa=AssignAst(la,ra)
        return aa
    @_('PRINT identifier')
    def print_stmt(self,p):
        pa=PrintAst(gst.nameInSymbolTable(p.identifier))
        return pa
    @_('INT')
    def type(self,p):
        return p[0]
    @_('ID')
    def identifier(self,p):
        return p[0]
    @_('NUMBER')
    def constant(self,p):
        return p[0]
lexer=CLexer()
parser=CParser()
code='''int main(){
int a,b,c;
a=30;
b=a;
c=b;
print a;
print b;
}'''
res=(parser.parse(lexer.tokenize(code)))
if res:
    print("valid code")
    res.print()
else:
    print("invalid code")