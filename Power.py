def interativePower(x,n):
    ret = 1
    for i in range(n):
        ret = ret* x
    
    return ret

def recursivePower(x,n):
    if n==0:
        return 1
    else:
        return x*recursivePower(x, n-1)

def recursivePower2(x,n):
    if n==0:
        return 1
    if n%2 == 1:
        y=recursivePower2(x,(n-1)/2)
        return x*y*y
    else:
        y=recursivePower2(x,n/2)
        return y*y
        

    
    

x = int(input("파워함수의 밑을 얼마로 할까요? "))
n = int(input("파워함수에서 몇 승을 구할까요? "))
print("반복에 의한 함수",x, "의",n, "승은 ", interativePower(x, n), "입니다.")
print("재귀에 의한 함수",x, "의",n, "승은 ", recursivePower(x, n), "입니다.")
print("재귀2에 의한 함수",x, "의",n, "승은 ", recursivePower2(x, n), "입니다.")