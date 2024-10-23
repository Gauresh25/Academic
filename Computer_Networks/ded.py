from typing import List
from decimal import Decimal, getcontext


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(index, path, value, last):
            if index == len(num):
                if abs(value - target) < Decimal('1e-10'):  # Use small threshold for floating-point comparison
                    result.append(path)
                return

            for i in range(index, len(num)):
                if i != index and num[index] == '0':
                    break

                current = int(num[index:i + 1])
                current_decimal = Decimal(current)

                if index == 0:
                    backtrack(i + 1, str(current), current_decimal, current_decimal)
                else:
                    backtrack(i + 1, path + "+" + str(current), value + current_decimal, current_decimal)
                    backtrack(i + 1, path + "-" + str(current), value - current_decimal, -current_decimal)
                    backtrack(i + 1, path + "*" + str(current), value - last + last * current_decimal,
                              last * current_decimal)
                    if current != 0:  # Avoid division by zero
                        backtrack(i + 1, path + "/" + str(current), value - last + last / current_decimal,
                                  last / current_decimal)

        getcontext().prec = 15  # Set precision for Decimal calculations
        result = []
        backtrack(0, "", Decimal(0), Decimal(0))
        return result


# Test cases
solution = Solution()

num = input();
target = int(input())

print("Expressions:")
soln = (solution.addOperators(num, target))
for i in soln:
    print(i)

# print(solution.addOperators("999999", 81))  # Output: ["9/9/9*9*9*9*9*9*9", "99/9*9-9/9/9/9/9"]
