# -*- coding:utf-8 -*-
'''
Created on 2018-03-10
@author: Hugh
'''

from Tkinter import *
from ConfigParser import ConfigParser
import re

class scorer:

    def __init__(self, layers, score):
        self.layers = layers
        self.score = score

    def tk_gui(self):
        global L1,L2,entry,root
        root = Tk()
        root.wm_title(u"冒险岛拉克兰计分器")
        root.geometry('300x280+150+200')
        Label(root,text="层数:").grid(row = 0, sticky = W)
        L1 = Label(root,text=self.layers)
        L1.grid(row = 0, column = 1)
        Button(root,text="层数+10",command = self.add_layers).grid(row = 0, column = 3, columnspan = 2,sticky = W)
        Label(root,text="分数:").grid(row = 2,sticky = W)
        L2 = Label(root,text=self.score)
        L2.grid(row = 2, column = 1, sticky = W)
        Label(root, text="分数+").grid(row=3, sticky = W)

        Button(root, text="40", command = self.add_score40).grid(row = 3, column = 1)
        Button(root, text="50", command=self.add_score50).grid(row=3, column=2)
        Button(root, text="60", command=self.add_score60).grid(row=3, column=3)
        Button(root, text="70", command=self.add_score70).grid(row=3, column=4)
        Button(root, text="80", command=self.add_score80).grid(row=3, column=5)

        entry = Entry(root)
        entry.grid(row = 5, column = 0, columnspan = 6,sticky = W)
        Button(root, text="重置层数", command = self.reset_layers).grid(row = 6, column = 0, columnspan = 3, sticky = W)
        Button(root, text="重置分数", command=self.reset_score).grid(row=6, column=3, columnspan=3, sticky=W)
        # Entry(root).grid(row = 0, column = 2, sticky = E)
        root.protocol('WM_DELETE_WINDOW', self.savedata)
        root.mainloop()

    def add_layers(self):
        self.layers += 10
        L1["text"] = self.layers

    def add_score40(self):
        self.score += 40
        L2["text"] = self.score
    def add_score50(self):
        self.score += 50
        L2["text"] = self.score
    def add_score60(self):
        self.score += 60
        L2["text"] = self.score
    def add_score70(self):
        self.score += 70
        L2["text"] = self.score
    def add_score80(self):
        self.score += 80
        L2["text"] = self.score

    def reset_layers(self):
        self.layers = int(entry.get())
        L1["text"] = self.layers
    def reset_score(self):
        self.score = int(entry.get())
        L2["text"] = self.score

    def savedata(self):

        cf = ConfigParser()
        fp = "./config.ini"
        cf.read(fp)
        cf.set("savedata", "layers", self.layers)
        cf.set("savedata", "score", self.score)
        with open(fp, 'w') as fw:  # 循环写入
            cf.write(fw)
        root.destroy()

if __name__ == '__main__':
    cf = ConfigParser()
    cf.read("./config.ini")
    layers = cf.get("savedata", "layers")
    score = cf.get("savedata", "score")
    print type(layers)
    a = scorer(int(layers),int(score))
    a.tk_gui()