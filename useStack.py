from Stack import Stack

def ParenMatch(X, n):
    S=Stack(10)
    for i in range(0, n):
        if isOpening(X[i]):
            S.push(X[i])
        else: #if closing
            if S.isEmpty():
                return False
            if not isMatch(X[i], S.pop()):
                return False
    if S.isEmpty():
        return True
    else:
        return False

def isOpening(a):
    if a=='(' or a =='{' or a=='[' :
        return True
    else:
        return False

def isMatch(a,b):
    if (a==')' and b=='(') or (a=='}' and b=='{') or (a==']' and b=='['):
        return True
    else:
        return False

#X=['{','}', '[','{','}',']']
X=['{','[','}',']']
print(ParenMatch(X, len(X)))