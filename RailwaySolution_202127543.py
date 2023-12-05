from Stack import LStack

print("열차 번호를 입력하세요")
target = list(map(int, input().split()))
print("input : ", target)
station = LStack()
targetIndex = 0
#들어가는건 1,2,3,4,5순서로 들어갈거고
#나오는건 그 순서로 나올 수 있는지 알려주라. 이게 target임
#station에 들어가게 만들어두고 그게 12345순서로 나올 수 있는지 검사 -> 역순으로 생각

for current in range(1, len(target) +1):
    station.push(target[targetIndex])
    while True:
        if station.isEmpty(): #pop이 되어있는지 검사
            break
        if current == station.topv(): # 1을 뺄 수 있는가?-> 지금 전부 다 들어가 있을수도 아무튼 이걸 넣어준 수에 맞는 횟수만큼 무조건 만족해야함. 
            station.pop() # 13245를 할 때 3을 두번빼게 되는데, current값이 2이상 벗어나버리면 안빠지는 값이 있을거임. 14253같이 4가 3번빠지게 될텐데, 3번빠지면 이미 참조하는값이 4라 그 이후에는 더 작은값이 못나옴. 1 3 2 4 5는 3보다 큰 4값이 나와서 성공.
            targetIndex += 1
        else:
            break
            

if station.isEmpty():
    print(True)
else:
    print(False)