from imutils.perspective import four_point_transform
import matplotlib.pyplot as plt
import pytesseract
import imutils
import cv2
import re
import numpy as np
import os
from PIL import Image
# 파일 꺼내오고
# 그거 이미지누끼딴후
# 이미지 shape가 2일때랑 3일때랑 분리해서 가야할듯
# 글자추출
# 그 영역 하얀색으로 지우기
# 번역하기
# 번역한 글자 끄집어 넣어주기 깔즤
def plt_imshow(title='image', img=None, figsize=(8 ,5)):
    plt.figure(figsize=figsize)

    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []
            for i in range(len(img)):
                titles.append(title)
 
        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)
 
            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
        plt.show()
        
    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()


path = "/Users/jojeonghyeon/Documents/WorkSpace/PYTHON/trans_test"
dirlsts = os.listdir(path)
print(dirlsts)
org_image = cv2.imread(path + "/" + dirlsts[0],0)
print(type(org_image))
image = org_image.copy()
image = imutils.resize(image, width=500)
print(image.shape)
ratio = org_image.shape[1] / float(image.shape[1])
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
# 이미지를 grayscale로 변환하고 blur를 적용
# 모서리를 찾기위한 이미지 연산
if len(image.shape) < 3:
    gray = image
else :
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
edged = cv2.Canny(blurred, 75, 200)
plt_imshow('edged',org_image)

# plt_imshow(['gray', 'blurred', 'edged'], [gray, blurred, edged])

print("imready")

text = pytesseract.image_to_string(edged,lang = 'jpn_vert')
print(text)
#여기서 자막부분을 가져와서 그거 주변부분 하이라이트 해주기 그걸로 하이라이트를 해줄거양