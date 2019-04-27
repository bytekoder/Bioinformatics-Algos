import os
from collections import defaultdict


def decode(conn):
    nn = int(conn.readline().strip())
    dd = list()
    for lin in conn:
        dd.append(list(map(int, lin.strip().split(' '))))
    return nn, dd


def calculateLimbLength(index):
    # return the limb length of the specified index [node] and the path where the limb connects
    curr_min = float('inf')
    bridge = 0, 0
    for i in range(index):
        for ii in range(i, index):
            curr = d[i][index] + d[index][ii] - d[i][ii]
            curr /= 2
            if curr < curr_min:
                curr_min = curr
                bridge = i, ii
    return int(curr_min), bridge


def path_between(i, j):
    poss_paths = [[(i, 0)]]
    while poss_paths:
        path = poss_paths.pop()
        node = path[-1][0]
        for next_node, dist in finalized_tree[node]:
            new_path = path[:]
            if next_node == j:
                new_path.append((j, dist))
                return new_path
            elif next_node < n:
                continue
            elif len(new_path) >= 2:
                if next_node != new_path[-2][0]:
                    new_path.append((next_node, dist))
                    poss_paths.append(new_path)
                    continue
            elif len(new_path) == 1:
                new_path.append((next_node, dist))
                poss_paths.append(new_path)
                continue


def adding_branch(index):
    # Build the tree
    global finalized_tree
    global int_node
    limb, bridge = calculateLimbLength(index)
    i, j = bridge
    path = path_between(i, j)
    distance = d[i][index] - limb
    start_node = i
    for node, dd in path:
        if dd == 0:
            continue
        if distance > dd:
            distance -= dd
            start_node = node
        elif distance == dd:
            finalized_tree[node].append((index, limb))
            finalized_tree[index].append((node, limb))
            break
        elif distance < dd:
            new_node = int_node
            int_node += 1
            finalized_tree[new_node].append((index, limb))
            finalized_tree[index].append((new_node, limb))
            finalized_tree[start_node].remove((node, dd))
            finalized_tree[node].remove((start_node, dd))
            finalized_tree[start_node].append((new_node, distance))
            finalized_tree[new_node].append((start_node, distance))
            finalized_tree[node].append((new_node, dd - distance))
            finalized_tree[new_node].append((node, dd - distance))
            break
    return None


def printTree(tree, conn):
    for key, value in tree.items():
        for next_node, dist in value:
            conn.write(str(key) + '->' + str(next_node) + ':' + str(dist) + '\n')
    return None


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        n, d = decode(f)
    int_node = n
    # NPE fix
    finalized_tree = defaultdict(list)
    finalized_tree[0].append((1, d[1][0]))
    finalized_tree[1].append((0, d[1][0]))
    for ind in range(2, n):
        adding_branch(ind)
    with open('tree_out.txt', 'w') as g:
        printTree(finalized_tree, g)
