def evaluate(str_in):
	tokens = str_in.split(" ")
	stack = []
	while len(tokens) > 0:
		item = tokens.pop(0)

		if item.isdigit():
			stack.append(int(item))

		elif item == "+":
			if len(stack) > 1:
				stack.append(stack.pop() + stack.pop())
			else:
				print ("ERROR: Invalid expression. Not enough input.")
				
		elif item == "-":
			if len(stack) > 1:
				tmp = stack.pop()
				stack.append(stack.pop() - tmp)
			else:
				print ("ERROR: Invalid expression. Not enough input.")
				
		elif item == "*":
			if len(stack) > 1:
				stack.append(stack.pop() * stack.pop())
			else:
				print ("ERROR: Invalid expression. Not enough input.")

		elif item == "/":
			if len(stack) > 1:
				tmp = stack.pop()
				stack.append(stack.pop() / tmp)
			else:
				print ("ERROR: Invalid expression. Not enough input.")

		elif item == "^":
			if len(stack) > 1:
				tmp = stack.pop()
				stack.append(pow(stack.pop(), tmp))
			else:
				print ("ERROR: Invalid Expression. Not enough input.")           

	return (stack.pop())

equation = "1 3 * 125 +"
print("Equation: '" + equation + "'")
print(evaluate(equation))