from sly import Parser
from Lexer import CLexer

class CParser(Parser):
    tokens=CLexer.tokens
    literals=CLexer.literals
    @_('main_func')
    def program(self,p):
        return true
    @_('return_type identifier "(" ")" "{" statements "}"')
    def main_func(self,p):
        pass
    @_('INT')
    def return_type(self,p):
        return p.int
    @_('statement ";" statements')
    def statements(self,p):
        pass
    @_('statement ";"')
    def statements(self,p):
        pass
    @_('declaration_stmt')
    def statement(self,p):
        pass
    @_('assignment_stmt')
    def statement(self,p):
        pass
    @_('print_stmt')
    def statement(self,p):
        pass
    @_('type list_of_variables')
    def declaration_stmt(self,p):
        pass
    @_('identifier "," list_of_variables')
    def list_of_variables(self,p):
        pass
    @_('identifier')
    def list_of_variables(self,p):
        pass
    @_('identifier "=" identifier ";"')
    def assignment_stmt(self,p):
        pass
    @_('identifier "=" NUMBER ";" ')
    def assignment_stmt(self,p):
        pass
    @_('PRINT identifier ";" ')
    def print_stmt(self,p):
        pass
    @_('INT')
    def type(self,p):
        return int
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
        int a;
        a=30;
        print a;
    }'''
    res=parser.parse(lexer.tokenize(code))
    if res:
        print("valid")
    else:
        print("invalid")