# from LinkedList import LinkedList
# from Vector import MyVector
# import sys

# class Graph:
#     def __init__(self):
#         self.adjlink=LinkedList()

#     class GNode:
#         def __init__(self, n):
#             self.name=n

#         def getName(self):
#             return self.name

#         def setName(self, n):
#             self.name=n

#     class Edge:
#         def __init__(self, o, des, dis):
#             self.ori=o
#             self.dest=des
#             self.dis=dis
#         def getOri(self):
#             return self.ori

#         def getDes(self):
#             return self.dest

#         def getDistance(self):
#             return self.dis

#         def printEdge(self):
#             print(self.ori.getName(), ",", self.dest.getName(), ",", self.dis, end='')

#     def addAdjLink(self, ori, dest, distance):
#         #ori=GNode(o)
#         #dest=GNode(d)
#         edge = self.Edge(ori, dest, distance)
#         self.adjlink.insertLast(edge)

#     def printGraph(self):
#         l=self.adjlink
#         cur = l.head
#         while cur!=l.trailer:
#             if cur!=l.head:
#                 print("[", end='')
#                 cur.data.printEdge()
#                 print("]")
#             cur=cur.getNext()


# if __name__ == "__main__":
#     def minDistance(Q, d): #Q에 들어있는 것들 중에서 가장 작은 distance값을 가지는 것을 리턴
#         minimum = sys.maxsize
#         mindistnode = None
#         cur = Q.head.getNext()
#         while cur!=Q.trailer:
#             temp=distOf(cur.getElement(),d)
#             if temp<minimum:
#                 minimum= temp
#                 mindistnode=cur
#             cur = cur.getNext()
#         return mindistnode
    
#     def distOf(u,d): #d를 참조해서 현재의 u까지의 거리를 얻어줌
#         for i in range(len(d)):
#             if u==d[i][0]:
#                 return d[i][1]
    
#     def setDist(u,d,nd): # 거리를 업데이ㅡㅌ
#         for i in range(len(d)):
#             if u==d[i][0]:
#                 d[i][1]=nd
                
#     def neighbors(u, g): # g에서 u의 이웃을 가진 링크들을 찾아옴
#         v=MyVector(100)
#         l = g.adjlink
#         cur=l.First()
#         while cur!=l.Last():
#             if(u==cur.getElement().getOri()):
#                 v.insertLast(cur.getElement())
#             cur=cur.getNext()
#         return v
    
#     #### Graph initialization ####
#     g = Graph()
#     s = g.GNode("s")
#     a= g.GNode("a")
#     b= g.GNode("b")
#     c= g.GNode("c")
#     d= g.GNode("d")
#     g.addAdjLink(s,a,10)
#     g.addAdjLink(s,c,5)
#     g.addAdjLink(a,c,2)
#     g.addAdjLink(c,a,3)
#     g.addAdjLink(a,b,1)
#     g.addAdjLink(c,b,9)
#     g.addAdjLink(c,d,2)
#     g.addAdjLink(d,s,7)
#     g.addAdjLink(b,d,4)
#     g.addAdjLink(d,b,6)
#     print("============Graph created==========")
#     g.printGraph()
#     V = LinkedList()
#     V.insertLast(s)
#     V.insertLast(a)
#     V.insertLast(b)
#     V.insertLast(c)
#     V.insertLast(d)
    
#     Dist=[]
#     Dist.append([s,0])
#     Dist.append([a,sys.maxsize])
#     Dist.append([b,sys.maxsize])
#     Dist.append([c,sys.maxsize])
#     Dist.append([d,sys.maxsize])
    
#     Prd =[]
#     Prd.append([a,None])
#     Prd.append([b,None])
#     Prd.append([c,None])
#     Prd.append([d,None])
    
#     Q = V
#     k=LinkedList()
#     u = minDistance(Q,Dist)
#     k.insertLast(u)

    # print(neighbors(u,g).printVector())
    
    ## 여따가 적으세요 당신의 코드를 #####
    # while not Q.isEmpty == True:
    #     u = minDistance(Q,Dist) ## 제일 짧은거리 get도
    #     s.insertLast(u)
    #     nei = neighbors(u,g)
    #     for i in nei:
    #         if distOf(i,Dist) > distOf(u,Dist) + Dist[]:
    #             setDist(i,Dist,i)
from LinkedList import LinkedList
from Vector import MyVector
import sys

class Graph:
    def __init__(self):
        self.adjlink=LinkedList()

    class GNode:
        def __init__(self, n):
            self.name=n

        def getName(self):
            return self.name

        def setName(self, n):
            self.name=n

    class Edge:
        def __init__(self, o, des, dis):
            self.ori=o
            self.dest=des
            self.dis=dis
        def getOri(self):
            return self.ori

        def getDes(self):
            return self.dest

        def getDistance(self):
            return self.dis

        def printEdge(self):
            print(self.ori.getName(), ",", self.dest.getName(), ",", self.dis, end='')

    def addAdjLink(self, ori, dest, distance):
        #ori=GNode(o)
        #dest=GNode(d)
        edge = self.Edge(ori, dest, distance)
        self.adjlink.insertLast(edge)

    def printGraph(self):
        l=self.adjlink
        cur = l.head
        while cur!=l.trailer:
            if cur!=l.head:
                print("[", end='')
                cur.data.printEdge()
                print("]")
            cur=cur.getNext()

