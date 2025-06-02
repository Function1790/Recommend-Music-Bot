data = "[a;({a;})]"

bra = "[{("
ket = {
    "]" : "[",
    "}" : "{",
    ")" : "("
}

code = []
stack = []
stack_type = []
current = []
statement = ''

cursor = 0

for i in data:
    if i in bra:
        stack_type.append(i)
        stack.append([])
    elif i in ket:
        if ket[i]==stack_type[len(stack)-1]:
            stack_type.pop()
            code.append(stack.pop())
        else:
            print("Err")
            break
    elif i==';':
        if len(stack) == 0:
            code.append(statement)
        else:
            stack[len(stack)-1].append(statement)
        statement = ''
    else:
        statement += i
    print('code: ', code, '\tstack: ', stack)