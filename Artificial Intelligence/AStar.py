matrix = [
   [0, 1, 4, 0, 0],  # A's connections
   [1, 0, 0, 1, 3],  # B's connections
   [4, 0, 0, 0, 2],  # C's connections
   [0, 1, 0, 0, 0],  # D's connections
   [0, 3, 2, 0, 0]   # E's connections
]
class Node:
    def __init__(self,name,dist,hue,parent=None):
        self.name = name
        self.dist = dist
        self.hue = hue
        self.func = dist+hue
        self.parent = parent

    def __lt__(self, other):
        return self.func<other.func

rep={0:'a',1:'b',2:'c',3:'d',4:'e'}
graph = {'a':[],'b':[],'c':[],'d':[],'e':[]}
hue= {'a':7,'b':5,'c':3,'d':1,'e':0}
n=len(matrix)
for i in range(n):
    for j in range(n):
       if matrix[i][j] !=0:
          graph[rep[i]].append((rep[j],matrix[i][j]))

print(graph)

openlist=[(Node('a',0,hue['a']))]
closelist = set()
goal ='e'
while openlist:
    openlist.sort()
    curr = openlist.pop(0)

    if curr.name == goal:
        print("done")
        print(curr.dist)
        while curr:
            print(curr.parent.name)
            curr = curr.parent
        exit()

    for neighbor,val in graph[curr.name]:
        if neighbor not in closelist:
            openlist.append(Node(neighbor,curr.dist+val,hue[neighbor],curr))

    #print(curr.name)