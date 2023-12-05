class DNode:
    def __init__(self, d, p, n):
        self.data = d
        self.prev = p
        self.next = n

    def getPrev(self):
        return self.prev

    def setPrev(self, p):
        self.prev = p

    def getNext(self):
        return self.next

    def setNext(self, n):
        self.next = n

    def getElement(self):
        return self.data

    def setElement(self, d):
        self.data = d


