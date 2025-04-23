matrix = [
   [0, 1, 4, 0, 0],  # A's connections
   [1, 0, 0, 1, 3],  # B's connections
   [4, 0, 0, 0, 2],  # C's connections
   [0, 1, 0, 0, 0],  # D's connections
   [0, 3, 2, 0, 0]   # E's connections
]
n=len(matrix)
rep={0:'a',1:'b',2:'c',3:'d',4:'e'}
graph = {'a':[],'b':[],'c':[],'d':[],'e':[]}
hue= {'a':7,'b':5,'c':3,'d':1,'e':0}
for i in range(n):
    for j in range(n):
       if matrix[i][j] !=0:
          graph[rep[i]].append((rep[j],matrix[i][j]))

print(graph)

openlist=[('a',hue['a'])]
goal = 'e'
closelist=[]

def minpop(openlist):
   min = openlist[0][1]
   minInd = 0

   for i in range(1,len(openlist)):
      if openlist[i][1]<min:
         min = openlist[i][1]
         minInd=i

   return openlist.pop(minInd)

while openlist:
   current,hval = minpop(openlist)

   if current== goal:
      print("reached")
      print(closelist)
      breakpoint()

   for neighbor in graph[current]:
      if neighbor not in closelist:
         print(neighbor[0])
         openlist.append((neighbor[0],hue[neighbor[0]]+neighbor[1]))

   closelist.append(current[0])