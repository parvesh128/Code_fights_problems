import re
from ExpressionTree import *

variable = None
#problem: "(((5 * x) / 4) + 13) - 15 = ?"
#answer: "  x     =20"
def substitute(problem,answer):

	answers = re.findall(r"[\w]+", answer)
	var = answers[0]
	val = answers[1]

	index = problem.index(var)

	new_problem = problem[0:index] + val + problem[index+1:]

	#print new_problem
	return new_problem

#((((((z / 1) + 3) / ?) + 3) / 2) * 10) - 7
def parseProblem(problem):
	global operators_list
	global variable
	root = ExprNode(NodeType.NonLeaf)
	#problem = problem.replace(' ','')
	eqidx = problem.index('=')
	orig_problem = problem

	problem = problem[:eqidx]
	problem_parts = re.findall(r"[\d]+|[^\s\\]", problem)

	#print problem_parts
	#return 

	temp = root
	stack = []
	for c in problem_parts:

		if c == '(':
			stack.append(temp)
			new_node = ExprNode(NodeType.NonLeaf)
			temp.l = new_node
			temp = new_node
		elif c == ')':
			temp = stack.pop()
		elif c.isalnum() or c == '?':
			#print c
			try:
				int(c)
			except ValueError:
				#It is variable
				variable = c

			if temp.type == NodeType.NonLeaf and temp.oper == None:
				temp.l = ExprNode(NodeType.Leaf)
				temp.l.val = c
			elif temp.type == NodeType.NonLeaf:
				temp.r = ExprNode(NodeType.Leaf)
				temp.r.val = c
		elif c in operators_list:
			if temp.type != NodeType.NonLeaf:
				print "Fatal error should not happen"
				break

			if c == '+':
				temp.oper = Operator.Plus
			elif c == '-':
				temp.oper = Operator.Minus
			elif c == '*':
				temp.oper = Operator.Mult
			elif c == '/':
				temp.oper = Operator.Div

	if len(stack) != 0:
		print "Fatal error should not happen"

	print root

	return root



def cleanup(string):

	retval = string.replace(' ','')

	return retval





def algebraHomework(problem, answer):

	#print problem
	problem = cleanup(problem)
	answer = cleanup(answer)
	global variable

	#print problem

	if '?' in answer:
		#Solve for variable
		root = parseProblem(problem)
		temp_problem_parts = problem.split('=')
		exprVal = int(temp_problem_parts[1])
		return root.solveForVariable(exprVal,variable)
	else:
		problem = substitute(problem,answer)
		root = parseProblem(problem)
		temp_problem_parts = problem.split('=')

		if temp_problem_parts[1] == '?':
			return root.computeexpr()
		else:
			#Solve for ?
			exprVal = int(temp_problem_parts[1])
			return root.solveForVariable(exprVal,variable)
		


if __name__ == '__main__':
	#DATA = "((((((z / 1) + 3) / ?) + 3) / 2) * 10) - 7"
	#print re.findall(r"[\w]+", DATA)
	#problem = '((((((z / 1) + 3) / ?) + 3) / 2) * 10) - 7'
	#problem = '((((((z / 1) + 3) / ?) + 3) / 2) * 10) -     7=33  '
	#answer = '     z=    7 '
	# parseProblem(problem)

	problem = '8 - q = 3'
	answer = 'q = ?'
	print algebraHomework(problem,answer)