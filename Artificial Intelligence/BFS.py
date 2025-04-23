from collections import deque
graph = {
    'A': [['B', 1], ['C', 3]],
    'B': [['A', 1], ['D', 2]],
    'C': [['A', 3], ['D', 1]],
    'D': [['B', 2], ['C', 1], ['E', 2]],
    'E': [['D', 2], ['F', 1], ['D', 1]],
    'F': [['E', 1]]
}

vis = set()
queue = []
queue.append(('A',['A'],0))
goal ='F'

def printer(queue):
    print("node | path | cost")
    for i in queue:
        print(i[0],i[1],i[2],sep=" | ")

    print("")

def minpop(queue):

    mincost = queue[0][2]
    minind=0

    for i in range(1,len(queue)):
        if queue[i][2]<mincost:
            mincost = queue[i][2]
            minind=i

    return queue.pop(minind)


def UCS():
    vis.clear()
    while queue:
        printer(queue)
        curr, path, cost = minpop(queue)

        if curr == goal:
            print("exit at ", path, cost)

        for neighbor in graph[curr]:
            if neighbor[0] not in vis:
                queue.append((neighbor[0], path + [neighbor[0]], cost + neighbor[1]))
                vis.add(neighbor[0])

def BFS():
    while queue:
        printer(queue)
        curr,path,cost = queue.pop(0)

        if curr == goal:
            print("exit at ",path,cost)



        for neighbor in graph[curr]:
            if neighbor[0] not in vis:
                queue.append((neighbor[0],path + [neighbor[0]],cost +neighbor[1]))
                vis.add(neighbor[0])

UCS()
