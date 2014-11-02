'''
Created on 2014年11月2日

@author: mengxiang
'''
#我的第一个python程序
 
from tkinter.messagebox import Message
from tkinter import * 
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.infoInput=Entry(self)
        self.infoInput.pack()
        self.quitButton = Button(self, text='退出', command=self.quit)
        self.quitButton.pack()
        self.showButton=Button(self,text="显示",command=self.showInfo)
        self.showButton.pack()
    def showInfo(self):
        info=self.infoInput.get() or 'world'
        messagebox.showinfo("信息提示",' %s' % info)
        
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()