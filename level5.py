#!/usr/bin/python
import level2 as l2 

def problem(mn = [32, 32], fplot = 1): 
    "Returns the map of the problem." 
    m = mn[0]
    n = mn[1]

    B = [[8,0], [8,1], [8,2], [8,3], [8,4], [8,5], [8,6], [8,7], 
         [9,7], [9,8], [10, 8], [10, 9], [11, 9], [12, 9], [13, 9], 
         [14, 9], [15, 9], [16, 9], [17, 9], [18, 9], [19, 9], [19, 10], 
         [19, 11], [19, 12], [19, 13], [19, 14], [18, 14], [17, 14], 
         [16, 14], [15, 14], [15, 15], [15, 16], [15, 17], [15, 18], 
         [16, 18], [17, 18], [17, 19], [17, 20], [11, 21], [12, 21], 
         [13, 21], [11, 22], [11, 23], [11, 24], [11, 25], [11, 26], 
         [11, 27], [28, 17], [29, 17], [30, 17], [31, 17], [28, 18], 
         [24, 19], [25, 19], [26, 19], [27, 19], [28, 19], [24, 20], 
         [24, 21], [25, 21], [25, 22], [25, 23], [25, 24], [11, 21], 
         [12, 21], [13, 21], [11, 22], [11, 23], [11, 24], [11, 25], 
         [11, 26], [11, 27]] 
    L = [[12, 0], [13, 0], [14, 0], [12, 1], [13, 1], [14, 1], 
         [12, 2], [13, 2], [14, 2], [18, 2], [19, 2], [20, 2], 
         [12, 3], [13, 3], [14, 3], [17, 3], [18, 3], [19, 3], 
         [12, 4], [13, 4], [14, 4], [15, 4], [16, 4], [17, 4], 
         [18, 4], [19, 4], [12, 5], [13, 5], [14, 5], [15, 5], 
         [16, 5], [17, 5]] 
    R = [[23, 3], [24, 3], [23, 4], [24, 4], [21, 6], [22, 6], [21, 7],
         [22, 7], [22, 13], [23, 13], [22, 14], [23, 14], [3, 9], [4, 9], 
         [3, 10], [4, 10], [5, 22], [6, 22], [5, 23], [6, 23], [17, 24],
         [18, 24], [17, 25], [18, 25], [17, 24], [18, 24], [17, 25], 
         [18, 25], [22, 26], [23, 26], [22, 27], [23, 27]] 
    T = [[26, 11], [27, 23]] 
    W = [[8, 8], [8, 9], [9, 9], [8, 10], [9, 10], [8, 11], [9, 11], 
         [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], 
         [3, 13], [4, 13], [5, 13], [6, 13], [7, 13], [8, 13], [9, 13], 
         [3, 14], [4, 14], [3, 15], [4, 15], [0, 16], [1, 16], [2, 16], 
         [3, 16], [3, 17], [4, 17], [5, 17], [6, 17], [7, 17], [8, 17], 
         [9, 17], [3, 18], [4, 18], [5, 18], [6, 18], [7, 18], [8, 18],
         [9, 18], [3, 19], [4, 19], [5, 19], [6, 19], [7, 19], [8, 19],
         [9, 19], [3, 20], [4, 20], [5, 20], [6, 20], [7, 20], [8, 20],
         [9, 20], [25, 14], [26, 14], [27, 14], [28, 14], [29, 14], 
         [30, 14], [31, 14], [25, 15], [19, 16], [20, 16], [21, 16], 
         [22, 16], [23, 16], [24, 16], [25, 16], [18, 19], [19, 19],
         [20, 19], [21, 19], [22, 19], [23, 19], [18, 20], [19, 20],
         [20, 20], [21, 20], [22, 20], [23, 20]] 
    
    S = dict() 
    for s in B: 
        S[tuple(s)] = "B" 
    for s in L: 
        S[tuple(s)] = "L" 
    for s in R: 
        S[tuple(s)] = "R" 
    for s in T: 
        S[tuple(s)] = "T" 
    for s in W: 
        S[tuple(s)] = "W"

    if fplot > 0: 
        for j in xrange(m):
            line = [] 
            for i in xrange(n): 
                if S.has_key((i, j)): 
                    line.append(S.get((i, j))) 
                else: 
                    line.append(".") 
            print("    " + " ".join(e0 for e0 in line))

    return S 

