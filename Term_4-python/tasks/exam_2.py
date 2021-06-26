from collections import defaultdict

courses = [[1, 0], [2, 0], [3, 1], [3, 2]]
n = 4

def build_graph(courses):
    gr = {}
    for i in range(n):
        gr[i] = []
    for course in courses:
        gr[course[0]].append(course[1])
    return gr

graph = build_graph(courses)


def topologicalSortUtil(graph, v, visited, stack):

    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            topologicalSortUtil(i, visited, stack)
    stack.insert(0, v)



def topSort(graph, n):
    visited = [False] * n
    stack = []

    for i in range(n):
        if visited[i] == False:
            topologicalSortUtil(graph, i, visited, stack)
    stack.insert(0, i)
    return stack


ans = topSort(build_graph(courses), n)[1:]
for i in ans:
    print(i, end=' ')
print()
reversed = ans[::-1]

def gen(ls):
    for i in ls:
        yield i

for i in gen(reversed):
    print(i)

