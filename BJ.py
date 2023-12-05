import sys

N , K = map(int,sys.stdin.readline().split())
A = []
for i in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))
Answer = 0
Weight = 0
Answer_list = [0]
# 가치합의 최대합은?
# bf or DP로 풀면되는데 DP로 푸는게 쉽겠죠?
## 0이 Weight 1이 밸류
# print(A)
B = []
A.sort(key=lambda x : x[1]/x[0], reverse= True)
# print(A)
for i in range(len(A)):
    B= []
    Answer = 0
    Weight = 0
    Answer += A[i][1]
    Weight += A[i][0]
    if Weight > K:
        Answer -= A[i][1]
        Weight -= A[i][0]
        continue
    B.append([Weight,Answer])
    if i == len(A):
        break
    for j in range(i+1,len(A)):
        for k in B:
            if k[0] + A[j][0] > K:
                continue
            else:
                Answer = k[1] + A[j][1]
                Weight = k[0] + A[j][0]
                # Answer = max(Answer,k[1] + A[j][1])
            # Answer = B[-1][1]+A[j][1]
            # Weight = B[-1][0]+A[j][0]
        # B.append([Weight,Answer])
        # if Weight > K:
        #     Weight -= A[j][0]
        #     Answer -= A[j][1]
            B.append([Weight,Answer])
        # max
        Answer_list.append(max(i[1] for i in B))
    # print(B)
    # Answer_list.append(Answer)
print(B)
print(max(Answer_list))