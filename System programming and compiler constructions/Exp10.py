def main():
    n = int(input("Enter the number of expressions: "))
    expressions = {}
    expr_registers = {}
    codeGen = []
    count = 0

    opcodes = {
        "+": "ADD",
        "-": "SUB",
        "*": "MUL",
        "/": "DIV"
    }

    for i in range(n):
        exp = input(f"Enter TAC expression {i + 1} (e.g., t1 = a + b): ").strip()
        lhs, rhs = exp.split('=')
        lhs = lhs.strip()
        rhs = rhs.strip()
        tokens = rhs.split()

        if len(tokens) != 3:
            print(f"Invalid format in expression: {exp}")
            continue

        op1, op, op2 = tokens
        expressions[lhs] = rhs

        if expr_registers.get(op1) is None and expr_registers.get(op2) is None:
            reg = f"R{count}"
            expr_registers[lhs] = reg
            code = f"MOV {op1}, {reg}\n{opcodes[op]} {op2}, {reg}"
            count += 1
        elif expr_registers.get(op1) is not None and expr_registers.get(op2) is None:
            reg = expr_registers[op1]
            expr_registers[lhs] = reg
            code = f"{opcodes[op]} {op2}, {reg}"
        elif expr_registers.get(op1) is None and expr_registers.get(op2) is not None:
            reg = expr_registers[op2]
            expr_registers[lhs] = reg
            code = f"MOV {op1}, {reg}\n{opcodes[op]} {op2}, {reg}"
        else:
            reg = expr_registers[op1]
            expr_registers[lhs] = reg
            code = f"{opcodes[op]} {expr_registers[op2]}, {reg}"

        codeGen.append(f"# {exp}\n{code}")

    print("--" * 10)
    print("Generated Code is: ")
    print("--" * 10)

    for code in codeGen:
        print(code)
        print()


if __name__ == "__main__":
    main()