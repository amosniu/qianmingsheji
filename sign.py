from tkinter import *           # 导入tkinter的all里边的所有库
from tkinter import messagebox  # 用于弹出提示框
from PIL import Image,ImageTk   # 安装pillow这个库
import requests


def download():
    startUrl = 'http://www.uustv.com/'
    # 获取用户输入的姓名
    name = entry.get()
    # 去空格
    name = name.strip()
    # 判断姓名是否为空
    if name == '':
        messagebox.showinfo('提示','请输入姓名')
    else:
        # 模拟网页发送数据
        data = {
            'fontcolor':'# 000000',
            'fonts':'haku.ttf',
            'sizes':60,
            'word':name
        }
        result = requests.post(startUrl,data = data)
        # 设置编码 查看网页源代码中的charset属性值
        result.encoding = 'utf-8'
        # 获取网页源码
        html = result.text
        # 正则表达式
        reg = r'<div class="tu">﻿<img src="(.*?)"/></div>'
        imagePath = re.findall(reg,html)
        # 图片完整路径
        imageUrl = startUrl + imagePath[0]
        # 获取图片内容  content
        response = requests.get(imageUrl).content

        # # wb 二进制来写数据 存在则覆盖，不存在则新建
        # f = open('{}.gif'.format(name),'wb')
        # f.write(response)
        with open('{}.gif'.format(name),'wb') as f:
            f.write(response)

        # 显示图片
        bm = ImageTk.PhotoImage(file = '{}.gif'.format(name))
        label2 = Label(root,image = bm)
        label2.bm = bm
        # 合并列 columnspan 组件所跨越的列数
        label2.grid(row = 2,columnspan = 2)

# 创建窗口
root = Tk()

# 标题
root.title('签名设计')

# 窗口大小，位置
root.geometry('550x280+300+200')
# # 窗口位置
# root.geometry('+400+200')

# 标签控件
label = Label(root,text = '签名',font = ('华文行楷',20),fg = 'red')
# 显示控件 grid 网格式布局 pack 包装布局 place 位置布局
label.grid()

# 输入框
entry = Entry(root,font = ('宋体',16))
entry.grid(row = 0,column = 1)

# 点击按钮 command 触发方法
button = Button(root,text = '设计签名',font = ('微软雅黑',12),command = download)
# 设置宽高
button['width'] = 10
button['height'] = 0
# E 右对齐 W 左对齐
button.grid(row = 1,column = 1,sticky = E)


# 显示窗口 消息循环
root.mainloop()