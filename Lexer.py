from sly import Lexer
class CLexer(Lexer):
    tokens={'INT','PRINT','ID','NUMBER'}
    literals={',',';','{','}','(',')','='}
    ignore=' \n\t'
    INT=r'int'
    PRINT=r'print'
    ID=r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER=r'\d+'
    def __init__(self):
        self.lineno=1
    def newline(self,t):
        r'\n+'
        self.lineno+=len(t.value)
lexer=CLexer()
code='''int main(){
    int a;
    a=30;
    print a;
}'''
tokens=lexer.tokenize(code)
for toks in tokens:
    print(f"type={toks.type},value={toks.value}")