from tkinter import *

class Rectangle:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.gen_rect = []

    def create_rectangles(self):
        for i in range(10):
            self.gen_rect.append(self.canvas.create_rectangle(
                self.x1 + (i*40), self.y1, self.x2 + (i*40), self.y2, fill='black'))  # right
            self.gen_rect.append(self.canvas.create_rectangle(
                self.x1 - (i*40), self.y1, self.x2 - (i*40), self.y2, fill='black'))  # left


class Objects(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.parent.title('Манипуляции с фигурами')
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()


    def initUI(self):
        self.rectangles = Button(
            self, text='gen_rectangle()',
             command=self.gen_rectangle, width=16)
        self.rectangles.grid(row=0, column=0)



    def gen_rectangle(self):
        self.gen_rectangle = Toplevel(self)
        self.canvas = Canvas(self.gen_rectangle, width=500, height=500)
        self.canvas.grid(row=0, column=0)
        self.all_rects = Rectangle(self.canvas, 250, 250, 275, 275)
        self.all_rects.create_rectangles()
        self.canvas.focus()

    def centerWindow(self):
        w = 400
        h = 32
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))




def main():
    root = Tk()
    ex = Objects(root)
    root.mainloop()

if __name__ == '__main__':
    main()
