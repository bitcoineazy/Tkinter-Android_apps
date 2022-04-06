import tkinter as tk
import math


class Circle:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tkinter Circle")
        self.center_window()

        self.speed = 0

        self.canvas = tk.Canvas(self.window, width=600, height=600)
        self.direction = self.canvas.create_oval(100, 100, 500, 500, fill='red')
        self.circle = self.canvas.create_oval(485, 285, 515, 315, fill='black')

        self.move_circle()
        self.canvas.pack()
        self.window.mainloop()

    def move_circle(self):
        tick = 1 + self.speed
        x = 300 + 200 * math.cos(tick)
        y = 300 + 200 * math.sin(tick)
        self.canvas.coords(self.circle, x - 24.0, y - 24.0, x + 24.0, y + 24.0)
        self.speed += 0.02
        self.canvas.after(10, self.move_circle)

    def center_window(self):
        w = 600
        h = 600
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    tkinter_circle = Circle()


if __name__ == '__main__':
    main()