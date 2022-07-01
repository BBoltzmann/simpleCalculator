string = input("Enter your password:")
def strCounter(string):
    st = num = ch = 0

    for c in string:
        if c.isdigit():
            num+=1
        elif c.isalpha():
            st+=1
        else:
            ch+=1
    return st, num, ch
alpha, beta, gama = strCounter(string)
sum = alpha+ beta + gama 
print("passwordcount",sum)
print("Number of letters in your password",alpha)
print("Number of digits in your password",beta)
print("Number of characters in your password",gama)