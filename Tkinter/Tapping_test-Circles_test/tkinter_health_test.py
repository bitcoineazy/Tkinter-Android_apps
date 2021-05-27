from tkinter import *
from tkinter import filedialog as fd
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
import time
import winsound


class Circles:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval([self.x1, self.y1], [self.x2, self.y2], fill="red")
        self.attempts = 0
        self.coords = self.canvas.coords(self.ball)

    def move_ball_1(self):
        random_tick = random.randint(1,10)
        deltax = 1
        deltay = 0
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(random_tick, self.move_ball_1)

    def move_ball_2(self):
        random_tick = random.randint(1, 10)
        deltax = -1
        deltay = 0
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(random_tick, self.move_ball_2)
        self.end_cord = self.canvas.coords(self.ball)

    def refresh_ball(self):
        self.canvas.delete('all')
        self.ball1 = Circles(self.canvas, 0, 250, 50, 300) #0, 0, 50, 50 - края
        self.ball2 = Circles(self.canvas, 500, 250, 450, 300) #450, 450, 500, 500
        self.canvas.addtag_closest('ball_1', 0, 250)
        self.canvas.addtag_closest('ball_2', 500, 250)
        self.ball1.move_ball_1()
        self.ball2.move_ball_2()

    def show_range(self):
        centre_1 = 25
        centre_2 = 475


