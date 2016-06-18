#!/usr/bin/python 

def move(pos0,n): 
    "The position (x, y) is updated based on input u(n)." 
    u = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]] 
    pos1 = [0,0] 
    pos1[0] = pos0[0] + u[n][0]
    pos1[1] = pos0[1] + u[n][1]
    return pos1 

def isValidPos(pos,mn): 
    "Returns 1 if pos is within bounds." 
    xmin = 0; 
    ymin = 0;
    xmax = mn[1]; 
    ymax = mn[0]; 
    if pos[0] < xmin: 
        return 0 
    elif pos[0] > xmax: 
        return 0 
    elif pos[1] < ymin: 
        return 0 
    elif pos[1] > ymax: 
        return 0 
    else: 
        return 1


def isValidMove(pos0,pos1,mn):
    "Check if pos1 can be reached from pos0 in one move."
    for n in xrange(0,7):
        pos = move(pos0, n)
        if pos[0] == pos1[0] and pos[1] == pos1[1]:
            if isValidPos(pos,mn): 
                return n  
    return 0 

def isValidSequence(seq_x, seq_y, mn = [8,8], fplot = 0): 
    "Return 1 if sequence is valid, 0 otherwise."
    pos0 = [seq_x[0], seq_y[0]] 
    seq = zip(seq_x[1:], seq_y[1:])
    pos = pos0 
    if fplot: 
        n = 1
        s1 = 79*"." 
        s2 = "Initial board"
        print(s1) 
        print(s2) 
        e = seq[-1] 
        plotState(s = pos0, e = e)
        for pos in seq:
            s2 = "Move " + repr(n)
            n += 1
            print(s1) 
            print(s2)
            plotState(pos, pos0, e)
        print(s1) 
    
    for p in seq:
        if isValidMove(pos, p, mn): 
            pos = p 
        else: 
            return 0
   
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
        print("    " + " ".join(r for r in row))  
    print("") 

def test():
    # A test sequence of locations on the board
    seq_x = [1, 3, 5] 
    seq_y = [2, 3, 4]
    mn = [8, 8] 
    v = isValidSequence(seq_x, seq_y, mn,1) 
    if v == 1: 
        print("Above sequence is valid.") 
    elif v <=0: 
        print("Above sequence is not valid.") 
    seq = [[1, 2], [3, 4], [5, 4]] 
    v = isValidSequence([x for x, y in seq], [y for x, y in seq], mn, 1) 
    if v == 1: 
        print("Above sequence is valid.")
        print("") 
    elif v <= 0: 
        print("Above sequence is not valid.")
        print("") 
# ------------------------------------------------------- # 

print("") 
test()
print("") 
print("Demonstration of level 1 functionalities.") 
print("") 

