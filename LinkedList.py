# from Node import DNode
# class LinkedList:
#     def __init__(self) :
#         self.head = DNode("head", None, None)
#         self.trailer = DNode("trailer", self.head, None)
#         self.head.setNext(self.trailer)
#         self.numElem = 0

#     def isEmpty(self):
#         if(self.numElem==1):
#             return True
#         else:
#             return False
#     def size(self):
#         return self.numElem

#     def First(self):
#         if self.numElem==0:
#             print("원소가 없서서 구해올 수 업습니다ㅡㅜ")
#         else:
#             return self.head.getNext()

#     def Last(self):
#         if self.numElem==0:
#             print("원소가 없어서 구해올 수 없습니다")
#         else:
#             return self.trailer.getNext()

#     def insertFirst(self,elem):
#         q=DNode(elem, self.head, self.head.getNext())
#         (self.head.getNext()).setPrev(q)
#         self.head.setNext(q)
#         self.numElem= self.numElem+1
#         return q

#     def inserAfter(self, p, elem):
#         q=DNode(elem, p, p.getNext())
#         (p.getNext()).setPrev(q)
#         p.setNext(q)
#         self.numElem= self.numElem+1
#         return q

#     def insertBefore(self, p , elem):
#         q=DNode(elem, p.getPrev(), p)
#         (p.getPrev()).setNext(q)
#         p.setPrev(q)
#         self.numElem= self.numElem+1
#         return q
    
#     def insertLast(self, elem):
#         v=DNode(elem, self.trailer.getPrev(), self.trailer)
#         (self.trailer.getPrev()).setNext(v)
#         self.trailer.setPrev(v)
#         self.numElem=self.numElem+1
#         return v

#     def printList(self):
#         cur = self.head
#         print("(", end='')
#         while cur!=self.trailer:
#             if cur!=self.head:
#                 if cur.getNext()!=self.trailer:
#                     print(cur.data, '-', end='')
#                 else:
#                     print(cur.data, ')', end='')
#             cur=cur.getNext()

# if __name__ == '__main__':
#     ll=LinkedList()
#     p1=ll.insertFirst("aaa")
#     p2=ll.inserAfter(p1,"BBB")
#     p3=ll.insertFirst("CCC")
#     ll.printList()
    

from Node import DNode

class LinkedList: # by Hyerim Bae
    def __init__(self):
        self.head  = DNode("head", None, None)
        self.trailer = DNode("trailer", self.head, None)
        self.head.setNext(self.trailer)
        self.numElem = 0

    def isEmpty(self):
        if(self.numElem==0):
            return True
        else:
            return False

    def size(self):
        #return self.numElem
        size=0
        cur=self.head
        while not cur.getNext() == self.trailer:
            cur=cur.getNext()
            size=size+1
        return size

    def First(self):
        if self.numElem ==0:
            print("원소가 없습니다.")
        else:
            return self.head.getNext()

    def Last(self):
        if self.numElem ==0:
            print("원소가 없습니다.")
        else:
            return self.trailer.getPrev()

    def insertFirst(self, elem):
        v=DNode(elem, self.head, self.head.getNext())
        (self.head.getNext()).setPrev(v)
        self.head.setNext(v)
        self.numElem=self.numElem+1
        return v

    def insertLast(self, elem):
        v=DNode(elem, self.trailer.getPrev(), self.trailer)
        (self.trailer.getPrev()).setNext(v)
        self.trailer.setPrev(v)
        self.numElem=self.numElem+1
        return v

    def insertAfter(self, pos, elem):
        v=DNode(elem, pos, pos.getNext())
        (pos.getNext()).setPrev(v)
        pos.setNext(v)
        self.numElem=self.numElem+1
        return v

    def insertBefore(self, pos, elem):
        v = DNode(elem, pos.getPrev(), pos)
        (pos.getPrev()).setNext(v)
        pos.setPrev(v)
        self.numElem = self.numElem + 1
        return v

    def remove(self, pos):
        elem=pos.getElement()
        pos.getPrev().setNext(pos.getNext())
        pos.getNext().setPrev(pos.getPrev())
        pos.setPrev(None)
        pos.setNext(None)
        self.numElem=self.numElem-1
        return elem

    def replaceElement(self, pos, elem):
        e=pos.getElement()
        pos.setElement(elem)
        return e

    def printList(self):
        cur = self.head
        print("(", end='')
        while cur!=self.trailer:
            if cur!=self.head:
                if cur.getNext()!=self.trailer:
                    print(cur.data, '-', end='')
                else:
                    print(cur.data, ')', end='')
            cur=cur.getNext()

    def toString(self):
        cur = self.head
        str = ""
        while cur!=self.trailer:
            if(cur!=self.head):
                str += cur.getElement()
            cur=cur.getNext()
        return str