class HealthTest(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.parent.title('Тест Здоровья')
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()
        self.count = 0
        self.results = []
        self.press_amounts = 0
        self.press_amounts_dict = {}
        self.flag = False #переменная чтобы фиксировать кол-во нажатий на времени % 5 == 0 только один раз

    def initUI(self):
        self.test_circles = Button(self, text='Тест Точность', command=self.circles, width=16)
        self.test_sounds = Button(self, text='Тэппинг-тест', command=self.tapping, width=16)
        self.instruction = Button(self, text='Инструкция', command=self.instruction, width=16)
        self.refresh_button = Button(self, text='Обновить', command=self.refresh_button, width=16)
        self.test_circles.grid(row=0, column=1)
        self.test_sounds.grid(row=0, column=0)
        self.instruction.grid(row=0, column=2)
        self.refresh_button.grid(row=0, column=3)

    def circles(self):
        self.circles_window = Toplevel(self)
        self.circles_window.title('Тест на точность')
        self.circles_begin_button = Button(self.circles_window, text='Начать тест', command=self.circles_logic, width=16)
        self.circles_save = Button(self.circles_window, text='Сохранить результаты', command=self.save_button, width=len('Сохранить результаты'))
        self.circles_begin_button.grid(row=0, column=0)
        self.circles_save.grid(row=0, column=1)

    def circles_logic(self):
        self.circles_test = Toplevel(self.circles_window)
        self.canvas = Canvas(self.circles_test, width=500, height=500)
        self.canvas.grid(row=0, column=0)
        self.canvas.focus()
        self.ball1 = Circles(self.canvas, 0, 250, 50, 300)
        self.ball2 = Circles(self.canvas, 500, 250, 450, 300)
        self.canvas.addtag_closest('ball_1', 0, 250)
        self.canvas.addtag_closest('ball_2', 500, 250)
        self.canvas.bind_all('<space>', self.circle_test)

    def circle_test(self, event):
        if self.count <= 10:
            ball_1 = self.canvas.find_withtag('ball_1')
            x1, x2, y1, y2 = self.canvas.bbox(ball_1)
            ball_2 = self.canvas.find_withtag('ball_2')
            x1_2, x2_2, y1_2, y2_2 = self.canvas.bbox(ball_2)
            self.x1 = x1
            self.x1_2 = x1_2
            self.ball1.refresh_ball()
            self.ball2.refresh_ball()
            self.results.append(abs(x1_2-x1))
            self.count += 1
        else:
            print('игра окончена')
            print(self.results)
            self.count = 0
            self.circles_test.destroy()
            self.stats_window = Toplevel(self)
            self.stats_window.title('Результаты теста точность')
            #self.stats_frame = Frame(self.stats_window)
            self.stats = Figure(figsize=(10, 10), dpi=100)
            fn = self.stats.add_subplot(1,1,1)
            x = [i+1 for i in range(10)]
            y = self.results[1:]
            try:
                fn.plot(x, y)
                fn.set_xlabel('Попытки', color='blue')
                fn.set_ylabel('Точность соотношения шариков(расстояние между ними)', color='red')
                fn.set_title('Тест на точность')
                self.stats_canvas = FigureCanvasTkAgg(self.stats, self.stats_window)
                self.stats_canvas.get_tk_widget().grid()
            except ValueError:
                self.circles_test.destroy()
                print('Ошибка, нажмите обновить чтобы сбросить значения предыдущего теста')

    def refresh_button(self):
        self.results = []
        self.press_amounts_dict = {}

    def tapping(self):
        self.tapping_test = Toplevel(self)
        self.tapping_test.title('Тэппинг тест')
        self.tapping_begin_button = Button(self.tapping_test, text='Начать тест', command=self.tapping_logic, width=16)
        self.tapping_save = Button(self.tapping_test, text='Сохранить результаты', command=self.save_button, width=len('Сохранить результаты'))
        self.tapping_begin_button.grid(row=0, column=0)
        self.tapping_save.grid(row=0, column=1)

    def tapping_logic(self):
        self.timer_window = Toplevel(self.tapping_test)
        self.timer_window.title('Тэппинг тест')
        self.timer_label = Label(self.timer_window, justify='center', padx=75, pady=75)
        self.timer_label.grid(row=0, column=0)
        self.time_start_count = time.time()
        self.timer_label.config(text='0', font='times 25')
        w = 200
        h = 200
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.timer_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        winsound.Beep(300, 500)
        self.timer_label.after(1, self.tapping_engine)
        self.timer_label.bind_all('<space>', self.press_amount)

    def press_amount(self, event):
        self.press_amounts += 1

    def tapping_engine(self):
        start_test_accurate = round(time.time() - self.time_start_count, 3)
        start_test = round(start_test_accurate, 1)
        self.timer_label.config(text=start_test, font='times 25')
        self.timer_label.after(1, self.tapping_engine)
        if 5 < start_test_accurate < 5.5 and self.flag == False:
            self.flag = True #переменная чтобы фиксировать кол-во нажатий только один раз
            self.press_amounts_dict['1'] = self.press_amounts
            print(self.press_amounts_dict)
            self.press_amounts = 0
        if 10 < start_test_accurate < 10.5 and self.flag == True:
            self.flag = False
            self.press_amounts_dict['2'] = self.press_amounts
            print(self.press_amounts_dict)
            self.press_amounts = 0
        if 15 < start_test_accurate < 15.5 and self.flag == False:
            self.flag = True
            self.press_amounts_dict['3'] = self.press_amounts
            print(self.press_amounts_dict)
            self.press_amounts = 0
        if 20 < start_test_accurate < 20.5 and self.flag == True:
            self.flag = False
            self.press_amounts_dict['4'] = self.press_amounts
            print(self.press_amounts_dict)
            self.press_amounts = 0
        if 25 < start_test_accurate < 25.5 and self.flag == False:
            self.flag = True
            self.press_amounts_dict['5'] = self.press_amounts
            print(self.press_amounts_dict)
            self.press_amounts = 0
        if 30 < start_test_accurate < 30.1 and self.flag == True:
            self.flag = False
            self.press_amounts_dict['6'] = self.press_amounts
            print(self.press_amounts_dict)
            self.press_amounts = 0
        if start_test_accurate >= 30.2:
            print('тэппинг тест пройден')
            print(self.press_amounts_dict)
            self.timer_window.destroy()
            self.stats_tapping_window = Toplevel(self.tapping_test)
            self.stats_tapping_window.title('Результаты тэппинг-теста')
            # self.stats_frame = Frame(self.stats_window)
            x = [i for i in range(6)]
            y = [self.press_amounts_dict['1'], self.press_amounts_dict['2'], self.press_amounts_dict['3'],
                 self.press_amounts_dict['4'], self.press_amounts_dict['5'], self.press_amounts_dict['6']]
            self.stats_tapping = Figure(figsize=(10, 10), dpi=100)
            fn = self.stats_tapping.add_subplot(1, 1, 1)
            try:
                fn.plot(x, y)
                fn.set_xlabel('5 сек промежутки', color='blue')
                fn.set_ylabel('Кол-во нажатий в промежуток', color='red')
                fn.set_title('Тэппинг-тест')
                self.stats_canvas_tapping = FigureCanvasTkAgg(self.stats_tapping, self.stats_tapping_window)
                self.stats_canvas_tapping.get_tk_widget().grid()
            except ValueError:
                self.tapping_test.destroy()
                print('Ошибка, нажмите обновить чтобы сбросить значения предыдущего теста')

    def instruction(self):
        help_texts = 'Тест на точность\n' \
                     'Тест запускается при нажатии на SPACE\n' \
                     'Всего 10 попыток\n' \
                     'Программа считает расстояние между центрами шариков\n' \
                     'Идеальный результат - 0(т.е. полностью совмещены)\n' \
                     'С каждой попыткой скорость увеличивается\n' \
                     'По окончанию теста программа выводит\nграфик точности между попытками\n\n\n' \
                     'Тэппинг-тест\n' \
                     'Запускается сразу при нажатии Начать тест\n' \
                     'Программа считает кол-во нажатий на клавишу SPACE\n' \
                     'Тест длится 30 сек\n' \
                     'По окончанию теста программа выводит график\n' \
                     'Кол-ва нажатий в 5-секундные промежутки во время теста\n\n' \
                     'Сохранить результаты теста можно в формате .csv,\n' \
                     'Нажав на кнопку Сохранить результаты в окне существующего теста\n\n'\
                    'Чтобы заново начать тест надо нажать Обновить в главном окне'
        self.instruction_window = Toplevel(self)
        self.help_text = Text(self.instruction_window)
        self.help_text.insert(1.0, help_texts)
        self.help_text.grid(row=0, column=0)

    def save_button(self):
        files = [('CSV Files', '*.csv')]
        file_name = fd.asksaveasfile(filetypes=files, defaultextension=files)
        try:
            with open(file_name.name, mode='w', newline='') as f:
                data = [['Попытка', 'Скорость реакции'],
                        [1,self.results[1]],
                        [2,self.results[2]],
                        [3,self.results[3]],
                        [4,self.results[4]],
                        [5,self.results[5]],
                        [6,self.results[6]],
                        [7,self.results[7]],
                        [8,self.results[8]],
                        [9,self.results[9]],
                        [10,self.results[10]]]
                writer = csv.writer(f)
                writer.writerows(data)
        except PermissionError:
            print('Закройте файл, чтобы сохранить')

    def centerWindow(self):
        w = 488
        h = 26
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
    root = Tk()
    ex = HealthTest(root)
    root.mainloop()

if __name__ == '__main__':
    main()