def isValidMove(p0, p1, mn, S):
    "Check validity of a move."
    # Move must start at a valid position. 
    # Move is valid if the resulting location is in bounds, not blocked
    # by barriers (B) and not end up on a rock (R) or barrier. 

    # Check if starts and ends on a valid position 
    if isValidPos(p0, mn, S) <= 0: 
        return -1 
    if isValidPos(p1, mn, S) <= 0: 
        return -2
    if p0 == p1: 
        return -3

    d = [p1[0] - p0[0], p1[1] - p0[1]]
    # Check if teleported
    if S.get(tuple(p1)) == "T":
        # Cannot start and end on teleports  
        if S.get(tuple(p0)) == "T": 
            return -11 
        otherT = [list(k) for k, v in S.items() if v == "T"]
        otherT.remove(p1)
        for p in otherT:
            d = [p[0] - p0[0], p[1] - p0[1]] 
            if {abs(d[0]), abs(d[1])} == {1, 2}: 
                break 
            return -12

    # Check if a valid knight move 
    elif {abs(d[0]), abs(d[1])} != {1, 2}:
        print(d) 
        return -4


    # Check if blocked by barriers 
    if abs(d[0]) == 2: 
        dx = [d[0] / abs(d[0]) for el in xrange(2)]
        dy = [0, d[1] / abs(d[1])] 
    else: 
        dx = [0, d[0] / abs(d[0])] 
        dy = [d[1] / abs(d[1]) for el in xrange(2)] 

    b0 = (p0[0] + dx[0], p0[1] + dy[0]) 
    b1 = (p0[0] + dx[1], p0[1] + dy[1]) 
    b0 = S[b0] if b0 in S else None 
    b1 = S[b1] if b1 in S else None 
    if b0 == "B": 
        if b1 == "B": 
            return -23

    return 1 

def isInBounds(p, mn): 
    "Returns 1 if p is in bounds on an m X n grid." 
    xmax = mn[1] - 1
    ymax = mn[0] - 1  
    xmin = 0 
    ymin = 0

    if p[0] > xmax: 
        return -1 
    elif p[0] < xmin: 
        return -1 
    elif p[1] > ymax: 
        return -1 
    elif p[1] < ymin: 
        return -1
    else: 
        return 1 

def isValidPos(p, mn, S): 
    "Returns 1 if p is a valid coordinate." 
    # Check if in bounds
    if isInBounds(p, mn) <= 0: 
        return -1

    # Check if on a rock 
    try: 
        if S[tuple(p)] == "R": 
            return -21
    except KeyError: 
        pass 
    
    # Check if on a barrier
    try: 
        if S[tuple(p)] == "B":
            return -22
    except KeyError: 
        pass

    return 1


def isValidPos2(p, mn, S): 
    "Returns 1 if p is a valid coordinate."
    # Check if in bounds
    if isInBounds(p, mn) <= 0: 
        return -1

    pt = tuple(p)
    pt = S[pt] if pt in S else None
    # Check if on a rock 
    if pt == "R": 
        return -21 

    # Check if on a barrier
    if pt == "B": 
        return -22 

    return 1

def move(pos0, cmd): 
    "Returns the new position based on cmd." 
    u = [[1, 2],[2, 1],[2, -1],[1, -2],[-1, -2],[-2, -1],[-2, 1],[-1, 2]] 
    x = pos0[0] + u[cmd][0]
    y = pos0[1] + u[cmd][1]

    return [x, y]  

