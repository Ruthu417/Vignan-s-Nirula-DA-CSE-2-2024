s=input()
al=n=k=0
for i in s:
    if i.isalpha():
        al+=1
    elif i.isdigit():
        k+=1
    else:
        n+=1
print("number of alphabets=",al)
print("number of special characters=",n)
print("number of digits=",k)