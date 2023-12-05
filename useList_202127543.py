from LinkedList import LinkedList



s=input('키보드 타이핑을 하세요')
ll = LinkedList()
posLoc=ll.head
for i in range(len(s)):
    if(s[i]=='['): ## [를 마주쳤을때 가장 앞으로 가기 위해 head로 보냄.
        posLoc = ll.head
    elif(s[i]==']'): ## ]를 마주쳤을때 가장 뒤로
        posLoc = ll.trailer.getPrev
    else:
        if ll.numElem == 0: ## 아무것도 없을 시 linkedlist가 없어서 insertAfter를 쓸 수 없음. 따라서 insertFirst사용
            posLoc = ll.insertFirst(s[i])
        else:
            if posLoc == ll.trailer.getPrev: ## getPrev를 사용할시 insertAfter를 사용 불가(trailer는 특별한 노드라 거기에 뭘 잇기가 어려움.)
                posLoc = ll.insertLast(s[i])
            else:
                posLoc = ll.insertAfter(posLoc,s[i]) 
ll.printList()
