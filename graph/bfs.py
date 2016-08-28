from collections import deque

def bfs(start, goal, successors):
    """Perform breadth-first search on a directed graph.
    
    start should be the starting node, and goal is the node to seek.
    
    successors should be a function which takes as input a node n, and
    returns a list of nodes m such that there is a directed edge n -> m.
    
    If there is a path from start to goal, returns a list of nodes giving
    the path, starting with start and ending with goal.  If there is no
    path, returns None.
    """

    # pred is a dict tracking nodes we have visited in our search.
    # Entries of the form n : k where n is a node we have visited,
    # and k is the predecessor of n which we visited previously
    # (so that k -> n).

    pred = {}

    # todo is a queue containing nodes waiting to be visited.
    # We will insert on the left and pop on the right.
    # Put in the start node to get started
    
    todo = deque([start])

    while todo:
        n = todo.pop()
        s = successors(n)
        for m in s:
            if m == goal:
                # Create the list of nodes in the path.
                # Might as well use deque to create it in the right
                # order.
                path = deque([n, m])
                k = n
                while k != start:
                    k = pred[k]
                    path.appendleft(k)
                return list(path)
            elif m in pred:
                pass # Now don't start that again
            else:
                pred[m] = n
                todo.appendleft(m)
    return None
