from tkinter import *
import math


class Figure:
    def __init__(self, canvas, **coords):
        self.__dict__.update(coords)
        self.canvas = canvas
        self.rectangles = []
        self.triangles = []
        self.hexagons = []
        self.ovals = []
        self.strips = []
        self.overlapping_1 = []
        self.overlapping_2 = []
        self.symmetric_1 = []
        self.symmetric_2 = []
        self.rectangles_generated = False
        self.triangles_generated = False
        self.hexagons_generated = False
        self.ovals_generated = False
        self.overlapping_generated = False
        self.symmetric_generated = False

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

    def create_hexagons(self):
        while not self.hexagons_generated:
            for i in range(1000):
                self.hexagons.append(self.canvas.create_polygon(
                    self.x4 + (i*80), self.y4, self.x5  + (i*80), self.y5, self.x6  + (i*80), self.y6,
                    self.x1 + (i*80), self.y1, self.x2  + (i*80), self.y2, self.x3  + (i*80), self.y3,
                ))
                self.hexagons.append(self.canvas.create_polygon(
                    self.x1 - (i*80), self.y1, self.x2  - (i*80), self.y2, self.x3  - (i*80), self.y3,
                    self.x4 - (i*80), self.y4, self.x5  - (i*80), self.y5, self.x6  - (i*80), self.y6,
                ))
            self.hexagons_generated = True
        for each in self.hexagons:
            if self.hexagons.index(each) // 3 :
                self.canvas.itemconfigure(each, fill='darkred')
            self.canvas.move(each, 10, 0)
        self.canvas.after(10, self.create_hexagons)

    def create_n(self, n, angle):
        while not self.ovals_generated:
            for i in range(1000):
                self.ovals.append(self.canvas.create_polygon(
                    self.get_n_angles_coords(self.x1 + (i*60), self.y1, self.x2 + (i*60), self.y2,
                                         n, angle)
                ))
                self.ovals.append(self.canvas.create_polygon(
                    self.get_n_angles_coords(self.x1 - (i*60), self.y1, self.x2 - (i*60), self.y2,
                                         n, angle)
                ))
            self.ovals_generated = True

    def get_n_angles_coords(self, x1, y1, x2, y2, n, angle):
        rotation = angle * math.pi / 180.0
        # Оси
        a = (x2 - x1) / 2.0
        b = (y2 - y1) / 2.0
        # Центр
        xc = x1 + a
        yc = y1 + b
        point_list = []
        for i in range(n):
            theta = (math.pi * 2) * (float(i) / n)
            x1 = a * math.cos(theta)
            y1 = b * math.sin(theta)
            # Поворачиваем x, y
            x = (x1 * math.cos(rotation)) + (y1 * math.sin(rotation))
            y = (y1 * math.cos(rotation)) - (x1 * math.sin(rotation))
            point_list.append(round(x + xc))
            point_list.append(round(y + yc))
        return point_list

    def create_3_strips(self): # 4.1
        for i in range(1000):
            self.strips.append(self.canvas.create_rectangle(
                self.x1 + (i*50), self.y1 + (i*50), self.x2 + (i*50), self.y2 + (i*50), fill='red'
            ))
            self.strips.append(self.canvas.create_rectangle(
                self.x1 - (i*50), self.y1 - (i*50), self.x2 - (i*50), self.y2 - (i*50), fill='red'
            ))
            self.strips.append(self.canvas.create_rectangle(
                self.x1-25 + (i*50), self.y1 + (i*50), self.x2-25 + (i*50), self.y2 + (i*50), fill='blue'
            ))
            self.strips.append(self.canvas.create_rectangle(
                self.x1-25 - (i*50), self.y1 - (i*50), self.x2-25 - (i*50), self.y2 - (i*50), fill='blue'
            ))
            self.strips.append(self.canvas.create_rectangle(
                self.x1+25 + (i*50), self.y1 + (i*50), self.x2+25 + (i*50), self.y2 + (i*50), fill='yellow'
            ))
            self.strips.append(self.canvas.create_rectangle(
                self.x1+25 - (i*50), self.y1 - (i*50), self.x2+25 - (i*50), self.y2 - (i*50), fill='yellow'
            ))

    def create_overlapping(self): # 4.2
        while not self.overlapping_generated:
            for i in range(1000):
                self.overlapping_1.append(self.canvas.create_rectangle(
                    self.x1 + (i*50), self.y1 + (i*25), self.x2 + (i*50), self.y2 + (i*25), fill='red'
                ))
                self.overlapping_1.append(self.canvas.create_rectangle(
                    self.x1 - (i*50), self.y1 - (i*25), self.x2 - (i*50), self.y2 - (i*25), fill='red'
                ))
                self.overlapping_2.append(self.canvas.create_polygon(
                    self.x1_2 + (i*40), self.y1_2, self.x2_2 + (i*40), self.y2_2, fill='blue'
                ))
                self.overlapping_2.append(self.canvas.create_rectangle(
                    self.x1_2 - (i*40), self.y1_2, self.x2_2 - (i*40), self.y2_2, fill='blue'
                ))
            self.overlapping_generated = True
        for each in self.overlapping_1:
            self.canvas.move(each, 4, 2)
        for each in self.overlapping_2:
            self.canvas.move(each, 5, 0)
        self.canvas.after(10, self.create_overlapping)

    def create_symmetric(self): #4.3
        while not self.symmetric_generated:
            for i in range(1000):
                self.symmetric_1.append(self.canvas.create_polygon(
                    self.get_n_angles_coords(
                        self.x1 + (i*30), self.y1, self.x2 + (i*30), self.y2, n=3, angle=150)))
                self.symmetric_1.append(self.canvas.create_polygon(
                    self.get_n_angles_coords(
                        self.x1 - (i*30), self.y1, self.x2 - (i*30), self.y2, n=3, angle=150)))
                self.symmetric_2.append(self.canvas.create_polygon(
                    self.get_n_angles_coords(
                        self.x1 + (i*30), self.y1+30, self.x2 + (i*30), self.y2+30, n=3, angle=90)))
                self.symmetric_2.append(self.canvas.create_polygon(
                    self.get_n_angles_coords(
                        self.x1 - (i*30), self.y1+30, self.x2 - (i*30), self.y2+30, n=3, angle=90)))
            self.symmetric_generated = True
        for each in self.symmetric_1:
            self.canvas.move(each, -7, 0)
        for each in self.symmetric_2:
            self.canvas.move(each, 7, 0)
        self.canvas.after(10, self.create_symmetric)


