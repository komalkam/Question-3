def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit(): 
            stack.append(int(token))
        else:  
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == "+":
                stack.append(operand1 + operand2)
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
            elif token == "/":
                stack.append(operand1 / operand2)

    return stack[0]  


if __name__ == "__main__":
    postfix_expression = "4 5 + 7 2 - *"

    result = evaluate_postfix(postfix_expression)
    print("Postfix Expression:", postfix_expression)
    print("Result:", result)
