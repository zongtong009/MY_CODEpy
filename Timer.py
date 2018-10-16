import tkinter as tk
import time


class Timer(tk.Frame):
    msec = 50

    def __init__(self, parent=None, **kw):
        tk.Frame.__init__(self, parent, kw)
        self.start = 0.0
        self.eTime = 0.0
        self.isRunning = False
        self.timestr = tk.StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        '''制作时间标签'''
        l = tk.Label(self, textvariable=self.timestr)
        self._setTime(self.eTime)
        l.pack(fill=tk.X, expand=tk.NO, pady=2, padx=2)

    def _update(self):
        '''用逝去的时间更新标签'''
        self.eTime = time.time() - self.start
        self._setTime(self.eTime)
        self.timer = self.after(self.msec, self._update)

    def _setTime(self, elap):
        '''将时间格式改为分：秒：百分秒'''
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

    def Start(self):
        if not self.isRunning:
            self.start = time.time() - self.eTime
            self._update()
            self.isRunning = True

    def Stop(self):
        if self.isRunning:
            self.after_cancel(self.timer)
            self.eTime = time.time() - self.start
            self._setTime(self.eTime)
            self.isRunning = False
            print(self.eTime)

    def Reset(self):
        self.start = time.time()
        self.eTime = 0.0
        self._setTime(self.eTime)


if __name__ == '__main__':
    winForm = tk.Tk()

    timer = Timer()
    timer.pack(side=tk.TOP)
    tk.Button(winForm, text='开始', command=timer.Start).pack(side=tk.LEFT)
    tk.Button(winForm, text='暂停', command=timer.Stop).pack(side=tk.LEFT)
    tk.Button(winForm, text='重置', command=timer.Reset).pack(side=tk.LEFT)
    tk.Button(winForm, text='退出', command=timer.quit).pack(side=tk.LEFT)

    winForm.mainloop()
