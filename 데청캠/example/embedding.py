from skimage import data, io
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

# # example image 1
#
# camera = data.camera()
# io.imshow(camera)
# plt.show()
# print(type(camera),camera.shape)
# print(camera)
#
# cat = data.chelsea()
# io.imshow(cat)
# plt.show()
# print(type(cat), cat.shape)
# print(cat)


# # example image 2
# red = np.array([[0,80,80],[10,255,255]])
# orange = np.array([[13,80,80],[23,255,255]])
# yellow = np.array([[25,80,80],[35,255,255]])
# green = np.array([[40,80,80],[80,255,255]])
# blue = np.array([[80,80,80],[40,255,255]])
# pink = np.array([[145,80,80],[160,255,255]])
# red_high = np.array([[170,80,80],[180,255,255]])
#
# color_names = ['red','orange','yellow','green','blue','pink']
# colors = [red,orange,yellow,green,blue,pink,red_high]
#
# # url = 'https://scikit-image.org/docs/stable/_static/img/logo.png'
# url = 'https://ssl.pstatic.net/tveta/libs/1287/1287131/5cf390889466bf6947dc_20200708155112268.jpg'
#
# image = io.imread(url)
# image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
# hsv = cv.cvtColor(image, cv.COLOR_RGB2HSV)
#
# ratio_dic = {}
# for i in range(len(colors)):
#     mask = cv.inRange(hsv, colors[i][0], colors[i][1])
#     io.imshow(mask)
#     plt.show()
#
#     if i != len(colors) -1:
#         ratio_dic[color_names[i]] = np.count_nonzero(mask)/float(np.prod(mask.shape))*100
#     else:
#         ratio_dic[color_names[0]] = ratio_dic[color_names[0]] + np.count_nonzero(mask) / float(np.prod(mask.shape)) * 100
#
# print(ratio_dic)


# example nlp
from collections import Counter
import pytagcloud

tag = [('hello',100),('world',80),('nice',60),('to',20),('meet',10),('you',50)]
tag_list = pytagcloud.make_tags(tag, maxsize=50)
pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(900,600), rectangular=False)

import webbrowser
webbrowser.open('word_cloud.jpg')