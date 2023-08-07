#generate numbers for 'tambola' game
import random
numlist=list(range(1,91))
num=random.sample(numlist,90)
'''
for i in range(91):
    r=input("generate:")
    if r=='':
        print(num[i],"\n")
    elif r=='show':
        a=num[0:i]
        print(sorted(a),"\n")
    elif r=='end':
        break
    
'''
k=[]

for i in range(91):
    r=input("generate: ")
    if r=='':
        if len(num)!=0:
            x=num.pop()
            print(x,"\n")
            k.append(x)
        else:
            print(sorted(k),"\n")
            break
    elif r=='show':
        n=sorted(k)
        for i in range(len(n)):
            print (n[i])
            i += 1
            if n[i]%10 == 0:
                print("\n")
            else:
                print(" ")
    elif r=='end':
        print(sorted(k),"\n")
        break
        
