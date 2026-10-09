graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['','H'],
    'E': ['','I'],
    'F': [],
    'G': ['J','']
}
def dls(node, goal, depth):
    if node == goal:
        return True
    if depth == 0:
        return False
    for child in graph[node]:
        if dls(child, goal, depth - 1):
            return True
    return False
def iddfs(start, goal):
    depth = 0
    while True:
        if dls(start, goal, depth):
            print("Goal found at depth", depth)
            return
        depth += 1
start = input("Enter start node: ")
goal = input("Enter goal node: ")
iddfs(start, goal)
