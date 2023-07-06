#A small Coding Interview question
import random
lis = []
in_circle = []
in_square=[]
def points(n):
    for i in range(n):
        x1 = random.uniform(0,1)
        y1 = random.uniform(0,1)
        lis.append((x1,y1))
points(1000)
print(lis)
for i in range(1000):
    check = (lis[i][0])*(lis[i][0]) + (lis[i][1])*(lis[i][1])
    if check<1:
        in_circle.append(lis[i])

print(len(in_circle))
n = (len(in_circle) / 1000)*4
print(n)