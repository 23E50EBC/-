import tkinter
from tkinter import font
import random

class Base1:

    def __init__(self):
        self.window1 = tkinter.Tk()
        self.wight,self.height = (1024,800)  #窗口大小控件
        self.window1.geometry(f"{self.wight}x{self.height}")

        #题目初始化区域
        self.random_number_1 = 0
        self.random_number_2 = 0
        self.random_operation = 0
        self.problem_display_string = ""
        self.user_answer = 0
        self.expected_answer = 0
        self.answer_color = "gray"

        self.font_size = min(self.wight//12,self.height//12)
        self.font1 = font.Font(family='Arial', size=self.font_size)

        self.frame1 = tkinter.Frame(master=self.window1, bd=2, relief="solid")
        #创建一个框，这个框用来装题目
        self.frame1.pack(side="top",fill="both",expand=True)
        #这是1下面的框
        self.frame1down = tkinter.Frame(master=self.window1, bd=2, relief="solid")
        self.frame1down.pack(side="top", fill="both", expand=True)

        #配置框沿“上面”对齐，并且填满
        self.frame2 = tkinter.Frame(master=self.frame1down, bd=2, relief="solid")
        #类似的，这个是按钮框
        self.frame2.pack(side="left", fill="both", expand=True)

        #这个是检验答案正确与否的框
        self.frame3 = tkinter.Frame(master=self.frame1down, bd=2, relief="solid")
        self.frame3.pack(side="left", fill="both", expand=True)
        self.frame3.config(bg=self.answer_color)

        #第一个是问题
        self.q_entry = tkinter.Entry(master=self.frame1,font=self.font1)
        self.q_entry.grid(row=0,column=0)
        #第二个是答案
        self.a_entry = tkinter.Entry(master=self.frame1,font=self.font1)
        self.a_entry.grid(row=1,column=0)

        #下面是9个按钮，但是因为创建顺序错误，这个按钮的实际数字键是编号+1
        self.num_button0 = tkinter.Button(master=self.frame2,text="1",font=self.font1,
                                          command=lambda :self._test_func(1))
        self.num_button0.grid(row=0,column=0,sticky='nsew')
        self.num_button1 = tkinter.Button(master=self.frame2,text="2", font=self.font1,
                                          command=lambda: self._test_func(2))
        self.num_button1.grid(row=0, column=1, sticky='nsew')
        self.num_button2 = tkinter.Button(master=self.frame2, text="3", font=self.font1,
                                          command=lambda: self._test_func(3))
        self.num_button2.grid(row=0, column=2, sticky='nsew')
        self.num_button3 = tkinter.Button(master=self.frame2, text="4", font=self.font1,
                                          command=lambda: self._test_func(4))
        self.num_button3.grid(row=1, column=0, sticky='nsew')
        self.num_button4 = tkinter.Button(master=self.frame2, text="5", font=self.font1,
                                          command=lambda: self._test_func(5))
        self.num_button4.grid(row=1, column=1, sticky='nsew')
        self.num_button5 = tkinter.Button(master=self.frame2, text="6", font=self.font1,
                                          command=lambda: self._test_func(6))
        self.num_button5.grid(row=1, column=2, sticky='nsew')
        self.num_button6 = tkinter.Button(master=self.frame2, text="7", font=self.font1,
                                          command=lambda: self._test_func(7))
        self.num_button6.grid(row=2, column=0, sticky='nsew')
        self.num_button7 = tkinter.Button(master=self.frame2, text="8", font=self.font1,
                                          command=lambda: self._test_func(8))
        self.num_button7.grid(row=2, column=1, sticky='nsew')
        self.num_button8 = tkinter.Button(master=self.frame2, text="9", font=self.font1,
                                          command=lambda: self._test_func(9))
        self.num_button8.grid(row=2, column=2, sticky='nsew')
        self.num_button9 = tkinter.Button(master=self.frame2, text="0", font=self.font1,
                                          command=lambda: self._test_func(0))
        self.num_button9.grid(row=0, column=3, sticky='nsew')
        self.num_button_confirm = tkinter.Button(master=self.frame2, text="确认答案", font=self.font1,
                                          command=lambda: self._answer_confirm())
        self.num_button_confirm.grid(row=1, column=3, sticky='nsew')
        self.num_button_reset = tkinter.Button(master=self.frame2, text="重置问题", font=self.font1,
                                                 command=lambda: self._reset_problem())
        self.num_button_reset.grid(row=2, column=3, sticky='nsew')


    def _test_func(self,num):
        #懒得改了直接包装了
        self._answer_insert(num)

    def _answer_insert(self,num):
        #这个是往答案entry里插入键盘数字的方法
        self.a_entry.insert(index=tkinter.END,string=str(num))

    def _answer_confirm(self):
        self.user_answer = int(self.a_entry.get())
        print(self.user_answer)
        if self.user_answer == self.expected_answer:
            print("True")
            self.answer_color = "green"
            self.frame3.config(bg=self.answer_color)
        else:
            print("False")
            self.answer_color = "red"
            self.frame3.config(bg=self.answer_color)
            self.a_entry.delete(first=0,last=tkinter.END)

    def _reset_problem(self):
        self.random_number_1 = random.randint(0, 999)
        self.random_number_2 = random.randint(0, 999)
        self.random_operation = random.randint(1,4)
        print(f"random_number_1={self.random_number_1},random_number_2{self.random_number_2},random_operation{self.random_operation}")
        if self.random_operation == 1:
            self.problem_display_string = f"{self.random_number_1} + {self.random_number_2}"
            self.expected_answer = self.random_number_1 + self.random_number_2
            print(f"self.expected_answer={self.expected_answer}")
        elif self.random_operation == 2:
            #这里的小小改动保证了被减数一定比减数大
            self.problem_display_string = f"{max(self.random_number_1,self.random_number_2)} - {min(self.random_number_1 , self.random_number_2)}"
            self.expected_answer = max(self.random_number_1,self.random_number_2)-min(self.random_number_1 , self.random_number_2)
            print(f"self.expected_answer={self.expected_answer}")
        elif self.random_operation == 3:
            self.problem_display_string = f"{self.random_number_1} × {self.random_number_2}"
            self.expected_answer = self.random_number_1 * self.random_number_2
            print(f"self.expected_answer={self.expected_answer}")
        elif self.random_operation == 4:
            #这一点保证了被除数一定比除数大，地板除得到商和余数
            self.problem_display_string = f"{max(self.random_number_1,self.random_number_2)} ÷ {min(self.random_number_1,self.random_number_2)}"
            self.expected_answer = max(self.random_number_1,self.random_number_2) // min(self.random_number_1,self.random_number_2)
            print(f"self.expected_answer={self.expected_answer}")

        self.q_entry.delete(first=0,last=tkinter.END)
        self.q_entry.insert(index=0,string=self.problem_display_string)
        self.answer_color = "gray"
        self.frame3.config(bg=self.answer_color)
        self.a_entry.delete(first=0,last=tkinter.END)


    def run(self):
        self.window1.mainloop()


if __name__ == "__main__":
    base = Base1()
    base.run()
