
only3_5 = []
def push3_5(n):
    for i in range(len(n)):
        if n[i]%3==0 or n[i]%5==0:
            only3_5.append(n[i])

num = []
for i in range(5):
    n = int(input("Enter an integer: "))
    num.append(n)

push3_5(num)
print(only3_5)

n1 = len(only3_5)
print(n1)
while n1>=0:
    if n1==0:
        print("StackEmpty")
        n1 = n1-1
    else:
        print(only3_5[n1 - 1],end=' ')
        only3_5.pop()
        n1 = n1 - 1
