from sly import Lexer

class CLexer(Lexer):
    tokens={'ADD','SUB','NUM'}
    literals={'(',')',','}
    ignore=' \t'
    ADD=r'add'
    SUB=r'sub'
    NUM=r'\d+'
    def error(self,t):
        self.index+=1
