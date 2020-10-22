
print("            ----- The Input Graph is -----")
print("                           A   ")
print("                        /    \\")
print("                       B       C")
print("                     /   \\   /  \\")
print("                    D     E  F    G")
print("                   /              \\")
print("                  H                I")

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": [],
    "F": [],
    "G": ["I"],
    "H": [],
    "I": []
}


visited = []
queue = []


def bfs(visited, graph, node, goal):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        if(s == goal):
            break

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


visited_dfs = set()


def dfs(visited_dfs, graph, node, goal):
    if node not in visited_dfs:
        print(node, end=" ")
        visited_dfs.add(node)
        for neighbour in graph[node]:
            dfs(visited_dfs, graph, neighbour, goal)
            if(goal in visited_dfs):
                return


g = input("Enter Goal Node for BFS : ")

bfs(visited, graph, "A", str(g).upper())
print()

g = input("Enter Goal Node for DFS : ")

dfs(visited_dfs, graph, "A", str(g).upper())
