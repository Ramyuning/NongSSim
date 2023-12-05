def binFib(k):
    if k<= 1:
        return k
    else:
        return binFib(k-1)+binFib(k-2)
    
def linFib(k):
    if k==1:
        return [k,0]
    else:
        l=linFib(k-1)
        i=l[0]
        j=l[1]
        return [i+j,i]
    
k= int(input("몇 번째 fibonacci 수를 구할까요? "))
print("BinFibonacci(",k,")는 ", binFib(k),"입니다.")
print("LinFibonacci(",k,")는 ", linFib(k)[0],"입니다.")