def allValidMoves(pos0, mn, S):
    "Return all valid positions after 1 step, assuming valid start point." 
    # This function does not check the validity of the starting position.
    moves = [] 
    otherT = []

    # Check if out of bounds, landing on barrier or rock 
    for cmd in xrange(0, 8):
        p = move(pos0, cmd) 
        if isValidPos2(p, mn, S) > 0:
            moves.append(p) 

    # Check not blocked by barrier 
    remove = list()
    p0 = pos0 
    for mv in moves:
        p1 = mv 
        d = [p1[0] - p0[0], p1[1] - p0[1]] 
        if abs(d[0]) == 2: 
            dx = [d[0] / abs(d[0]) for el in xrange(2)]
            dy = [0, d[1] / abs(d[1])] 
        else: 
            dx = [0, d[0] / abs(d[0])] 
            dy = [d[1] / abs(d[1]) for el in xrange(2)] 

        b0 = (p0[0] + dx[0], p0[1] + dy[0]) 
        b1 = (p0[0] + dx[1], p0[1] + dy[1]) 
        b0 = S[b0] if b0 in S else None 
        b1 = S[b1] if b1 in S else None 
        if b0 == "B": 
            if b1 == "B": 
                remove.append(mv)
        
    for e0 in remove: 
        moves.remove(e0)

    # Check if lands on a teleport
    for mv in moves:
        if S.get(tuple(mv)) == "T":
            otherT = [list(k) for k, v in S.items() if v == "T"]
            otherT.remove(mv)
            currentT = mv
    
    if len(otherT) >= 1: 
        if len(otherT) > 1: 
            print("Teleport destination not uniquely defined.")
            print("Can only have two teleports on map.") 
        moves.remove(currentT) 
        moves.append(otherT[0])

    return moves 

def isValidSequence(seq, mn, S, fplot = 0):
    "Check the validity of the sequence of moves, also plots the moves." 
    
    # Check for repeated position
    for p in seq: 
        if seq.count(p) > 1: 
            return -1 

    p0 = seq[0] 
    for p in seq[1:]: 
        if isValidMove(p0, p, mn, S) > 0:
            p0 = p 
        else: 
            return 0 
    
    if 2 >= fplot >= 1: 
        count = 1
        s1 = 79 * "." 
        s2 = "----Initial board---- " 
        print(s1) 
        print(s2)
        e = seq[-1] 
        s = seq[0] 
        plotState(s = s, e = e, mn = mn) 
        for p in seq[1:]: 
            s2 = "Move " + repr(count) 
            count += 1 
            print(s1) 
            print(s2) 
            plotState(p, s, e, mn) 
        print(s1) 
    if fplot >= 2:
        [m, n] = mn 
        print("----All moves----") 
        print("")
        print("    " + " ".join(str(n % 10) for n in range(n)))
        print("") 
        for j in xrange(m): 
            line = [] 
            for i in xrange(n):
                symbol = "." 
                if S.has_key((i,j)): 
                    symbol = S.get((i, j))
                if seq.count([i, j]) > 0: 
                    symbol = "K" 
                line.append(symbol) 
            print(repr(j).rjust(2) + "  " + " ".join(e0 for e0 in line)) 

    return 1 

def plotState(k = ['', ''] , s = ['', ''], e = ['', ''], mn = [8, 8]): 
    "Print the board state to the terminal."
    print("") 
    for m in xrange(mn[0]): 
        row = ""  
        for n in xrange(mn[1]):
            c = ". " 
            if n == e[0] and m == e[1]: 
                c = "E "  
            if n == s[0] and m == s[1]:
                c = "S "
            if n == k[0] and m == k[1]: 
                c = "K "    
            row = row + c  
        print("    " + "".join(r for r in row))  
    print("")

def stepCost(p, S): 
    "Return the step cost based on position p and problem description S."
    pt = tuple(p) 
    pt = S[pt] if pt in S else None
    if pt == "W": 
        c = 2 
    elif pt == "T": 
        c = 1 
    elif pt == "L": 
        c = 5
    elif pt == "R": 
        raise Exception("Step cost undefined for Rock square.") 
    elif pt == "B": 
        raise Exception("Step cost undefined for Barrier square.") 
    else: 
        c = 1 

    return c 
    

