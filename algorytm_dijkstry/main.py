import json
import numpy as np

json_file = open("input.json")
json_data = json.load(json_file)

number = len(json_data[0])

matrix = np.zeros((number, number))
for i in range(0, number):
    for j in range(0, number):
        matrix[i][j] = json_data[i][j]

neighbours_after = []
tmp = []
for i in range(0, number):
    tmp = []
    for j in range(0, number):
        if matrix[i, j] != 0:
            tmp.append(j)
    neighbours_after.append(tmp)

vertex_from = int(input('podaj wierzcholek z ktorego wychodzimy:'))

costs_matrix = np.zeros((3, number))
to_check = []
for i in range(0, number):
    to_check.append(i)
    costs_matrix[0, i] = i
    costs_matrix[1, i] = np.inf
    costs_matrix[2, i] = -1
costs_matrix[1, vertex_from] = 0

checked = []
for i in neighbours_after[vertex_from]:
    costs_matrix[1, i] = matrix[vertex_from, i]
    costs_matrix[2, i] = vertex_from
    for j in neighbours_after[i]:
        value = matrix[i, j] #cost of edge from i to j
        total_value = matrix[i, j] + costs_matrix[1, i]
        if total_value < costs_matrix[1, j]:
            costs_matrix[1, j] = total_value
            costs_matrix[2, j] = i
    checked.append(i)
    to_check.remove(i)
checked.append(vertex_from)
to_check.remove(vertex_from)

while len(to_check) != 0:
    smallest_value = costs_matrix[1, to_check[0]]
    chosen = to_check[0]
    for vertex in to_check:
        if costs_matrix[1, vertex] < smallest_value:
            smallest_value = costs_matrix[1, vertex]
            chosen = vertex
    i = chosen
    for j in neighbours_after[i]:
        value = matrix[i, j]  # value from i to j
        total_value = matrix[i, j] + costs_matrix[1, i]
        if total_value < costs_matrix[1, j]:
            costs_matrix[1, j] = total_value
            costs_matrix[2, j] = i
    checked.append(i)
    to_check.remove(i)

print('algorithm table:')
print(costs_matrix)
print('(-1 means that vertix does not have a predecessor - we cannot reach it)\n')

#wyświetlanie dróg do wszystkich wierzchołków
path = []
for vertex_to in costs_matrix[0]:
    vertex_to = int(vertex_to)
    prev = int(vertex_to)
    path.append(prev)
    while vertex_from not in path and costs_matrix[2, prev] != -1:
        path.append(int(costs_matrix[2, prev]))
        prev = int(costs_matrix[2, prev])
    if len(path) > 1:
        print('shortest path from vertex', vertex_from, 'to vertex', vertex_to, 'is:', ' -> '.join(str(i) for i in reversed(path)))
        print('cost of path:', int(costs_matrix[1, vertex_to]))
    else:
       print('path from vertex', vertex_from, 'to vertex', vertex_to, 'does not exists')
    path.clear()
    print('--------------------------------------------------------------------------------------------------')

