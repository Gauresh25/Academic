import re
import fileinput

file1 = 'input_file.txt'
file2 = 'output.txt'
f = open(file2, 'w+')


def transform(str1: str):
    keywords = ['if', 'else', 'for', 'int', 'float', 'double']
    operators = ['+', '-', '*', '/', "^", "=", '%']
    seperator = [':', ';']

    str2 = re.findall(r'\w+|[^\s\w]', str1)
    for i in str2:
        if i in keywords:
            print(f'{i} is a Keyword')
            f.write(f'{i} is a Keyword\n')
        elif i in operators:
            print(f'{i} is a Operator')
            f.write(f'{i} is a Operator\n')
        elif i in seperator:
            print(f'{i} is a seperator')
            f.write(f'{i} is a Seperator\n')
        elif i.isdigit():
            print(f'{i} is a constant')
            f.write(f'{i} is a constant\n')
        else:
            print(f'{i} is a identifier')
            f.write(f'{i} is a identifier\n')




for i in fileinput.input(files = file1):
    str1 = "".join(i)


transform(str1)