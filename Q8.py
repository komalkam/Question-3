def reverse_string_using_stack(input_string):
    stack = []
    reversed_string = ""

    for char in input_string:
        stack.append(char)

   
    while len(stack) > 0:
        reversed_string += stack.pop()

    return reversed_string


if __name__ == "__main__":
    input_string = "Hello, World!"

    reversed_string = reverse_string_using_stack(input_string)
    print("Original String:", input_string)
    print("Reversed String:", reversed_string)
