import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        c, h, o = input().split()
        c = int(c)
        h = int(h)
        o = int(o)
        c = c // 2
        h = h // 6
        atom = [c, h, o]
        min_atom = min(atom)
        print(min_atom)
        
        
    except EOFError:
        break