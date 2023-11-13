import sys
from abc import ABC,ABCMeta,abstractmethod

class AST(metaclass=ABCMeta):
	@abstractmethod
	def printEqTarget(self):
		pass

class CallAst(AST):
    def __init__(self,name,left,right):
        self.name=name
        self.left=left
        self.right=right

    def printEqTarget(self):
        print(self.name,end=" ")
        self.left.printEqTarget()
        self.right.printEqTarget()
        
class NumberAst(AST):
    def __init__(self, number):
        self.number = number

    def printEqTarget(self):
        print(self.number,end=" ")
