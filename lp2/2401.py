n = int(input())
r = 1
while(n > 0):
    n -= 1
    c = input().split()
    if(c[1] == '*'):
        r *= int(c[0])
    elif(c[1] == '/'):
        r /= int(c[0])

print(int(r))