from tkinter import *
import time


class RandomName(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.name_list = []
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        #  定义标签栏
        l = Label(self, textvariable=self.timestr, font=("微软雅黑, 300"))
        self.set_name(self._elapsedtime)
        l.pack(side=TOP)

    def update(self):
        # 更新显示内容
        self._elapsedtime = time.time() - self._start
        self.set_name(self._elapsedtime)  # 设置显示内容
        self._timer = self.after(100, self.update)  # 刷新界面

    def set_name(self, elap):
        # 随机产生姓名
        name_list = ['王禹惟', '赵楚宜', '陈天廊', '汪圣展', '李芊淑', '孙一丁', '袁汉蕴', '蔡  昊',
                     '马镜涵', '曹涵晰', '陈宏嘉', '魏麟懿', '王  泽', '朱泓澎', '樊  想', '崔敬茜']
        cur = int(elap * 100 % len(name_list))
        self.timestr.set(name_list[cur])
        print(name_list[cur])

    def Start(self):
        # 开始
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self.update()
            self._running = True

    def Stop(self):
        # 暂停
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self.set_name(self._elapsedtime)
            self._running = False


    def name_label(self):
        # 显示窗口
        self.pack(side=TOP)
        Button(self, text='开始', command=self.Start, width=20, height=5).pack(side=LEFT)
        Button(self, text='结束', command=self.Stop, width=20, height=5).pack(side=LEFT)


if __name__ == '__main__':
    root = Tk()
    root.title("少惠林编程中级班选人答题神器")
    root.geometry('1600x900')
    sw = RandomName(root)
    sw.name_label()
    root.mainloop()
