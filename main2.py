import argparse
from Parser1 import CParser
from Lexer1 import CLexer
parser = argparse.ArgumentParser()

parser.usage = "tinyCC [options] file"

parser.add_argument('-tokens',action='store_true',help="Show tokens in file.toks (or out.toks)")
parser.add_argument('-parse',action='store_true',help="Stop processing with parsing")
parser.add_argument('-ast', action='store_true',help="Show abstract syntax trees in file.ast (or out.ast)")
parser.add_argument('-symtab',action='store_true',help="Show symbol table in file.sym (or out.sym)")
parser.add_argument('-compile',action='store_true',help="Compile the program and generate spim code in file.spim (or out.spim)")
parser.add_argument('file',help="TinyC Program")
args = parser.parse_args()
lexer=CLexer()
f=open(args.file)
code=f.read()
tokens=lexer.tokenize(code)

args.compile = True  #default value
if args.tokens:
	tokens_file_name = args.file +".toks"
	tokens_file = open(tokens_file_name,"w")
    # call tokenize and print tokens into tokens_file
if args.parse:
	# call parser, which should not create Program data structure
	args.ast = False
	args.compile = False
if args.ast:
	ast_file_name = args.file +".ast"
	ast_file = open(ast_file_name,"w")
	# call parser, creates Program object
	# call program.print(), which should print ast
if args.compile:
	target_code_file_name = args.file +".spim"
	target_code_file = open(target_code_file_name,"w")
    # call parser, creates Program object
    # call program.compile(), which should 

