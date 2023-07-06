dic = {101:'C++',102:'Python',103:'Java'}
stk=[]
for key in dic:
        x = str(key) + ':' + str(dic[key])
        stk.append(x)
print(stk)
while True:
        print("Menu")
        print("1: Pop")
        print("2: Display")
        print("3: Exit")
        ch = int(input("enter choice: "))
        def display():
                if len(stk)==0:
                        print("UNDERFLOW")
                else:
                        print(stk[-1],'<-- TOP')
                        for i in range(-2,-len(stk)-1,-1):
                                print(stk[i])
        def pop1():
                if len(stk)==0:
                        print("UNDERFLOW")
                else:
                        ch1 = input("Do u want to pop item?(y or n)...")
                        if ch1=='y':
                                stk.pop()
                                display()

        if ch==1:
                pop1()
        elif ch==2:
                display()
        elif ch==3:
                break
        else:
                print("Invalid Choice")

        
