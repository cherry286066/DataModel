x=input("enter a string")
y=input("enter another string")
s=0
for i in range(len(x)):
    for j in range(len(y)):
        if x[i]==y[j]:
            s=s+1
            break
#added comments
if s==len(x):
    print("it is anagram")
else:
    print("its not an anagram")
