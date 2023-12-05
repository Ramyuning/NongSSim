from random import randint
import time


def insertion_sort(list):
    s_list=list[:]
    for end in range(1, len(s_list)):
        for i in range(end, 0, -1):
            if s_list[i-1] > s_list[i]:
                s_list[i-1], s_list[i] = s_list[i],s_list[i-1]
    return s_list




def merge_sort(list):
    if len(list)<=1:
        return list
    mid=len(list)//2
    sl=list[:mid]
    sr=list[mid:]
    S1=merge_sort(sl)
    S2=merge_sort(sr)
    return merge(S1,S2)

def merge(left,right):
    result=[]
    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0] <= right[0]:
                result.append(left[0])
                left= left[1:]
            else:
                result.append(right[0])
                right= right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result
def quick_sort(list):
    L=[]
    E=[]
    G=[]
    if(len(list)!=0):
        pivot = list[0]
        for i in range(len(list)):
            if list[i]<pivot:
                L.append(list[i])
            elif list[i] == pivot:
                E.append(list[i])
            else:
                G.append(list[i])
        L=quick_sort(L)
        G=quick_sort(G)
    return L+E+G

def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                BIG = list[j]
                list[j] = list[j+1]
                list[j+1] = BIG
    return list

n=int(input("몇 개의 숫자를 생성할까요?"))
S=[]
for i in range(0,n):
    S.append(randint(1,1000))
# print(S)
time_1 = int(round(time.time()*100000))
insertion_sort(S)
# print("InsertionSort:",insertion_sort(S))
time_2 = int(round(time.time()*100000))
print("Insertion Sort 걸린시간",time_2-time_1)
time_1 = int(round(time.time()*100000))
merge_sort(S)
# print("merge Sort : ", merge_sort(S))
time_2 = int(round(time.time()*100000))
print("Merge Sort 걸린시간",time_2-time_1)
time_1 = int(round(time.time()*100000))
quick_sort(S)
# print("Quick Sort : ", quick_sort(S))
time_2 = int(round(time.time()*100000))
print("Quick Sort 걸린시간",time_2-time_1)

time_1 = int(round(time.time()*100000))
bubble_sort(S)
time_2 = int(round(time.time()*100000))
print("Bubble Sort 걸린시간",time_2-time_1)
