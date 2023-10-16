from enum import Enum
DataType = Enum('DataType',['INT','DOUBLE'])

class SymbolTableEntry:
	def __init__(self,name,datatype):
		self.name=name
        self.datatype=datatype
	def getSymbolName(self):
		return self.name
	def getDataType(self):
		return self.datatype
	def print(self):
		pass


class SymbolTable:
	def __init__(self):
		self.table = []
	def addSymbol(self,symbol):
		self.table.append(symbol)
	def nameInSymbolTable(self,name):
		for i in self.table:
            if i.getSymbolName()==self.name:
                return i
        return None
	def printSymbolTable(self):
		pass

