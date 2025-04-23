data = [
    't1=a+b',
    't2=5',
    't3=a+b',
    't4=5+t3',
    't5=a+b',
    't6=a+t2',
]


def tempF(code, removed):
    for k, v in removed.items():
        if k not in code:
            continue
        else:
            return [k, v]
    return []


def solve(data):
    temp = {}
    removed = {}
    for i in data:
        index = i.find('=')
        name = i[0:index].strip()
        code = i[index + 1:].strip()

        t = tempF(code, removed)
        if len(t) != 0:
            code = code.replace(t[0], t[1])

        if code not in temp.values():
            temp[name] = code
        else:
            key = ""
            for k, v in temp.items():
                if v == code:
                    key = k
                    break
            removed[name] = key
    return temp


ans = solve(data)
count = 0

# Create a copy of the dictionary to avoid modifying it during iteration
processed_ans = {}
for k, v in ans.items():
    processed_ans[k] = v

# Print the optimized expressions
for k, v in ans.items():
    print(f't{count + 1}=', end='')
    print(v)

    # Update references in remaining expressions
    for k1, v1 in processed_ans.items():
        processed_ans[k1] = processed_ans[k1].replace(k, f't{count + 1}')

    count += 1