if __name__ == '__main__':

    def minDistance(Q, d): #Q에 들어있는 것들 중에서 가장 작은 distance값을 가지는 것을 리턴
        minimum = 10000
        mindistnode = None
        cur = Q.head.getNext()
        while cur!=Q.trailer:
            #temp=getDist(cur.getElement(), d)
            temp = distOf(cur.getElement(), d)
            #print(temp)
            if temp<minimum:
                minimum=temp
                mindistnode=cur
            cur=cur.getNext()
        return mindistnode

    def printLL(Q):
        cur = Q.head.getNext()
        print("[", end='')
        while cur != Q.trailer:
            if(cur.next==Q.trailer):
                print(cur.data.getName(), end='')
            else:
                print(cur.data.getName(), ',', end='')
            cur = cur.getNext()
        print(']')

    def neighbors(u, g): # g에서 u의 이웃을 가진 링크들을 찾아옴
        v=MyVector(100)
        l = g.adjlink
        cur=l.First()
        while cur!=l.Last():
            if(u==cur.getElement().getOri()):
                v.insertLast(cur.getElement())
            cur=cur.getNext()
        return v

    def distOf(u, d): #d를 참조해서 현재의 u까지의 거릴 값을 얻어옴
        for i in range(len(d)):
            if u==d[i][0]:
                return d[i][1]

    def setDist(u, d, nd): #거리를 없데이트
        for i in range(len(d)):
            if u==d[i][0]:
                d[i][1]=nd

    ############################# Initialization
    g=Graph()
    s=g.GNode("s")
    a=g.GNode("a")
    b=g.GNode("b")
    c=g.GNode("c")
    d=g.GNode("d")
    g.addAdjLink(s, a, 10)
    g.addAdjLink(s, c, 5)
    g.addAdjLink(a, c, 2)
    g.addAdjLink(c, a, 3)
    g.addAdjLink(a, b, 1)
    g.addAdjLink(c, b, 9)
    g.addAdjLink(c, d, 2)
    g.addAdjLink(d, s, 7)
    g.addAdjLink(b, d, 4)
    g.addAdjLink(d, b, 6)
    print("Graph inserted===================")
    g.printGraph()

    V=LinkedList()
    V.insertLast(s)
    V.insertLast(a)
    V.insertLast(b)
    V.insertLast(c)
    V.insertLast(d)
    # V.printList()
    #Dist=[[s,0], [a, 1000], [b, 1000], [c, 1000], [d,1000]]
    Dist=[]
    Dist.append([s, 0])
    Dist.append([a, sys.maxsize])
    Dist.append([b, sys.maxsize])
    Dist.append([c, sys.maxsize])
    Dist.append([d, sys.maxsize])

    Prd=[]
    Prd.append([a, None])
    Prd.append([b, None])
    Prd.append([c, None])
    Prd.append([d, None])

    Q=V
    S=LinkedList()
    # y = minDistance(Q,Dist)
    ## 여따가 적으세요 당신의 코드를 #####
    # while not Q.isEmpty == True:
    # u = minDistance(Q,Dist) ## 제일 짧은거리 get도 s임
    # print(u.getElement().getName())
    # S.insertLast(u.getElement())
    # # S.printList()
    # nei = neighbors(u.getElement(),g)
    # print(nei.getItems())
    # print(nei.getSize())
    # Q.remove(0)
    print("Initial Q=========")
    printLL(V)
    while not Q.isEmpty():
        u = minDistance(Q,Dist)
        S.insertLast(u.getElement())
        nei = neighbors(u.getElement(),g)
        for i in nei.getItems():
            if i !=0:
                if distOf(i.getDes(),Dist) > distOf(i.getOri(),Dist) + i.getDistance():
                    setDist(i.getDes(),Dist,distOf(i.getOri(),Dist) + i.getDistance())
                    for k in Prd:
                        if i.getDes() == k[0]:
                            k[1] = i.getOri()
        Q.remove(u)
    
    print("Min Distance of dijstra==========")
    for i in Dist:
        print(i[0].getName(), ":", i[1])
    print("Precedure============")
    for i in Prd:
        print(i[0].getName(), ":", i[1].getName())
    print("Final S===================")
    print("[", end='')
    # print(S.First().getElement().getName())
    # print(S.printList())
    A = []
    cur = S.head
    while cur!=S.trailer:
        if cur!=S.head:
            if cur.getNext()!=S.trailer:
                print(cur.data.getName(), end=' ,')
            else:
                print(cur.data.getName(), end=']')
        cur=cur.getNext()
    
    # for i in range(S.size()):
    #     S.First
    # print(Dist)
    # print(Prd)
        # for k in Dist:
        #     if u.getElement().getName() == k[0]:
        #         Q.remove(k[0])
    # if distOf(nei.elementAt(0),Dist) > distOf(u.getElement(),Dist):
    # # + g.adjlink.head :
    #     print("gal")
    # else:
    #     print("dal")
    # print(nei.getSize())
    # for i in range(len(nei.getSize())):
        
    #     distOf(nei.elementAt(i),Dist) > distOf(u.getElement(),Dist) + g.adjlink.head
    # print("끗이네요")
        # for i in nei:
        #     if distOf(i,Dist) > distOf(u,Dist) + Dist[]:
        #         setDist(i,Dist,i)
    
    # S.insertLast(y)
    # S.printList()
    # print(y.getElement())
    

    