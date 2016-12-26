
operators_list = ['+','-','*','/']

class Operator:
	Plus, Minus, Mult, Div = range(4)


class NodeType:
	Leaf, NonLeaf = range(2)



class ExprNode:

	def __init__(self,type):

		self.type = type

		if type == NodeType.Leaf:
			self.val = None
		else:
			self.oper = None
			self.l = None
			self.r = None

	def getOperatorFromEnum(self,OperatorType):

		# if OperatorType == Operator.Plus:
		# 	return '+'
		# elif OperatorType == Operator.Minus:
		# 	return '-'
		# elif OperatorType == Operator.Mult:
		# 	return '*'
		# else:
		# 	return '/'
		return operators_list[OperatorType]


	def __repr__(self):

		retval = ''

		#print 'hello'

		if self.type == NodeType.Leaf:
			retval = self.val
			return retval

		if self.l != None:
			
			if self.l.type == NodeType.Leaf:
				retval = retval + str(self.l)
			else:
				retval = retval + '(' + str(self.l) + ')'

		retval = retval + self.getOperatorFromEnum(self.oper)

		if self.r != None:
			
			if self.r.type == NodeType.Leaf:
				retval = retval + str(self.r)
			else:
				retval = retval + '(' + str(self.r) + ')'

		return retval


	def compute(self,loper,roper,oper):
		if oper == Operator.Plus:
			return loper + roper
		elif oper == Operator.Minus:
			return loper - roper
		elif oper == Operator.Mult:
			return loper*roper
		else:
			return loper/roper


	def inverseComputeLeft(self,roper,oper,exprVal):
		if oper == Operator.Plus:
			return exprVal - roper
		elif oper == Operator.Minus:
			return exprVal + roper
		elif oper == Operator.Mult:
			return exprVal/roper
		else:
			return exprVal*roper



	def computeexpr(self):

		result = None

		if self.type == NodeType.Leaf:
			result = int(self.val)
			return result

		left_operand = None
		if self.l != None:
			left_operand = self.l.computeexpr()

		right_operand = None
		if self.r != None:
			right_operand = self.r.computeexpr()


		if self.l is None or self.r is None:
			print "failure"
			return 0

		return self.compute(left_operand,right_operand,self.oper)


	def inverseComputeRight(self,loper,oper,exprVal):
		if oper == Operator.Plus:
			return exprVal - loper
		elif oper == Operator.Minus:
			return loper - exprVal
		elif oper == Operator.Mult:
			return exprVal/loper
		else:
			return loper/exprVal

	def solveForVariable(self,exprVal,variable):

		if self.type == NodeType.Leaf and self.val == variable:
			return exprVal
			#This should only happen in case of if the last left leaf node is the variable to be computed

		if self.r.type == NodeType.NonLeaf:
			pass
			#Should not happen depending on the format of the expression
			#TODO

		if self.r.val != variable:

			new_expr_val = self.inverseComputeLeft(int(self.r.val),self.oper,exprVal)
			return self.l.solveForVariable(new_expr_val,variable)
			
		
		#print "Hello"
		left_operand = self.l.computeexpr() #There should ne no variabe in 

		#print "Hello " + str(left_operand) + " " + str(exprVal)
		right_operand = self.inverseComputeRight(left_operand,self.oper,exprVal)

		#print right_operand
		return right_operand


		






	__str__ = __repr__

 