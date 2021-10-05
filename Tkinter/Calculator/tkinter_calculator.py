from tkinter import *
import re


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Калькулятор")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()

    def initUI(self):
        self.entry = Entry(self, width=50)
        self.entry.grid(row=0, columnspan=4)
        self.button_plus = Button(self, text='плюс', width=8)
        self.button_plus.grid(row=1, column=0)
        self.button_minus = Button(self, text='минус', width=8)
        self.button_minus.grid(row=1, column=1)
        self.button_multiply = Button(self, text='умножить', width=8)
        self.button_multiply.grid(row=1, column=2)
        self.button_erase = Button(self, text='очистить', width=8)
        self.button_erase.grid(row=1,column=3)
        self.button_equally = Button(self, text='равно', width=8)
        self.button_equally.grid(row=2, column=3)
        self.button_cnk = Button(self, text='C из n по k', width=8)
        self.button_cnk.grid(row=2, column=2)
        self.button_division = Button(self, text='делить', width=8)
        self.button_division.grid(row=2, column=1)
        self.button_degree = Button(self, text='в степени', width=8)
        self.button_degree.grid(row=2, column=0)
        self.pack()
        self.button_erase.bind('<Button-1>', self.button_erase_clicked)
        self.button_plus.bind('<Button-1>', self.button_plus_clicked)
        self.button_minus.bind('<Button-1>', self.button_minus_clicked)
        self.button_multiply.bind('<Button-1>', self.button_multiply_clicked)
        self.button_division.bind('<Button-1>', self.button_division_clicked)
        self.button_cnk.bind('<Button-1>', self.button_cnk_clicked)
        self.button_equally.bind('<Button-1>', self.button_equally_clicked)
        self.button_degree.bind('<Button-1>', self.button_degree_clicked)

    def button_erase_clicked(self, event):
        print('очистились')
        self.entry.delete(0, END)

    def button_plus_clicked(self, event):
        print('плюс')
        self.entry.insert(END, ' плюс ')

    def button_minus_clicked(self, event):
        print('минус')
        self.entry.insert(END, ' минус ')

    def button_multiply_clicked(self, event):
        print('умножить')
        self.entry.insert(END, ' умножить ')

    def button_division_clicked(self, event):
        print('поделили')
        self.entry.insert(END, ' делить ')

    def button_cnk_clicked(self, event):
        print('c из n по k')
        self.entry.delete(0, END)
        self.entry.insert(END, ' C из n=  по k= ')

    def button_degree_clicked(self, event):
        print('степень')
        self.entry.insert(END, ' степень ')

    def button_equally_clicked(self, event):
        print('равно')
        if 'С из' in self.entry.get() or 'С из' in self.entry.get():
            str = self.entry.get()
            str_com = str.split()
            n_index = str_com.index('n=')
            k_index = str_com.index('k=')
            num1_join = ' '.join(str_com[n_index+1:k_index])
            num2_join = ' '.join(str_com[k_index+1:9])
            num1 = self.calc(num1_join)
            num2 = self.calc(num2_join)
            n = num1
            k = num2
            print(num1_join, num2_join)
            if 0 <= k <= n:
                nn = 1
                kk = 1
                for t in range(1, min(k, n-k)+1):
                    nn *= n
                    kk *= t
                    n -= 1
                self.entry.delete(0, END)
                self.entry.insert(0, self.calc(nn // kk))
                print(nn // kk)
            else:
                self.entry.delete(0, END)
                self.entry.insert(0, '0')
        elif 'А из' in self.entry.get() or 'A из' in self.entry.get():
            str = self.entry.get()
            str_com = str.split()
            n_index = str_com.index('n=')
            k_index = str_com.index('k=')
            num1_join = ' '.join(str_com[n_index+1:k_index])
            num2_join = ' '.join(str_com[k_index+1:9])
            num1 = self.calc(num1_join)
            num2 = self.calc(num2_join)
            if 0 <= k <= n:
                nn = 1
                kk = 1
                for t in range(1, min(k, n - k) + 1):
                    nn *= n
                    kk *= t
                    n -= 1
                
                self.entry.delete(0, END)
                self.entry.insert(0, self.calc(nn // kk))
            else:
                self.entry.delete(0, END)
                self.entry.insert(0, '0')
        else:
            gets = self.entry.get()
            form = gets.split()
            if 'минус' in form:
                minus_index = form.index('минус')
                num1_join = ' '.join(form[0:minus_index])
                num2_join = ' '.join(form[minus_index:6])
                num1 = self.calc(num1_join)
                num2 = self.calc(num2_join)
            elif 'плюс' in form:
                plus_index = form.index('плюс')
                num1_join = ' '.join(form[0:plus_index])
                num2_join = ' '.join(form[plus_index:6])
                num1 = self.calc(num1_join)
                num2 = self.calc(num2_join)
            elif 'умножить' in form:
                multiply_index = form.index('умножить')
                num1_join = ' '.join(form[0:multiply_index])
                num2_join = ' '.join(form[multiply_index:6])
                num1 = self.calc(num1_join)
                num2 = self.calc(num2_join)
            elif 'делить' in form:
                division_index = form.index('делить')
                num1_join = ' '.join(form[0:division_index])
                num2_join = ' '.join(form[division_index:6])
                num1 = self.calc(num1_join)
                num2 = self.calc(num2_join)
            elif 'степень' in form:
                degree_index = form.index('степень')
                num1_join = ' '.join(form[0:degree_index])
                num2_join = ' '.join(form[degree_index:6])
                num1 = self.calc(num1_join)
                num2 = self.calc(num2_join)

            
            if 'плюс' in form:
                result_plus = num1 + num2
                str_plus = self.calc(result_plus)
                self.entry.insert(END, f' = {str_plus}')
                if result_plus == 0:
                    self.entry.insert(END, f'ноль')
            elif 'минус' in form:
                result_subtraction = num1 - num2
                str_subtraction = self.calc(result_subtraction)
                self.entry.insert(END, f' = {str_subtraction}')
                if result_subtraction == 0:
                    self.entry.insert(END, f'ноль')
            elif 'умножить' in form:
                result_multiply = num1 * num2
                str_multiply = self.calc(result_multiply)
                self.entry.insert(END, f' = {str_multiply}')
                if result_multiply == 0:
                    self.entry.insert(END, f'ноль')
            elif 'делить' in form:
                result_division = num1 / num2
                str_division = self.calc(result_division)
                self.entry.insert(END, f' = {str_division}')
                if result_division == 0:
                    self.entry.insert(END, f'ноль')
            elif 'степень' in form:
                result_degree = num1 ** num2
                str_degree = self.calc(result_degree)
                self.entry.insert(END, f' = {str_degree}')
                if result_degree == 0:
                    self.entry.insert(END, f'ноль')

    def calc(self, var):
        a = {"один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8,

             "девять": 9, "ноль": 0}

        b = {"десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,

             "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19}

        c = {"двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70,

             "восемьдесят": 80, "девяносто": 90}

        d = {100: "сто", 200: "двести", 300: "триста", 400: "четыреста", 500: "пятьсот", 600: "шестьсот",
             700: "семьсот",

             800: "восемьсот", 900: "девятьсот"}
        th = {1: ['', "один", "два", 'три', 'четыре'],
              1000: ['тысяч ', 'одна тысяча ', 'две тысячи ', 'три тысячи ', 'четыре тысячи '],
              1000000: ['миллионов ', 'один миллион', 'два миллиона ', 'три миллиона ', 'четыре миллиона '],
              1000000000: ['миллиардов ', 'один миллиард ', 'два миллиарда ', 'три миллиарда ', 'четыре миллиарда ']}

        def intg(a, b, c, d, th, var):
            kts = 1
            res = str()
            while var // kts:
                rch = (var % (kts * 1000)) // kts  # Делит число на тысячи

                if rch != 0:
                    if rch % 100 > 19 or rch % 100 < 10:  # Проверка от 10 до 19

                        if rch % 10 > 0 and rch % 10 < 5:  # Проверка от 1 до 4

                            res = th[kts][rch % 10] + res

                        else:  # Проверка на оставшиеся значения
                            res = th[kts][0] + res

                            for k, v in a.items():  # Проверка цифр
                                if v == rch % 10 and rch % 10 not in [0, 1, 2, 3, 4]:
                                    res = str(k) + " " + res

                        for k, v in c.items():  # Проверка десятков
                            if v == rch % 100 // 10 * 10:
                                res = str(k) + " " + res

                    else:  # Проверка на значения от 10 до 19
                        res = th[kts][0] + res
                        for k, v in b.items():
                            if v == rch % 100:
                                res = str(k) + " " + res

                    # if rch % 100 == 0 and rch//100 !=0:
                    # res = th[kts][0]+res
                    for k, v in d.items():  # Проверка сотен
                        if k == rch // 100 * 100:
                            res = str(v) + " " + res

                kts *= 1000
            return res

        def flo(a, b, c, d, th, var):
            des = {1: ' десятых', 3: ' тысячных', 4: ' десьтитысячных', 2: ' сотых', 5: ' стотысячных'}
            f = int(var)
            var = var - int(var)
            var = round(var, 4)
            var = str(var).replace("0.", '')
            vard = re.sub(r'^0+', '', var)
            rez = ""
            if vard == "":
                rez = intg(a, b, c, d, th, f)
            else:
                if f % 100 > 20 or f % 100 < 10:
                    if f == 0:
                        rez = "ноль целых "
                    if f % 10 == 1:
                        rez = "одна целая "
                        f -= 1
                    elif f % 10 == 2:
                        rez = "две целых "
                        f -= 2
                if rez == "":

                    rez = intg(a, b, c, d, th, f) + 'целых '
                else:
                    rez = intg(a, b, c, d, th, f) + rez
                dopp = len(var)
                rez1 = ''

                vard = int(vard)
                if vard % 100 > 20 or vard % 100 < 10:
                    if vard % 10 == 1:
                        rez1 = "одна"
                        var = var[0:len(var) - 1] + "0"
                    elif vard % 10 == 2:
                        rez1 = "две"
                        var = var[0:len(var) - 1] + "0"
                var = re.sub(r'^0+', '', var)
                if var == "":
                    var = 0
                var = int(var)
                rez = rez + intg(a, b, c, d, th, var) + rez1 + des[dopp]
            return rez

        def dd(s, b):  # Функция проверки и нахождния от 10 - 19
            for i in b:
                if i in s:
                    return b[i]
            return 0

        def inp(s, a, b, c):  # Проверка от 0 - 9 и 20 - 99
            k = dd(s, b)  # Проверка от 10-19
            if k > 0:
                return k
            k = -1
            for i in c:
                if i in s:
                    k += c[i]
                    break
            for i in a:
                if i in s:
                    k += a[i]
                    break
            if k == -1:
                return "В словах допущена ошибка!"  # Ни одного сова не найдено - неверн введенные сова
            k += 1
            return k

        # def outp(var):
        #    if var

        if type(var) == str:
            var.strip()
            if re.search(r'[a-z]|[0-9]', var, re.I):
                return "Введен неверный символ"
            var = re.split(r'\s+', var)
            return inp(var, a, b, c)
        elif type(var) == int:
            if var < 0:
                return 'минус ' + intg(a, b, c, d, th, abs(var))
            else:
                return intg(a, b, c, d, th, var)
        elif type(var) == float:
            if var < 0:
                return 'минус ' + flo(a, b, c, d, th, abs(var))
            else:
                return flo(a, b, c, d, th, var)

    def centerWindow(self):
        w = 300
        h = 80
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
    root = Tk()
    ex = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