def findGoal2(s, e, mn, S, searchtype = "BFS", max_depthlimit = 1000):
    "Returns a sequence of moves from s to e." 
    
    from collections import OrderedDict 
    #from sys import maxsize 

    # Check inputs 
    if isValidPos(s, mn, S) <= 0: 
        return -3 
    if isValidPos(e, mn, S) <= 0: 
        return -4  

    #max_depthlimit = 100000
    #max_depthlimit = 10000 

    max_goalcost = 0 

    if searchtype == "IDDFS": 
        min_depthlimit = 1 
        lasttype = True
    elif searchtype == "DFS": 
        min_depthlimit = max_depthlimit - 1 
        lasttype = True 
    else:   #"BFS" 
        min_depthlimit = max_depthlimit - 1 
        lasttype = False 
    
    p = s
    parent = []
    pathcost = 0
    depth = 0

    rootnode = (tuple(p), [parent, pathcost, depth]) 

    for depthlimit in xrange(min_depthlimit, max_depthlimit):
        depth = 0 
        visited = dict() 
        q = OrderedDict() 
        q.update([rootnode]) 
        while depth <= depthlimit + 1:
            if len(q) == 0:
                print("Empty queue.") 
                break 
            node = q.popitem(last = lasttype) 
            depth = node[1][2]
            cur_pathcost = node[1][1] 

            # check if path contains repeated nodes
            if node[1][0] == []: 
                repeated = False 
            else: 
                int_seq = findSolution(s, node[1][0], visited) 
                int_seq.append(list(node[0])) 
                for e0 in int_seq: 
                    if int_seq.count(e0) > 1: 
                        repeated = True 
                    else:
                        repeated = False 

            # Update path cost to node 
            if not repeated: 
                old_pathcost = visited.get(node[0], [-1, -1, -1])[1]
                if old_pathcost < cur_pathcost: 
                    visited.update([node]) 
            else: 
                continue 

            if list(node[0]) == e: 
                print("A solution has been found.") 
                if cur_pathcost > max_goalcost: 
                    max_goalcost = cur_pathcost 
                    seq = list(int_seq) 
                continue 
            
            # Expand node 
            parent = list(node[0]) 
            depth += 1 
            moves = allValidMoves(parent, mn, S)
            try: 
                moves.remove(visited[tuple(parent)][0])
            except ValueError: 
                pass 
            
            for move in moves: 
                pathcost = stepCost(move, S) + cur_pathcost 

                if q.has_key(tuple(move)): 
                    if pathcost < q[tuple(move)][1]: 
                        continue 
                q.update([(tuple(move), 
                        [parent, pathcost, depth])])
        else: 
            print("Depth limit reached.") 

    else:
        print("Max depth limit reached.") 
        
    return seq 

def findSolution(s, e, nodes):
    "Used by findGoal2() to look up the moves from s to e." 
    sequence = [] 
    if e == []: 
        return sequence 
    
    k = e 
    sequence.append(k) 
    while k != s: 
        k = nodes.get(tuple(k))[0] 
        sequence.append(k) 

    sequence.reverse() 
    
    return sequence

def findSequenceCost(sequence, mn, S):
    "Returns the cost of a sequence of moves." 
    cost = 0 
    if isValidSequence(sequence, mn, S) > 0: 
        for p in sequence[1:]: 
            cost += stepCost(p, S) 
    else: 
        raise Exception("Invalid sequence.") 

    return cost

def test(s, e, mn, S, searchtype, max_depthlimit = 500000): 
    import time 
    t0 = time.time() 
    seq = findGoal2(s, e, mn, S, searchtype, max_depthlimit) 
    et = time.time() - t0

    if isinstance(seq, int): 
        print("Exit code: %s" %seq) 
    else:
        v = isValidSequence(seq, mn, S, 3) 
        print("Sequence: %s" %seq)
        if v > 0: 
            print("Sequence is valid.") 
            print("Cost: %s" %findSequenceCost(seq, mn, S)) 
    print("Elapsed time: %s" %et) 

    return seq

# ------------------------------------------- # 
print("") 
S = problem() 
print("Demonstrate level 5 on a smaller grid.") 
test([1, 1], [3, 3], [8, 8], S, "DFS") 


