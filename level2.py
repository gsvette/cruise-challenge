#!/usr/bin/python


def getDistance(p1, p2): 
    "Return the Manhattan distance between p1 and p2." 
    d = 0; 
    for e1, e2 in zip(p1, p2):
        d += abs(e2 - e1) 
    return d

def getVector(p1, p2): 
    "Return the vector from p1 to p2." 
    v = [e2 - e1 for e1, e2 in zip(p1, p2)] 
    return v  

def findGoal(s, e, mn):
    "Return a sequence of moves from start s to end e on an m X n grid." 
    # Check inputs 
    if isValidPos(s, mn) <= 0: 
        return -3 
    if isValidPos(e, mn) <= 0: 
        return -4  

    if min(mn) < 4: 
        maxcount = 100
    else: 
        maxcount = 500000

    p = s
    q = [[s, list()]]
    nodelist = dict([(tuple(p), list())]) 
    count = 0
    while p != e:
        count += 1 
        if len(q) == 0: 
            return -1
        elif count > maxcount: 
            return -2 
        node = q.pop(0)
        nodelist.setdefault(tuple(node[0]), node[1])
        if node[0] == e: 
            return findSolution(s, e, nodelist) 
        
        moves = allValidMoves(node[0], mn)
        #try:
        #    #moves.remove(node[1])
        #except ValueError: 
        #    pass 
        
        for k in nodelist.iterkeys(): 
            try:  
                moves.remove(list(k))
            except ValueError:
                pass 

        q.extend(zip(moves, [node[0] for el in xrange(len(moves))])) 

def findSolution(s, e, nodes):
    "Returns the sequence of moves from s to e." 
    k = e 
    sequence = []
    sequence.append(k)  
    while k != s: 
        k = nodes.get(tuple(k))
        sequence.append(k) 
    sequence.reverse() 
    return sequence 

def move(pos0, cmd): 
    "The position (x, y) is updated based on input u(cmd)." 
    u = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]] 
    pos1 = [0,0] 
    x = pos0[0] + u[cmd][0]
    y = pos0[1] + u[cmd][1]
    return [x, y]  

def allValidMoves(pos0, mn): 
    "All valid subsequent positions." 
    moves = [] 
    for cmd in xrange(0, 8): 
        p = move(pos0, cmd) 
        if isValidPos(p, mn) > 0: 
            moves.append(p) 
    return moves 

def isValidPos(pos, mn): 
    "Returns 1 if pos is within bounds." 
    xmin = 0; 
    ymin = 0;
    xmax = mn[1]; 
    ymax = mn[0]; 
    if pos[0] < xmin: 
        return 0 
    elif pos[0] >= xmax: 
        return 0 
    elif pos[1] < ymin: 
        return 0 
    elif pos[1] >= ymax: 
        return 0 
    else: 
        return 1


def isValidMove(pos0, pos1, mn):
    "Check validity of a move." 
    if isValidPos(pos0, mn) <= 0: 
        return -1 
    if isValidPos(pos1, mn) <= 0: 
        return -2 

    for cmd in xrange(0,8):
        pos = move(pos0, cmd)
        if pos1[0] == pos[0] and pos1[1] == pos[1]:
            return 1 
    return 0 

def isValidSequence(seq_x, seq_y, mn = [8,8], fplot = 0): 
    "Return 1 if sequence is valid, 0 otherwise."
    seq = zip(seq_x, seq_y)
    p0 = seq[0]

    for p in seq[1:]:
        if isValidMove(p0, p, mn) > 0: 
            p0 = p 
        else: 
            return 0
    if fplot: 
        n = 1
        s1 = 79*"." 
        s2 = "Initial board"
        print(s1) 
        print(s2) 
        e = seq[-1]
        s = seq[0] 
        plotState(s = s, e = e, mn = mn)
        for p in seq[1:]:
            s2 = "Move " + repr(n)
            n += 1
            print(s1) 
            print(s2)
            plotState(p, s, e, mn)
        print(s1) 
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

def test(mn):
    import time 
    t0 = time.time() 
    count1 = 0
    count2 = 0
    count3 = 0
    for i in xrange(0, mn[1]): 
        for j in xrange(0, mn[0]): 
            for k in xrange(0, mn[1]): 
                for l in xrange(0, mn[0]):
                    if [i, j] != [k, l]: 
                        #print(i,j,k,l,count)
                        count1 += 1
                        seq = findGoal([i, j], [k, l], mn) 
                        # print(seq)
                        if seq < 0:
                            count2 += 1 
                            print([i,j],[k,l],count2) 
                            print("No solution found,", seq) 
                        else:
                            count3 += 1
                            x = [e0 for e0, e1 in seq] 
                            y = [e1 for e0, e1 in seq] 
                            if isValidSequence(x, y, mn, 0):
                                print([i,j],[k,l],count3) 
                                print("Solution is valid.")
    print("No solution found in ", count2, " cases.") 

    print("===============================================") 
    mn = [8, 8] 
    seq = findGoal([0, 0], [0, 3], mn) 
    print(seq)
    if seq == -1: 
        seq_x = [e1 for e1, e2 in seq] 
        seq_y = [e2 for e1, e2 in seq]
        print(isValidSequence(seq_x, seq_y, mn, 0)) 
    print("Elapsed time: %s" %(time.time() - t0))

def test2(s, e, mn):
    import time 
    t0 = time.time() 
    seq = findGoal(s, e, mn) 
    et = time.time() - t0 
    if isinstance(seq, int): 
        print("Not a valid sequence. Exit code: %s" %seq) 
    else: 
        x = [e0 for e0, e1 in seq] 
        y = [e1 for e0, e1 in seq]
        print("Sequence: %s" %seq) 
        v = isValidSequence(x, y, mn, 1)
        print("Sequence: %s" %seq) 
        if v == 1: 
            print("Sequence is valid." ) 

    print("Elapsed time: %s" %et)
    return seq 

# ------------------------------------------------------------ # 

test2([1, 2], [5, 4], [8, 8])

print("") 
print("Sample usage: ") 
print("     sequence = test2(start, end, grid_size)") 
print("     sequence = test2([1, 2], [5, 4], [8, 8]")
print("") 

#if __name__ == '__main__': 
#    
#    test2([1, 2], [5, 4], [8, 8]) 