class Objects(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.parent.title('Манипуляции с фигурами')
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()
        self.all_figures = []

    def initUI(self):
        self.canvas_area = Button(
            self, text='Поле', width=10, command=self.make_canvas)
        self.rectangles = Button(
            self, text='gen_rectangle()',
             command=self.gen_rectangle, width=16)
        self.rectangles.grid(row=0, column=1)
        self.canvas_area.grid(row=0, column=0)
        triangles = Button(self, text='gen_triangles()', command=self.gen_triangle, width=16)
        hexagons = Button(self, text='gen_hexagons()', command=self.gen_hexagon, width=16)
        n_angles = Button(self, text='n_угольники()', command=self.gen_n_angles, width=16)
        rotating = Button(self, text='rotate()', command=self.rotate, width=16)
        strips_1 = Button(self, text='4.1', command=self.make_strips, width=2)
        strips_2 = Button(self, text='4.2', command=self.make_overlapping, width=2)
        symmetric = Button(self, text='4.3', command=self.make_symmetric, width=2)
        strips_1.grid(row=1, column=3, sticky='w')
        strips_2.grid(row=1, column=3)
        symmetric.grid(row=1, column=3, sticky='e')
        self.rotating_angle = Entry(self, width=16)
        moving = Button(self, text='move()', command=self.move, width=16)
        self.deltaxy = Entry(self, width=16)
        n_angle_label = Label(self, width=20, text='Кол-во углов, поворот')
        self.n_angle = Entry(self, width=16)
        triangles.grid(row=0, column=2)
        hexagons.grid(row=0, column=3)
        rotating.grid(row=1, column=0)
        moving.grid(row=1, column=1)
        n_angles.grid(row=0, column=4)
        n_angle_label.grid(row=1, column=4)
        self.rotating_angle.grid(row=2, column=0)
        self.deltaxy.grid(row=2, column=1)
        self.n_angle.grid(row=2, column=4)

    def make_canvas(self):
        self.canvas_window = Toplevel(self)
        self.canvas = Canvas(self.canvas_window, width=750, height=750)
        self.canvas.grid(row=0, column=0)
        # TODO: frontend
        for i in range(1000):  # x,y axes
            self.canvas.create_line(0 + (i*375), 375, 750 + (i*750), 375, width=2)
            self.canvas.create_line(0 - (i*375), 375, 750 - (i*750), 375, width=2)
            self.canvas.create_line(375, 750 + (i*750), 375, 0 + (i*750), width=2)
            self.canvas.create_line(375, 750 - (i*750), 375, 0 - (i*750), width=2)
        coords_grid = [i for i in range(1000000) if i % 100 == 0]
        for i in range(1000):
            if i > 0:
                self.canvas.create_text(375 + (i*100), 385, text=f'{coords_grid[i]}')
                self.canvas.create_text(375 - (i*100), 385, text=f'-{coords_grid[i]}')
                self.canvas.create_text(395, 395 + (i*100), text=f'-{coords_grid[i]}')
                self.canvas.create_text(395, 395 - (i*100), text=f'{coords_grid[i]}')
        # Фиксация элементов координатной сетки, чтобы в дальнейшем её не двигать
        self.canvas_grid = self.canvas.find_all()

    def gen_rectangle(self):
        all_rects = Figure(self.canvas, x1=250, y1=250, x2=275, y2=275)
        all_rects.create_rectangles()

    def gen_triangle(self):
        all_triangles = Figure(self.canvas, x1=300, y1=250, x2=285, y2=330, x3=265, y3=250)
        all_triangles.create_triangles()

    def gen_hexagon(self):
        all_hexagons = Figure(self.canvas, x1=235, y1=224, x2=265, y2=224, x3=280, y3=250,
                                   x4=265, y4=276, x5=235, y5=276, x6=220, y6=250)
        all_hexagons.create_hexagons()

    def gen_n_angles(self):
        all_n_angles = Figure(self.canvas, x1=250, y1=250, x2=290, y2=290)
        n, angle = self.n_angle.get().split(',')
        all_n_angles.create_n(int(n), int(angle))

    def make_strips(self): # 4.1
        strips = Figure(self.canvas, x1=375, y1=375, x2=395, y2=395)
        strips.create_3_strips()

    def make_overlapping(self): # 4.2
        overlapping = Figure(self.canvas, x1=375, y1=375, x2=405, y2=405,
                             x1_2=500, y1_2=500, x2_2=530, y2_2=530)
        overlapping.create_overlapping()

    def make_symmetric(self): # 4.3
        symmetric = Figure(self.canvas, x1=400, y1=400, x2=430, y2=430)
        symmetric.create_symmetric()

    def move(self):
        """Параллельный перенос"""
        deltax, deltay = self.deltaxy.get().split(',')
        all_figures = self.canvas.find_all()
        # Фигуры, которые можно двигать (без поля)
        movable_figures = list(set(all_figures) - set(self.canvas_grid))
        for each in movable_figures:
            self.canvas.move(each, deltax, deltay)
        self.canvas.after(10, self.move)

    def rotate(self):
        angle = int(self.rotating_angle.get())
        rotation = angle * math.pi / 180.0
        all_figures = self.canvas.find_all()
        movable_figures = list(set(all_figures) - set(self.canvas_grid))
        box_coords = []
        real_coords = []
        for each in movable_figures:
            box_coords.append(self.canvas.bbox(each))
            real_coords.append(self.canvas.coords(each))
        #print(box_coords)
        new_coords = []
        rotator = Figure(self.canvas)
        for item in box_coords:
            x1 = item[0]
            y1 = item[1]
            x2 = item[2]
            y2 = item[3]
            n = len(real_coords[box_coords.index(item)]) // 2
            new_coords.append(rotator.get_n_angles_coords(x1, y1, x2, y2, n, angle))
        #print(new_coords)
        #print(real_coords)
        for figure in movable_figures:
            self.rotating(figure, new_coords[movable_figures.index(figure)])

    def rotating(self, figure, *args):
        self.canvas.coords(figure, [float(x) for x in args[0]])

    def centerWindow(self):
        w = 880
        h = 96
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
