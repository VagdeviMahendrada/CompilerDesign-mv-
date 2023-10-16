from SymbolTable import SymbolTable
class Function:
	def __init__(self, returnType, name):
		self.returnType = returnType
		self.name       = name
		self.statementsAstList = []
		self.localSymbolTable = SymbolTable()
	def setStatementsAstList(self, sastList):
		self.statementsAstList = sastList
	def getStatementsAstList(self):
		return self.statementsAstList
	def setLocalSymbolTable(self,localList):
		self.localSymbolTable = localList
	def getLocalSymbolTable(self):
		return self.localSymbolTable
	def print(self):
		print("	Procedure:",end="")
		print(self.name,end="")
		print(", ReturnType:",end="")
		print(self.returnType)
		for i in self.statementsAstList:
			i.print()