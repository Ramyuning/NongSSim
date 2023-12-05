from StudentClass import Student
from Vector import MyVector
import sys

v=MyVector(2)

v.insertLast(Student("Gregg", 89))
v.insertLast(Student("Velva", 90))
v.insertLast(Student("Randell", 100))
v.insertLast(Student("Vallie", 75))
v.insertLast(Student("Tammi", 68))
v.insertLast(Student("Ima", 99))
v.insertLast(Student("Mina", 76))
v.insertLast(Student("Fleta", 88))

MIN_score = sys.maxsize
MAX_score = -(sys.maxsize - 1)

# print(MAX, MIN)
MAX = 0
MIN = 0

for i in range(v.size):
    if v.elementAt(i).score < MIN_score:
        MIN = i
        MIN_score = v.elementAt(i).score

for i in range(v.size): #202127543 조정현S
    if v.elementAt(i).score > MAX_score:
        MAX = i
        MIN_score = v.elementAt(i).score
print("가장 낮은 성적을 가진 친구 : ", v.elementAt(MIN).name, "| 성적 : ", v.elementAt(MIN).score)
print("가장 높은 성적을 가진 친구 : ", v.elementAt(MAX).name, "| 성적 : ", v.elementAt(MAX).score)
