from tkinter import *



class Figure:
    def __init__(self, canvas, **coords):
        self.__dict__.update(coords)
        self.canvas = canvas
        self.rectangles = []
        self.triangles = []
        self.hexagons = []
        self.rectangles_generated = False
        self.triangles_generated = False
        self.hexagons_generated = False

    def create_rectangles(self):
        while not self.rectangles_generated:
            for i in range(1000):
                self.rectangles.append(self.canvas.create_rectangle(
                    self.x1 + (i*40), self.y1, self.x2 + (i*40), self.y2, fill='black'))
                self.rectangles.append(self.canvas.create_rectangle(
                    self.x1 - (i*40), self.y1, self.x2 - (i*40), self.y2, fill='black'))
            self.rectangles_generated = True
        for each in self.rectangles:
            self.canvas.move(each, -1, 0)
        self.canvas.after(10, self.create_rectangles)


    def create_triangles(self):
        while not self.triangles_generated:
            for i in range(1000):
                self.triangles.append(self.canvas.create_polygon(
                    self.x1 + (i*40), self.y1, self.x2  + (i*40), self.y2, self.x3  + (i*40), self.y3
                ))
                self.triangles.append(self.canvas.create_polygon(
                    self.x1 - (i*40), self.y1, self.x2  - (i*40), self.y2, self.x3  - (i*40), self.y3
                ))
            self.triangles_generated = True
        for each in self.triangles:
            self.canvas.move(each, 1, 0)
        self.canvas.after(10, self.create_triangles)


class Objects(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.parent.title('Манипуляции с фигурами')
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()


    def initUI(self):
        self.canvas_area = Button(
            self, text='Поле', width=10, command=self.make_canvas)
        self.rectangles = Button(
            self, text='gen_rectangle()',
             command=self.gen_rectangle, width=16)
        triangles = Button(self, text='gen_triangles()', command=self.gen_triangle, width=16)
        self.rectangles.grid(row=0, column=1)
        self.canvas_area.grid(row=0, column=0)
        triangles.grid(row=0, column=2)

    def make_canvas(self):
        self.canvas_window = Toplevel(self)
        self.canvas = Canvas(self.canvas_window, width=500, height=500)
        self.canvas.grid(row=0, column=0)
        self.canvas.focus()

    def gen_rectangle(self):
        self.all_rects = Figure(self.canvas, x1=250, y1=250, x2=275, y2=275)
        self.all_rects.create_rectangles()

    def gen_triangle(self):
        self.all_triangles = Figure(self.canvas, x1=300, y1=250, x2=220, y2=330, x3=265, y3=250)
        self.all_triangles.create_triangles()


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
