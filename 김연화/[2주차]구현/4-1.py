x = 1
y = 1
N = int(input())
direction = list(map(str,input().split()))

for d in direction:
    if d=='R':
      if y == N:
          continue
      else:
          y+=1
    elif d=='L':
      if y == 1:
          continue
      else:
          y-=1
    elif d=='U':
      if x == 1:
          continue
      else:
          x-=1

    elif d=='D':
      if x == N:
          continue
      else:
          x += 1
print(x,y)
