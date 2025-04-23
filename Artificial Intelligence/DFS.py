from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

def DFS(start,goal):
    vis = set()
    stack = [(start,[start],0)]

    while stack:
        print(stack)
        curr,path,cost = stack.pop()
        print(curr)

        if curr == goal :
            print("goal path" )
            print(path)

        vis.add(curr)

        for neighbor in reversed(graph[curr]):
            if neighbor not in vis:
                stack.append((neighbor,path+[neighbor],cost +1))

def DLS(start,goal,limit):
    vis = set()
    stack = [(start,[start],0)]

    while stack:
        print(stack)
        curr,path,cost = stack.pop()
        print(curr)

        if curr == goal :
            print("goal path" )
            print(path)
            exit()

        vis.add(curr)
        if cost >= limit:
            print("limit reached abandoning path ",path)
            continue



        for neighbor in reversed(graph[curr]):
            if neighbor not in vis:
                stack.append((neighbor,path+[neighbor],cost +1))

def DFID(start,goal):
    iter = 1
    for i in range(len(graph)):
        print("for depth ",iter)
        DLS(start,goal,iter)
        iter = iter +1


DFID('A','G')