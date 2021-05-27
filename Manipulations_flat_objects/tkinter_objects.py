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
        self.rectangles_generated = False
        self.triangles_generated = False
        self.hexagons_generated = False
        self.ovals_generated = False

    def create_rectangles(self):
        while not self.rectangles_generated:
            for i in range(1000):
                self.rectangles.append(self.canvas.create_rectangle(
                    self.x1 + (i*40), self.y1, self.x2 + (i*40), self.y2, fill='black'))
                self.rectangles.append(self.canvas.create_rectangle(
                    self.x1 - (i*40), self.y1, self.x2 - (i*40), self.y2, fill='black'))
            self.rectangles_generated = True
        #for each in self.rectangles:
        #    self.canvas.move(each, -1, 0)
        #self.canvas.after(10, self.create_rectangles)


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
            all_hexs = self.canvas.find_all()
            #print(self.canvas.itemcget(all_hexs[0], 'offset'))
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
            #if self.hexagons.index(each) // 3 :
            #    self.canvas.itemconfigure(each, fill='blue')
            self.canvas.move(each, 10, 0)
            #self.canvas.move(each, -10, 3)
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

        # major and minor axes
        a = (x2 - x1) / 2.0
        b = (y2 - y1) / 2.0

        # center
        xc = x1 + a
        yc = y1 + b

        point_list = []
        for i in range(n):
            theta = (math.pi * 2) * (float(i) / n)

            x1 = a * math.cos(theta)
            y1 = b * math.sin(theta)

            # rotate x, y
            x = (x1 * math.cos(rotation)) + (y1 * math.sin(rotation))
            y = (y1 * math.cos(rotation)) - (x1 * math.sin(rotation))

            point_list.append(round(x + xc))
            point_list.append(round(y + yc))

        return point_list


class Objects(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.parent.title('Манипуляции с фигурами')
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()
        self.grid_generated = False

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
        self.canvas = Canvas(self.canvas_window, width=500, height=500)
        self.canvas.grid(row=0, column=0)
        # TODO: frontend
        self.axes_lines = []
        self.coords_grid_text = []
        for i in range(1000):  # x,y axes
            self.axes_lines.append(self.canvas.create_line(0 + (i*250), 250, 500 + (i*500), 250, width=2))
            self.axes_lines.append(self.canvas.create_line(0 - (i*250), 250, 500 - (i*500), 250, width=2))
            self.axes_lines.append(self.canvas.create_line(250, 500 + (i*500), 250, 0 + (i*500), width=2))
            self.axes_lines.append(self.canvas.create_line(250, 500 - (i*500), 250, 0 - (i*500), width=2))
        coords_grid = [i for i in range(1000000) if i % 100 == 0]
        for i in range(1000):
            if i > 0:
                self.coords_grid_text.append(self.canvas.create_text(250 + (i*100), 260, text=f'{coords_grid[i]}'))
                self.coords_grid_text.append(self.canvas.create_text(250 - (i*100), 260, text=f'-{coords_grid[i]}'))
                self.coords_grid_text.append(self.canvas.create_text(250, 250 + (i*100), text=f'-{coords_grid[i]}'))
                self.coords_grid_text.append(self.canvas.create_text(250, 250 - (i*100), text=f'{coords_grid[i]}'))
    def gen_rectangle(self):
        self.all_rects = Figure(self.canvas, x1=250, y1=250, x2=275, y2=275)
        self.all_rects.create_rectangles()

    def gen_triangle(self):
        self.all_triangles = Figure(self.canvas, x1=300, y1=250, x2=285, y2=330, x3=265, y3=250)
        self.all_triangles.create_triangles()

    def gen_hexagon(self):
        self.all_hexagons = Figure(self.canvas, x1=235, y1=224, x2=265, y2=224, x3=280, y3=250,
                                   x4=265, y4=276, x5=235, y5=276, x6=220, y6=250)
        self.all_hexagons.create_hexagons()

    def gen_n_angles(self):
        self.all_n_angles = Figure(self.canvas, x1=250, y1=250, x2=290, y2=290)
        n, angle = self.n_angle.get().split(',')
        self.all_n_angles.create_n(int(n), int(angle))

    def move(self):
        """Параллельный перенос"""
        while not self.grid_generated:
            all_figures = self.canvas.find_all()
            all_figures_objects = []
            for each in all_figures:
                all_figures_objects.append(each)
            deltax, deltay = self.deltaxy.get().split(',')
            for each in self.axes_lines:
                all_figures_objects.remove(each)
            for each in self.coords_grid_text:
                all_figures_objects.remove(each)
            self.grid_generated = True
        for each in all_figures_objects:
            self.canvas.move(each, deltax, deltay)
        self.canvas.after(2, self.move)

    def rotate(self):
        pass


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
