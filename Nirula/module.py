def factorial(n):
    f=1
    for v in range(1,n+1):
        f*=v
    return f

#factorial(n)

def find_sum(n):
    n=input("Enter the value:")
    sm=0
    for ch in n:
        sm+=int(ch)
    return sm

#find_sum

def is_palindrome():
    st=input("enter the string:")
    if st==st[::-1]:
        return True
    else:return False
    
#is_palindrome()