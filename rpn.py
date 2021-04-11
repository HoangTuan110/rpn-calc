"""

    This is a simple RPN (Reverse Polish Notation) calculator written in Python.
    It may be quite slow, but I don't care lol.

"""

def calc(code):
    # Variables
    tokens      = code.split(" ")
    stack       = []
    ops         = "+-*/"
    result      = ""

    # Helper functions
    push        = lambda n:   stack.append(n)
    pop         = lambda:     stack.pop()
    is_number   = lambda ipt: ipt.isnumeric()
    is_hex      = lambda ipt: "x" in ipt
    is_binary   = lambda ipt: "b" in ipt

    # Main part
    for token in tokens:
        if is_number(token) or is_hex(token) or is_binary(token):
            push(eval(token))
            if len(result) == 0:
                result += f"{token}"
        # This is to avoid the case that user put extra spaces at the end
        # or the start of the input
        elif token == "":
            continue
        elif token in ops:
            op1, op2 = stack.pop(), stack.pop()
            # Since 'result' have the first value ('op1') already in them,
            # so we don't need to add it twice.
            result += f" {token} {op2}"
            push(eval(f"{op1} {token} {op2}"))
        else:
            print(f"Illegal character: {token}")
            break

    print(eval(result))

def repl():
    while True:
        calc(input(">> "))


repl()
