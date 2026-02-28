import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        w,h,r = input().split()
        w = int(w)
        h = int(h)
        d = int(r)* 2
        if d < w and d < h:
            print("YES")
        else:
            print("NO")
        
            
        
    except EOFError:
        break