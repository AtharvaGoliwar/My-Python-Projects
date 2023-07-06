#testing
import pickle 
'''lis=['Atharva is a coder']
file=open('todo.dat','ab')
pickle.dump(lis,file)
print("gg")'''

'''lis = []
file = open('todo.dat','rb')
lis1=[]
try:
    while True:
        lis = pickle.load(file)
        lis1.append(lis)
        print(lis)
except EOFError:
    file.close()
print(lis1)'''
'''lis1.pop()

for i in range(len(lis1)):
    file1 = open('todo.dat','wb')
    pickle.dump(lis1[i],file1)

lis3=[]
file2 = open('todo.dat','rb')
try:
    while True:
        lis3=pickle.load(file2)
        print(lis)
except EOFError:
    file.close()'''

'''f1 = open('C:\\Users\\Atharva Goliwar\\Desktop\\todo.dat','ab')
pickle.dump(['hello'],f1)
print("gg")'''

def todoread():
    f1 = open('C:\\Users\\Atharva Goliwar\\Desktop\\todo.dat','rb')
    ch1=[]
    ch=[]
    try:
        while True:
            ch1=pickle.load(f1)
            ch.append(ch1)
            print(ch1)
    except EOFError:
        f1.close()
    print(ch)

todoread()



