def generate_tac(expression):
    parts = expression.split("=")
    lhs = parts[0].strip()
    rhs = parts[1].strip()

    addition_parts = [part.strip() for part in rhs.split("+")]
    print(addition_parts)

    temp_counter = 1
    for i in range(len(addition_parts)):
        multiplication_parts = [part.strip() for part in addition_parts[i].split("*")]
        if len(multiplication_parts) > 1:
            left = multiplication_parts[0]
            right = multiplication_parts[1]
            temp_result = "t" + str(temp_counter)
            temp_counter += 1
            print(f"{temp_result} = {left} * {right}")
            addition_parts[i] = temp_result

    print(addition_parts)
    # Then handle all additions
    final_result = addition_parts[0]
    for i in range(1, len(addition_parts)):
        temp_add = addition_parts[i]
        temp_var = "t" + str(temp_counter)
        temp_counter += 1
        print(f"{temp_var} = {final_result} + {temp_add}")
        final_result = temp_var

    # Final assignment
    print(f"{lhs} = {final_result}")


if __name__ == "__main__":
    #input_expression = input("Enter an expression : ")
    generate_tac(" a = r + t * s + q")

#(e.g.,):