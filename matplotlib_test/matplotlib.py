import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def test_matplotlib():
    # fig, ax = plt.subplots()
    # x = np.arange(0, 4*np.pi, 0.1)
    # y = np.sin(x)
    # z = np.cos(x)
    # ax.plot(x, y, 'r--', x, z, 'b--')
    # ax.set_title('sin&cos')
    # ax.set_xlabel('x-axis')
    # ax.set_ylabel('y-axis')

    # fig, (ax1, ax2) = plt.subplots(1,2, sharey=True)
    # ax1.plot(x, y, 'r--', x, z, 'b--')
    # ax2.plot(x, y, z)


    #   散点图
    # x = np.array([1,2,3,4,5,6,7,8])
    # y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
    # sizes = np.array([20,50,100,200,500,1000,60,90])
    # colors = np.array(["red","green","black","orange","purple","beige","cyan","magenta"])
    # plt.scatter(x, y, sizes, c=colors, alpha=0.5)

    # 柱形图
    # x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
    # y = np.array([12, 22, 6, 18])

    # 竖柱形图
    # plt.bar(x,y)
    # 横柱形图
    # plt.barh(x,y, color = ["#4CAF50","red","hotpink","#556B2F"])

    # 加载地图图像, 下载地址：https://static.jyshare.com/images/demo/map.jpeg
    img = Image.open('images/image.png')
    # 转换为数组
    data = np.array(img)
    # 绘制地图
    plt.imshow(data)
    # 隐藏坐标轴
    plt.axis('off')

    plt.show()